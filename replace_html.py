import re

with open('c:/Users/ASUS/Desktop/EvrenAKI/KITAP4/websitesi/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    ('<title>Evrenakı Teorisi - 4 Boyutlu Hidrodinamik Evren Modeli</title>', '<title>Proje Başlığı</title>'),
    ('<h1 class="splash-title">EVRENAKI</h1>', '<h1 class="splash-title">PROJE BAŞLIĞI</h1>'),
    ('<p class="splash-subtitle">Kozmik Girdap Mekaniği</p>', '<p class="splash-subtitle">Proje Alt Başlığı</p>'),
    ('''<p class="splash-statement">"Evrenakı Teorisi\'nde varsayımlara yer yoktur; her iddia mutlaka kanıtlarla mühürlenmiştir."</p>''', '<p class="splash-statement">"Buraya projenizle ilgili bir slogan veya giriş cümlesi gelebilir."</p>'),
    ('<h2>EVRENAKI</h2>', '<h2>PROJE ADI</h2>'),
    ('<span>Teorik Fizik & Kozmoloji</span>', '<span>Kategori / Alt Başlık</span>'),
    ('<div class="hero-badge">YENİ KOZMOLOJİK PARADİGMA</div>', '<div class="hero-badge">YENİ PROJE ETİKETİ</div>'),
    ('<h1 class="hero-title">Evrenakı Teorisi</h1>', '<h1 class="hero-title">Proje Başlığı</h1>'),
    ('<p class="hero-subtitle">Uzay boşluğu bir hiçlik değil; Compton frekansında dönen parçacıklar ve süper-akışkan bir okyanustur.</p>', '<p class="hero-subtitle">Buraya projenizin açıklamasını, ana fikrini veya özetini yazabilirsiniz.</p>'),
    ("EVRENAKI TEORİSİ\'NİN ANA UNSURLARI", "PROJENİN ANA UNSURLARI"),
    ('''<h3>Plenum (Sürekli Ortam)</h3>
                                        <p>Uzay boşluğu viskozitesi sıfır olan sıkıştırılabilir bir Cosmofluid ile doludur. Kütleçekimi bu akışkandaki basınç gradyanıdır.</p>''', '''<h3>Özellik 1</h3>
                                        <p>Birinci özellik açıklaması.</p>'''),
    ('''<h3>Evrensel Spin İlkesi</h3>
                                        <p>Atom altı parçacıklar soyut olasılık bulutları değil, Compton frekansında fiziksel olarak dönen 4 boyutlu girdapsal yapılardır.</p>''', '''<h3>Özellik 2</h3>
                                        <p>İkinci özellik açıklaması.</p>'''),
    ('''<p>“Okuyacağınız bu kitap, geçmişin bilimsel dehalarıyla savaşıyor izlenimi uyandırabilir; oysa gerçekte, o dehaların unutulan doğrularının melodisini yeniden seslendirmekte ve onları devasa bir akışkanlar mekaniği senfonisinde birleştirmektedir.”</p>''', '''<p>“Buraya kitabınızdan veya projenizden bir alıntı koyabilirsiniz.”</p>'''),
    ('<span>— Evrenakı Teorisi, Önsöz</span>', '<span>— Proje, Önsöz</span>'),
    ('<p>Teorinin geliştirilmesi aşamasında bilim insanlarından gelen zorlu itirazlar, Shapiro Gecikmesi hesaplarındaki rölativistik açmazlar ve bunlara verilen matematiksel/hidrodinamik çözümler.</p>', '<p>Buraya hakem değerlendirmeleri veya düzeltme notlarının kısa açıklaması gelebilir.</p>'),
    ('<p>Mikro girdapların merkezcil itim (kütleçekim) ile birikerek makro bir küresel cisim oluşturma sürecini canlı izleyin.</p>', '<p>Simülasyon veya görsel içerikleriniz için açıklama alanı.</p>'),
    ('<iframe id="sim-frame" src="Simulasyon/boyut_simulasyonu.html" frameborder="0"></iframe>', '<iframe id="sim-frame" src="Simulasyon/simulasyon.html" frameborder="0"></iframe>')
]

for old, new in replacements:
    html = html.replace(old, new)

with open('c:/Users/ASUS/Desktop/EvrenAKI/KITAP4/websitesi/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated successfully")
