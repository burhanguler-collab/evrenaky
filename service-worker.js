/* ==========================================================================
   EVRENAKI — SERVİS İŞÇİSİ
   ==========================================================================
   SÜRÜM DAMGASI aşağıdaki satırdadır ve HER YAYINDA firebase_update_site.py
   tarafından otomatik güncellenir. Elle değiştirmek gerekmez.
   ------------------------------------------------------------------------
   13 Ağu 2026'da YENİDEN YAZILDI. Eski sürümün üç kusuru vardı:

   1. `index.html` ASSETS içinde ön-önbellekleniyor ve fetch işleyicisinde
      CACHE-FIRST sunuluyordu. Sonuç: Firebase `no-cache` gönderse bile işçi
      ESKİ index.html'i veriyor, o da eski `app.js?v=NN`'i çağırıyordu.
      Bir yayın sonrası düzeltme ancak İKİNCİ açılışta görünüyordu
      (stale-while-revalidate arka planda tazeliyordu). Gerçek yaşanan kusur
      buydu: app.js'te bir sözdizimi hatası düzeltildi, deploy edildi, ama
      sitede hâlâ eski hata görünüyordu.

   2. CACHE_NAME elle yazılmış sabit bir tarih dizgisiydi
      ('project-cache-20260810-1725'). Değişmediği sürece activate olayı eski
      önbelleği silmiyordu. Kimse elle artırmayı hatırlamazsa önbellek
      süresiz yaşıyordu.

   3. ASSETS içinde 'app.js' SÜRÜM SORGUSU OLMADAN yazılıydı; sayfa ise
      'app.js?v=28' istiyor. `caches.match` sorgu dizesini de karşılaştırdığı
      için bu girdi hiç işe yaramıyor, yalnızca yanıltıyordu.

   YENİ STRATEJİ — üç kanal:
     • GEZİNME ve HTML  → AĞ-ÖNCELİKLİ. Kabuk asla bayat kalmaz; çevrimdışıysa
                          önbellekten döner. Kusur 1'i kökten kapatır.
     • .md metinler     → AĞ-ÖNCELİKLİ (eskiden de böyleydi, korunuyor).
     • Diğer varlıklar  → önbellek-öncelikli + arka planda tazeleme.
                          Bunlar `?v=` ile sürümlendiği için bayatlama riski yok.
   ========================================================================== */

const SW_SURUM  = '20260815-082701';          /* yayında otomatik damgalanır */
const CACHE_NAME = 'evrenaki-' + SW_SURUM;

/* Çevrimdışı iskelet. index.html BİLEREK burada — ama yalnız ÇEVRİMDIŞI
   yedek olarak kullanılır, asla önbellekten öncelikli sunulmaz. */
const ASSETS = [
  'index.html',
  'index.css',
  'manifest.json',
  'Gorseller/pwa_icon.png'
];

self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      /* addAll tek bir dosya 404 verirse TAMAMEN başarısız olur ve işçi hiç
         kurulmaz. Tek tek ekleyip hataları yutuyoruz. */
      return Promise.all(ASSETS.map(u =>
        cache.add(u).catch(err => console.warn('[SW] atlandı:', u, err))
      ));
    })
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => {
          console.log('[SW] eski önbellek silindi:', k);
          return caches.delete(k);
        })
      ))
      .then(() => self.clients.claim())
  );
});

/* Yardımcı: yanıtı önbelleğe koy (yalnız başarılı ve temel yanıtlar) */
function onbellekle(request, response){
  if (!response || response.status !== 200 || response.type === 'opaque') return;
  const clone = response.clone();
  caches.open(CACHE_NAME).then(cache => cache.put(request, clone));
}

self.addEventListener('fetch', event => {
  const req = event.request;

  /* Yalnız kendi kaynağımız; eklenti/CDN isteklerine dokunma */
  if (!req.url.startsWith(self.location.origin)) return;
  /* GET dışını hiç ele almayalım */
  if (req.method !== 'GET') return;

  const url = new URL(req.url);

  /* --- 1) GEZİNME ve HTML: AĞ-ÖNCELİKLİ --------------------------------
     Kabuk her zaman ağdan gelir. Yayın yapılınca değişiklik İLK açılışta
     görünür. Ağ yoksa önbellekteki index.html devreye girer. */
  const gezinme = req.mode === 'navigate' ||
                  (req.headers.get('accept') || '').includes('text/html');
  if (gezinme) {
    event.respondWith(
      fetch(req)
        .then(res => { onbellekle(req, res); return res; })
        .catch(() => caches.match(req).then(c => c || caches.match('index.html')))
    );
    return;
  }

  /* --- 2) KİTAP METİNLERİ (.md): AĞ-ÖNCELİKLİ -------------------------- */
  if (url.pathname.includes('/Metin/') || url.pathname.endsWith('.md')) {
    event.respondWith(
      fetch(req)
        .then(res => { onbellekle(req, res); return res; })
        .catch(() => caches.match(req))
    );
    return;
  }

  /* --- 3) DİĞER VARLIKLAR: önbellek-öncelikli + arka planda tazele ------
     app.js / index.css `?v=` ile sürümlendiği için sürüm artınca URL değişir
     ve otomatik olarak yeni dosya çekilir. */
  event.respondWith(
    caches.match(req).then(cached => {
      if (cached) {
        fetch(req).then(res => onbellekle(req, res)).catch(() => {});
        return cached;
      }
      return fetch(req).then(res => { onbellekle(req, res); return res; });
    })
  );
});
