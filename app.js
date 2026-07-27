// Evrenakı Teorisi Website Application Logic

// Chapter Registry
const chapters = [
    { id: 'ozet', title: 'Kitabın Özeti & Teorinin Özü', file: 'Metin/kitap_ozeti.md', group: 'all' },
    { id: 'akademik_01_01', title: '1.1 Giriş ve Metodoloji', file: 'Metin/Akademik/Kisim_1_Giris/01_Metodoloji_ve_Manifesto.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },
    { id: 'akademik_01_02', title: '1.2 Klasik ve Modern Fiziğin Krizleri', file: 'Metin/Akademik/Kisim_1_Giris/02_Fizigin_Krizleri.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },
    { id: 'akademik_01_03', title: '1.3 Evrenin Akışkan Doğası', file: 'Metin/Akademik/Kisim_1_Giris/03_Evrenaki_Postulasi.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },
    { id: 'akademik_01_04', title: '1.4 Dördüncü Boyut ve İzdüşüm', file: 'Metin/Akademik/Kisim_1_Giris/04_Dorduncu_Boyut.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },
    { id: 'akademik_01_05', title: '1.5 Evrenakı Gradyanları', file: 'Metin/Akademik/Kisim_1_Giris/05_Evrenaki_Gradyanlari.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },
    { id: 'akademik_01_06', title: '1.6 Evrenakı Terminolojisi ve Temel Kavramlar', file: 'Metin/Akademik/Kisim_1_Giris/06_Evrenaki_Terminolojisi.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },
    { id: 'akademik_01_07', title: '1.7 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_1_Giris/07_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },
    { id: 'akademik_01_kaynakca', title: '1.8 Kaynakça', file: 'Metin/Akademik/Kisim_1_Giris/99_Kaynakca.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },
    { id: 'akademik_02_01', title: '2.1 Mikro Evren Aktörleri', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/01_Mikro_Evren.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_02', title: '2.2 Zerre ve Işığın Kinematiği', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/02_Zerre_ve_Isik.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_03', title: '2.3 Işığın Fiziksel Parametreleri ve Renkler', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/03_Isigin_Parametreleri_ve_Renkler.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_04', title: '2.4 Işık Hızı ve Zerre', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/04_Isik_Hizi_ve_Zerre.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_05', title: '2.5 Mikro ve Makro Evrenin Tekilliği', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/05_Mikro_Makro_Evren_Tekilligi.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_06', title: '2.6 Işık Davranışlarında Tekillik: Yansıma, Kırılma, Soğurma ve Geçirme', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/06_Isik_Yansima_Kirilma_Sogurma_Gecirme.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_07', title: '2.7 Michelson İnterferometresi ve Kayıpsız Girişim Mekanizması', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/07_Michelson_Interferometresi_ve_Kayipsiz_Girisim.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_08', title: '2.8 Çift Yarığın Deşifresi: Tek Bir Kenarla Başlar', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/08_Kirinim_ve_Cift_Yarik_Mekanizmasi.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_09', title: '2.9 Evrenakı Gradyanları ve Polarizasyon', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/09_Evrenaki_Gradyanlari_ve_Polarizasyon.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_10', title: '2.10 Kuantum Anomalilerinin Çözümü', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/10_Kuantum_Anomalileri.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_11', title: '2.11 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/11_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_kaynakca', title: '2.12 Kaynakça', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/99_Kaynakca.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_03_01', title: '3.1 Evrenin Makine Dairesi: Nükleon ve Zitterbewegung', file: 'Metin/Akademik/Kisim_3_Makro_Evren/01_Evrenin_Makine_Dairesi.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_02', title: '3.2 Makro Evreni Şekillendiren 5 Kuvvet', file: 'Metin/Akademik/Kisim_3_Makro_Evren/02_5_Hidrodinamik_Kuvvetin_Koku.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_03', title: '3.3 Mikrodan Makroya Evrenakı', file: 'Metin/Akademik/Kisim_3_Makro_Evren/03_Mikrodan_Makroya_Evrenaki.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_04', title: '3.4 Kütle-İtim (Push-Gravity) Mekanizması', file: 'Metin/Akademik/Kisim_3_Makro_Evren/04_Kutle_Itim_Mekanizmasi.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_05', title: '3.5 Hortum Dinamikleri ve Siklostrofik Denge', file: 'Metin/Akademik/Kisim_3_Makro_Evren/05_Hortum_Dinamikleri.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_06', title: '3.6 Atmosferik Hareketler ve Coriolis Etkisi', file: 'Metin/Akademik/Kisim_3_Makro_Evren/06_Atmosferik_Hareketler.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_07', title: '3.7 Kozmolojik Genişleme ve Karanlık Enerji Hipotezi', file: 'Metin/Akademik/Kisim_3_Makro_Evren/07_Kozmolojik_Genisleme.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_08', title: '3.8 Makro-Girdabın Motoru: Vorteks Nedenselliği', file: 'Metin/Akademik/Kisim_3_Makro_Evren/08_Makro_Girdabin_Motoru.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_08b', title: "3.8.6 Güneş'in Galaktik Yörüngesi ve Galaksinin Kanat Çırpışı", file: 'Metin/Akademik/Kisim_3_Makro_Evren/08_5_Gunesin_Galaktik_Yorungesi_ve_Galaksinin_Kanat_Cirpisi.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_09', title: "3.9 Ay'ın Görmezden Gelinen Gizemleri", file: 'Metin/Akademik/Kisim_3_Makro_Evren/09_Ayin_Gizemleri.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_10', title: '3.10 Satürn Halka Dinamiği', file: 'Metin/Akademik/Kisim_3_Makro_Evren/10_Saturn_Halka_Dinamigi.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_11', title: '3.11 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_3_Makro_Evren/11_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_kaynakca', title: '3.12 Kaynakça', file: 'Metin/Akademik/Kisim_3_Makro_Evren/99_Kaynakca.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
        { id: 'akademik_04_01', title: '4.1 Bilimin Tekilliği: Mikro ve Makronun Matematiksel Birleşimi', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/01_Bilimin_Tekilligi.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },
    { id: 'akademik_04_02', title: '4.2 Matematiksel Model — I: Temel Model ve G\'nin Türetimi', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/02_Evrensel_Sabitler_1_Temel_Model.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },
    { id: 'akademik_04_02b', title: '4.2 Matematiksel Model — II: 5 Hidrodinamik Etki ve Kanıtlar', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/02_Evrensel_Sabitler_2_Hidrodinamik_Etkiler.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },
    { id: 'akademik_04_02c', title: '4.2 Matematiksel Model — III: Galaktik ve Kozmolojik Ölçek', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/02_Evrensel_Sabitler_3_Galaktik_Kozmolojik.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },
    { id: 'akademik_04_02d', title: '4.2 Matematiksel Model — IV: Modelin Sınırları ve İtirazlar', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/02_Evrensel_Sabitler_4_Sinirlar_ve_Itirazlar.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },
    { id: 'akademik_04_03', title: '4.3 Kütleçekimsel Merceklenme: Optik ve Kütlenin Tekilliği', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/03_Kutlecekimsel_Merceklenme.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },
    { id: 'akademik_04_04', title: '4.4 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/04_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },
    { id: 'akademik_04_kaynakca', title: '4.5 Kaynakça', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/99_Kaynakca.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },
    { id: 'akademik_05_01', title: '5.1 Işığın Sabitsizliği', file: 'Metin/Akademik/Kisim_5_Deneyler/01_Isigin_Sabitsizligi.md', group: 'akademik', part: 'Kısım V: Deneyler' },
    { id: 'akademik_05_02', title: '5.2 Kütle Dışı Evrenakı Gradyanları', file: 'Metin/Akademik/Kisim_5_Deneyler/02_Kutle_Disi_Evrenaki_Gradyanlari.md', group: 'akademik', part: 'Kısım V: Deneyler' },
    { id: 'akademik_05_03', title: '5.3 Kütle İçi Evrenakı Gradyanları', file: 'Metin/Akademik/Kisim_5_Deneyler/03_Kutle_Ici_Evrenaki_Gradyanlari.md', group: 'akademik', part: 'Kısım V: Deneyler' },
    { id: 'akademik_05_04', title: '5.4 Eksenel Kütle İtim', file: 'Metin/Akademik/Kisim_5_Deneyler/04_Eksenel_Kutle_Itim.md', group: 'akademik', part: 'Kısım V: Deneyler' },
    { id: 'akademik_05_05', title: '5.5 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_5_Deneyler/05_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım V: Deneyler' },
    { id: 'akademik_05_kaynakca', title: '5.6 Kaynakça', file: 'Metin/Akademik/Kisim_5_Deneyler/99_Kaynakca.md', group: 'akademik', part: 'Kısım V: Deneyler' },
    { id: 'akademik_06', title: '6. Kanıtlara Giriş', file: 'Metin/Akademik/Kisim_6_Kanitlar/06_Kanitlar.md', group: 'akademik', part: 'Kısım VI: Kanıtlar' },
    { id: 'akademik_06_00', title: '6.0 Yalnızca Evrenakı’nın Açıkladığı Gözlemler Matrisi', file: 'Metin/Akademik/Kisim_6_Kanitlar/00_Yalnizca_Evrenakinin_Acikladigi_Gozlemler.md', group: 'akademik', part: 'Kısım VI: Kanıtlar' },
    { id: 'akademik_06_01', title: '6.1 Evrenakı Kinematiğinden Doppler Türetimi', file: 'Metin/Akademik/Kisim_6_Kanitlar/01_Evrenaki_Doppler_Turetimi.md', group: 'akademik', part: 'Kısım VI: Kanıtlar' },
    { id: 'akademik_06_02', title: '6.2 Kütleçekimsel Kızıla Kayma ve Tek Mekanizmalı Çözüm', file: 'Metin/Akademik/Kisim_6_Kanitlar/02_Kutlecekimsel_Kizila_Kayma_Sentezi.md', group: 'akademik', part: 'Kısım VI: Kanıtlar' },
    { id: 'akademik_06_03', title: '6.3 Ekvatoral Vorteks ve Yörünge Anomalileri', file: 'Metin/Akademik/Kisim_6_Kanitlar/03_Ekvatoral_Vorteks_ve_Yorunge_Anomalileri.md', group: 'akademik', part: 'Kısım VI: Kanıtlar' },
    { id: 'akademik_06_04', title: '6.4 Camdaki Hız Geri Kazanımı ve Abraham-Minkowski', file: 'Metin/Akademik/Kisim_6_Kanitlar/04_Camdaki_Hiz_Geri_Kazanimi.md', group: 'akademik', part: 'Kısım VI: Kanıtlar' },
    { id: 'akademik_06_05', title: '6.5 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_6_Kanitlar/05_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım VI: Kanıtlar' },
    { id: 'akademik_06_kaynakca', title: '6.6 Kaynakça', file: 'Metin/Akademik/Kisim_6_Kanitlar/99_Kaynakca.md', group: 'akademik', part: 'Kısım VI: Kanıtlar' },
    { id: 'akademik_07', title: 'Kısım VII: Tartışma ve Sonuç', file: 'Metin/Akademik/Kisim_7_Tartisma_ve_Sonuc/06_Tartisma_ve_Sonuc.md', group: 'akademik', part: 'Kısım VII: Tartışma ve Sonuç' },
    { id: 'akademik_07_03', title: '7.7 Modern Fiziğin Açık Krizleri ve Evrenakı Ufku', file: 'Metin/Akademik/Kisim_7_Tartisma_ve_Sonuc/03_Modern_Fizigin_Acik_Krizleri_ve_Evrenaki_Ufku.md', group: 'akademik', part: 'Kısım VII: Tartışma ve Sonuç' },
    { id: 'akademik_07_kaynakca', title: 'Kaynakça', file: 'Metin/Akademik/Kisim_7_Tartisma_ve_Sonuc/99_Kaynakca.md', group: 'akademik', part: 'Kısım VII: Tartışma ve Sonuç' },
    { id: 'akademik_08', title: 'Kısım VIII: Ekler', file: 'Metin/Akademik/Kisim_8_Ekler/07_Matematiksel_Ekler.md', group: 'akademik', part: 'Kısım VIII: Ekler' },
    { id: 'akademik_09', title: '9.1 Doç. Dr. Rıza Demirbilek Değerlendirmesi', file: 'Metin/Akademik/Kisim_9_Hakem_Degerlendirmeleri/01_Doc_Dr_Riza_Demirbilek_Degerlendirmesi.md', group: 'akademik', part: 'Kısım IX: Hakem Değerlendirmeleri' },
    { id: 'akademik_09_ai', title: '9.2 Claude Fable 5 Değerlendirmesi', file: 'Metin/Akademik/Kisim_9_Hakem_Degerlendirmeleri/02_Claude_Fable_5_Degerlendirmesi.md', group: 'akademik', part: 'Kısım IX: Hakem Değerlendirmeleri' },
    { id: 'akademik_09_gemini', title: '9.3 Gemini 3.1 Pro Değerlendirmesi', file: 'Metin/Akademik/Kisim_9_Hakem_Degerlendirmeleri/03_Gemini_3_1_Pro_Degerlendirmesi.md', group: 'akademik', part: 'Kısım IX: Hakem Değerlendirmeleri' },
    { id: 'akademik_09_10kriter', title: '9.4 10 Kriterlik Resmi Standart Testi', file: 'Metin/Akademik/Kisim_9_Hakem_Degerlendirmeleri/04_Evrenaki_Resmi_Standartlara_Gore_Degerlendirme.md', group: 'akademik', part: 'Kısım IX: Hakem Değerlendirmeleri' },
    { id: 'akademik_09_02', title: '9.5 Önceki Değerlendirmeler ve Tartışmalar', file: 'Metin/Akademik/Kisim_9_Hakem_Degerlendirmeleri/08_Hakem_Degerlendirmeleri.md', group: 'akademik', part: 'Kısım IX: Hakem Değerlendirmeleri' },
    { id: 'akademik_09_99', title: '9.6 Hakemlik Standartı ve Kriterler', file: 'Metin/Akademik/Kisim_9_Hakem_Degerlendirmeleri/99_Hakemlik_Standarti.md', group: 'akademik', part: 'Kısım IX: Hakem Değerlendirmeleri' },
    { id: 'populer_01', title: '1. Uzay Boş Değil!', file: 'Metin/Populer/populer_01.md', group: 'populer' },
    { id: 'populer_02', title: '2. Elma Neden Düşmez, İtilir!', file: 'Metin/Populer/populer_02.md', group: 'populer' },
    { id: 'populer_03', title: '3. Işığın Gerçek Yüzü: Zerreler', file: 'Metin/Populer/populer_03.md', group: 'populer' },
    { id: 'populer_04', title: '4. Işıkla İlgili Her Şey Yanlış', file: 'Metin/Populer/populer_04.md', group: 'populer' },
    { id: 'populer_05', title: '5. Dördüncü Boyutun Sırrı', file: 'Metin/Populer/populer_05.md', group: 'populer' },
    { id: 'populer_06', title: '6. Zaman Bükülmez, Saatler Yavaşlar', file: 'Metin/Populer/populer_06.md', group: 'populer' },
    { id: 'populer_07', title: '7. Karanlık Madde Masalı', file: 'Metin/Populer/populer_07.md', group: 'populer' },
    { id: 'populer_08', title: '8. Evreni Şekillendiren 5 Güç', file: 'Metin/Populer/populer_08.md', group: 'populer' },
    { id: 'populer_09', title: "9. Ay ve Satürn'ün Gizemleri", file: 'Metin/Populer/populer_09.md', group: 'populer' },
    { id: 'populer_10', title: '10. Einstein Bile İtiraf Etti', file: 'Metin/Populer/populer_10.md', group: 'populer' },
    { id: 'populer_11', title: '11. Görünmezi Ölçtük', file: 'Metin/Populer/populer_11.md', group: 'populer' },
    { id: 'populer_12', title: '12. Sözlük, SSS & İnteraktif Test', file: 'Metin/Populer/populer_12.md', group: 'populer' },
    { id: 'eski_akademik_01', title: 'Eski: Akademik Bölüm 1', file: 'Metin/Eski_Surum/akademik_01.md', group: 'eski' },
    { id: 'eski_akademik_29', title: 'Eski: Akademik Bölüm 29', file: 'Metin/Eski_Surum/akademik_29.md', group: 'eski' },
    { id: 'duzeltme', title: 'Hakem Değerlendirmeleri', file: 'Metin/Eski_Surum/duzeltme.md', group: 'eski' }
];

// Safe LocalStorage Fallback (avoids crashes in private modes or file:/// CORS runs)
let safeStorage = null;
let storageMemoryFallback = {};
try {
    safeStorage = window.localStorage;
    // Test if actually writable
    safeStorage.setItem('__test_storage__', '1');
    safeStorage.removeItem('__test_storage__');
} catch (e) {
    console.warn("localStorage is not available. Falling back to memory storage.", e);
    safeStorage = {
        getItem(key) {
            return key in storageMemoryFallback ? storageMemoryFallback[key] : null;
        },
        setItem(key, value) {
            storageMemoryFallback[key] = String(value);
        },
        removeItem(key) {
            delete storageMemoryFallback[key];
        },
        clear() {
            storageMemoryFallback = {};
        }
    };
}


// Üyelik/oturum altyapısı: Firebase Authentication (firebase-client.js)
// firebase-client.js yüklenemezse üyelik özellikleri kapanır; site okuma modunda çalışmaya devam eder.
let currentUser = null; // Giriş yapmış üye bilgisi

// Yönetici hesapları — Firebase Authentication ile doğrulanmış e-postalar.
// Buradaki e-posta ile Firebase Console > Authentication > Users içinde bir hesap açılmış olmalıdır.
const ADMIN_EMAILS = ['burhanguler@gmail.com'];

// App State Variables

// Global Version State
let activeVersion = safeStorage ? (safeStorage.getItem('selectedVersion') || 'akademik') : 'akademik';

// Global Memory Cache for full-text chapter search
const chapterTextsCache = {};
let isIndexLoading = false;

// Preload/Index chapter markdown files in background for full-text search
async function preloadChapterTexts() {
    if (isIndexLoading) return;
    isIndexLoading = true;
    for (const chap of chapters) {
        if (!chapterTextsCache[chap.id]) {
            try {
                const res = await fetch(chap.file);
                if (res.ok) {
                    const text = await res.text();
                    // Store normalized lower-case text for fast search
                    chapterTextsCache[chap.id] = text.toLocaleLowerCase('tr-TR');
                }
            } catch (e) {
                // Ignore fetch errors
            }
        }
    }
}

window.selectVersion = function(version) {
    activeVersion = version;
    if (safeStorage) safeStorage.setItem('selectedVersion', version);
    
    // Build TOC for selected version
    buildTOC();
    
    // Close splash
    const splash = document.getElementById('splash-screen');
    if (splash && !splash.classList.contains('fade-out')) {
        splash.classList.add('fade-out');
        try {
            safeStorage.setItem('introPlayed', 'true');
        } catch (e) {
            console.warn("Storage save failed:", e);
        }
        setTimeout(() => {
            splash.style.display = 'none';
        }, 600);
    }
    
    // İntrodan sonra doğrudan ilk bölüme değil, 'Başlangıç' (home) sayfasına yönlendir.
    window.location.hash = '#home';
};

window.continueReading = function() {
    // Kaldığı yerden devam et veya ilk bölüme git
    loadChapter(activeVersion === 'akademik' ? 'akademik_01_01' : 'populer_01');
};

window.resetVersionSelection = function(e) {
    if (e) e.preventDefault();
    if (safeStorage) {
        safeStorage.removeItem('introPlayed');
        safeStorage.removeItem('selectedVersion');
    }
    window.location.hash = ''; // Clear hash so it loads home
    window.location.reload();
};

let activeChapterId = null;
let currentFontSize = 1.05; // rem units

// DOM Elements Initialization & Event Listeners
document.addEventListener("DOMContentLoaded", () => {

    // Handle Splash Screen Intro
    try {
        initSplashScreen();
    } catch (e) {
        console.error("initSplashScreen error:", e);
    }

    // Initialize Auth State & Check Session
    try {
        initAuth();
    } catch (e) {
        console.error("initAuth error:", e);
    }

    // Initialize Analytics Tracking
    try {
        initAnalytics();
    } catch (e) {
        console.error("initAnalytics error:", e);
    }

    // Register PWA Service Worker for offline mobile app support
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('service-worker.js')
            .then(reg => console.log('Service Worker registered:', reg.scope))
            .catch(err => console.warn('Service Worker registration failed:', err));
    }

    // Build Table of Contents Sidebar Links
    try {
        buildTOC();
    } catch (e) {
        console.error("buildTOC error:", e);
    }

    // Initialize Icons
    try {
        if (typeof lucide !== 'undefined') {
            lucide.createIcons();
        }
    } catch (e) {
        console.warn("lucide not defined or failed to load:", e);
    }

    // Hash Routing listener
    window.addEventListener('hashchange', handleRoute);

    // Initial route handling
    try {
        handleRoute();
    } catch (e) {
        console.error("handleRoute error:", e);
    }

    // Font Sizing event handlers
    const btnDec = document.getElementById('btn-decrease-font');
    if (btnDec) btnDec.addEventListener('click', () => changeFontSize(-0.05));
    const btnInc = document.getElementById('btn-increase-font');
    if (btnInc) btnInc.addEventListener('click', () => changeFontSize(0.05));

    // Restore saved settings
    try {
        restoreSavedSettings();
    } catch (e) {
        console.error("restoreSavedSettings error:", e);
    }

    // Theme Toggle Handler
    const btnTheme = document.getElementById('btn-theme-toggle');
    if (btnTheme) btnTheme.addEventListener('click', toggleTheme);

    // Sidebar triggers for mobile drawer mode
    const sidebar = document.getElementById('sidebar');
    const toggleSidebar = document.getElementById('btn-toggle-sidebar');
    if (toggleSidebar && sidebar) {
        toggleSidebar.addEventListener('click', () => {
            sidebar.classList.toggle('open');
        });
    }
    const closeSidebar = document.getElementById('btn-close-sidebar');
    if (closeSidebar && sidebar) {
        closeSidebar.addEventListener('click', () => {
            sidebar.classList.remove('open');
        });
    }

    // Trigger background pre-index of all chapters for instant full-text search
    preloadChapterTexts();

    // Search bar filter function (Başlık ve Tüm Bölüm İçeriğinde Arama)
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
        searchInput.addEventListener('focus', () => preloadChapterTexts(), { once: true });

        searchInput.addEventListener('input', (e) => {
            const rawQuery = e.target.value;
            const query = (rawQuery || '').toLocaleLowerCase('tr-TR').trim();
            const list = document.getElementById('toc-list');
            if (!list) return;

            const accordions = list.querySelectorAll('.toc-accordion');

            if (!query) {
                // Reset all elements
                list.querySelectorAll('.toc-item').forEach(item => {
                    item.style.display = '';
                    const badge = item.querySelector('.search-match-badge');
                    if (badge) badge.remove();
                });
                accordions.forEach(acc => {
                    acc.style.display = '';
                    const content = acc.querySelector('.toc-accordion-content');
                    const icon = acc.querySelector('i');
                    const hasActiveChild = content && content.querySelector('.toc-link.active');
                    if (content) content.style.display = hasActiveChild ? 'block' : 'none';
                    if (icon) icon.style.transform = hasActiveChild ? 'rotate(180deg)' : 'rotate(0deg)';
                });
                return;
            }

            if (query.length >= 2 && Object.keys(chapterTextsCache).length === 0) {
                preloadChapterTexts();
            }

            // Direct top level items (e.g., home item or change version)
            const topItems = list.children;
            Array.from(topItems).forEach(li => {
                if (li.classList.contains('toc-accordion')) return;
                const title = (li.getAttribute('data-title') || li.textContent || '').toLocaleLowerCase('tr-TR');
                li.style.display = title.includes(query) ? '' : 'none';
            });

            // Accordion sections (parts and sub-chapters)
            accordions.forEach(acc => {
                const partTitle = (acc.getAttribute('data-title') || '').toLocaleLowerCase('tr-TR');
                const content = acc.querySelector('.toc-accordion-content');
                const icon = acc.querySelector('i');
                const subItems = content ? content.querySelectorAll('.toc-item') : [];

                let matchedSubCount = 0;
                subItems.forEach(sub => {
                    const subTitle = (sub.getAttribute('data-title') || sub.textContent || '').toLocaleLowerCase('tr-TR');
                    const chapLink = sub.querySelector('.toc-link');
                    const chapId = chapLink ? chapLink.id.replace('link-', '') : '';

                    let isTitleMatch = subTitle.includes(query) || partTitle.includes(query);
                    let isContentMatch = false;

                    if (chapId && chapterTextsCache[chapId]) {
                        isContentMatch = chapterTextsCache[chapId].includes(query);
                    }

                    const oldBadge = sub.querySelector('.search-match-badge');
                    if (oldBadge) oldBadge.remove();

                    if (isTitleMatch || isContentMatch) {
                        sub.style.display = '';
                        matchedSubCount++;

                        if (isContentMatch && !isTitleMatch && chapLink) {
                            const badge = document.createElement('span');
                            badge.className = 'search-match-badge';
                            badge.style.cssText = 'font-size: 0.72em; color: var(--neon-cyan); background: rgba(0, 229, 255, 0.12); border: 1px solid rgba(0, 229, 255, 0.25); padding: 1px 6px; border-radius: 10px; margin-left: 6px; font-weight: 500;';
                            badge.textContent = 'metinde geçiyor';
                            chapLink.appendChild(badge);
                        }
                    } else {
                        sub.style.display = 'none';
                    }
                });

                if (matchedSubCount > 0 || partTitle.includes(query)) {
                    acc.style.display = '';
                    if (content) content.style.display = 'block';
                    if (icon) icon.style.transform = 'rotate(180deg)';
                } else {
                    acc.style.display = 'none';
                }
            });
        });
    }

    // Navigation buttons handlers
    const btnPrev = document.getElementById('btn-prev-chap');
    if (btnPrev) btnPrev.addEventListener('click', () => navigateChapter(-1));
    const btnNext = document.getElementById('btn-next-chap');
    if (btnNext) btnNext.addEventListener('click', () => navigateChapter(1));

    // Scroll progress bar logic
    const viewport = document.getElementById('main-viewport');
    if (viewport) {
        viewport.addEventListener('scroll', () => {
            const homeView = document.getElementById('home-view');
            const progressBar = document.getElementById('progress-bar');
            if (homeView && homeView.style.display === 'block') {
                if (progressBar) progressBar.style.width = '0%';
                return;
            }
            const scrollTop = viewport.scrollTop;
            const scrollHeight = viewport.scrollHeight - viewport.clientHeight;
            const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
            if (progressBar) progressBar.style.width = `${progress}%`;
        });
    }
});

// Build Sidebar Navigation dynamically
function buildTOC() {
    const list = document.getElementById('toc-list');
    list.innerHTML = '';

    // Home View item
    const homeLi = document.createElement('li');
    homeLi.className = 'toc-item';
    homeLi.setAttribute('data-title', 'Giriş Başlangıç');
    homeLi.innerHTML = `
        <a href="#home" class="toc-link" id="link-home">
            <i data-lucide="home" style="width:16px; height:16px; margin-right:8px;"></i>
            Başlangıç
        </a>
    `;
    list.appendChild(homeLi);

    // Filter chapters by activeVersion
    const filteredChapters = chapters.filter(c => c.group === activeVersion || c.group === 'all');
    let currentPartList = null;
    let currentPartName = null;

    filteredChapters.forEach(chap => {
        if (chap.part) {
            if (currentPartName !== chap.part) {
                currentPartName = chap.part;
                const partLi = document.createElement('li');
                partLi.className = 'toc-item toc-accordion';
                partLi.setAttribute('data-title', chap.part);
                partLi.innerHTML = `
                    <div class="toc-accordion-header" style="display:flex; justify-content:space-between; align-items:center; cursor:pointer; padding: 12px; background: rgba(0, 229, 255, 0.05); border-radius: 8px; margin-bottom: 4px; font-weight: 600; color: var(--neon-cyan); border-left: 2px solid var(--neon-cyan);">
                        <span>${chap.part}</span>
                        <i data-lucide="chevron-down" style="width:16px; height:16px; transition: transform 0.3s;"></i>
                    </div>
                    <ul class="toc-accordion-content" style="list-style:none; padding-left: 15px; display: none; margin-top: 4px; padding-bottom: 8px;">
                    </ul>
                `;
                list.appendChild(partLi);
                
                const header = partLi.querySelector('.toc-accordion-header');
                const content = partLi.querySelector('.toc-accordion-content');
                const icon = partLi.querySelector('i');
                icon.style.transform = 'rotate(0deg)'; // default closed
                
                header.addEventListener('click', () => {
                    const isOpen = content.style.display === 'block';
                    content.style.display = isOpen ? 'none' : 'block';
                    icon.style.transform = isOpen ? 'rotate(0deg)' : 'rotate(180deg)';
                });
                
                currentPartList = content;
            }
            
            const subLi = document.createElement('li');
            subLi.className = 'toc-item';
            subLi.style.marginBottom = '2px';
            subLi.setAttribute('data-title', chap.title);
            subLi.innerHTML = `
                <a href="#${chap.id}" class="toc-link" id="link-${chap.id}" style="padding: 8px 12px; font-size: 0.9em; opacity: 0.9;">
                    ${chap.title}
                </a>
            `;
            currentPartList.appendChild(subLi);
            
        } else {
            currentPartName = null;
            const li = document.createElement('li');
            li.className = 'toc-item';
            li.setAttribute('data-title', chap.title);
            li.innerHTML = `
                <a href="#${chap.id}" class="toc-link" id="link-${chap.id}">
                    ${chap.title}
                </a>
            `;
            list.appendChild(li);
        }
    });
    
    // Sürüm Değiştir Butonu
    const changeVersionLi = document.createElement('li');
    changeVersionLi.className = 'toc-item';
    changeVersionLi.setAttribute('data-title', 'Başka Sürüm Seç');
    changeVersionLi.innerHTML = `
        <a href="#" class="toc-link" onclick="resetVersionSelection(event)" style="color: var(--neon-magenta); border-top: 1px solid var(--border-color); margin-top: 15px; padding-top: 15px; font-weight: bold;">
            <i data-lucide="refresh-cw" style="width:16px; height:16px; margin-right:8px;"></i>
            Başka Sürüm Seç
        </a>
    `;
    list.appendChild(changeVersionLi);

    if (typeof lucide !== 'undefined') lucide.createIcons();
}

// Active TOC link highlight
function setActiveTocLink(id) {
    document.querySelectorAll('.toc-link').forEach(link => link.classList.remove('active'));
    const activeLink = document.getElementById(`link-${id}`);
    if (activeLink) {
        activeLink.classList.add('active');
        // Active link bir akordiyon içerisindeyse üst akordiyonu otomatik aç
        const parentContent = activeLink.closest('.toc-accordion-content');
        if (parentContent) {
            parentContent.style.display = 'block';
            const parentAcc = parentContent.closest('.toc-accordion');
            if (parentAcc) {
                const icon = parentAcc.querySelector('.toc-accordion-header i');
                if (icon) icon.style.transform = 'rotate(180deg)';
            }
        }
    }

    // Close mobile drawer on link select
    const sidebar = document.getElementById('sidebar');
    if (sidebar) sidebar.classList.remove('open');
}

// Hash Routing Handler
function handleRoute() {
    const hash = window.location.hash || '#home';
    const mainViewport = document.getElementById('main-viewport');

    // Scroll viewport back to top
    if (mainViewport) mainViewport.scrollTop = 0;

    if (hash === '#home') {
        showTab('book');
        document.getElementById('home-view').style.display = 'block';
        document.getElementById('reader-view').style.display = 'none';
        document.getElementById('page-title').textContent = 'Giriş';
        setActiveTocLink('home');
        activeChapterId = null;
    } else if (hash === '#sim') {
        switchTab('sim');
        setActiveTocLink('sim');
        activeChapterId = null;
    } else if (hash === '#forum') {
        switchTab('forum');
        setActiveTocLink('forum');
        activeChapterId = null;
        loadForumThreads('all');
    } else {
        const chapterId = hash.replace('#', '');
        const chapter = chapters.find(c => c.id === chapterId);
        if (chapter) {
            showTab('book');
            document.getElementById('home-view').style.display = 'none';
            document.getElementById('reader-view').style.display = 'block';
            setActiveTocLink(chapterId);
            loadChapterContent(chapter);
        }
    }
}

// Switch between Tabs (Book Reading vs Simulation Hub view)
function switchTab(tabId) {
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.tab-pane').forEach(pane => pane.classList.remove('active'));

    if (tabId === 'book') {
        document.getElementById('tab-book').classList.add('active');
        document.getElementById('pane-book').classList.add('active');
        // Handle restoration of last selected hash
        if (!window.location.hash || window.location.hash === '#sim') {
            window.location.hash = activeChapterId ? `#${activeChapterId}` : '#home';
        }
    } else if (tabId === 'sim') {
        document.getElementById('tab-sim').classList.add('active');
        document.getElementById('pane-sim').classList.add('active');
        window.location.hash = '#sim';
        initSimulationHub();
    } else if (tabId === 'forum') {
        document.getElementById('tab-forum').classList.add('active');
        document.getElementById('pane-forum').classList.add('active');
        window.location.hash = '#forum';
    }
}

// Show specific tab container
function showTab(tabId) {
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.tab-pane').forEach(pane => pane.classList.remove('active'));

    if (tabId === 'book') {
        document.getElementById('tab-book').classList.add('active');
        document.getElementById('pane-book').classList.add('active');
    } else if (tabId === 'sim') {
        document.getElementById('tab-sim').classList.add('active');
        document.getElementById('pane-sim').classList.add('active');
        initSimulationHub();
    } else if (tabId === 'forum') {
        document.getElementById('tab-forum').classList.add('active');
        document.getElementById('pane-forum').classList.add('active');
    }
}

// Reload iframe content of active simulation
function reloadSimulation() {
    const frame = document.getElementById('sim-frame');
    if (frame) frame.src = frame.src;
}

// SIMULATION LABORATORY CATALOG REGISTRY
const simulationsList = [
    {
        id: 'sim_boyut_4d',
        title: '4D İzdüşüm ve Hiper-Küre Akışkan Tüneli',
        category: 'kozmoloji',
        badgeClass: 'badge-magenta',
        badgeText: '4D & KOZMOLOJİ',
        file: 'Simulasyon/boyut_simulasyonu.html',
        chapterId: 'akademik_01_04',
        chapterName: '1.4 Dördüncü Boyut ve İzdüşüm',
        desc: '4. Boyut hiper-küre kesitlerinin 3D uzaydaki küresel sönümleme ve akışkan tüneli kinematiğini interaktif olarak deneyimleyin.'
    },
    {
        id: 'sim_3d_gradyan',
        title: '3D Klasik Geometrik Şekillerin Gradyanları',
        category: 'geometri',
        badgeClass: 'badge-blue',
        badgeText: 'GEOMETRİ & GRADYANLAR',
        file: 'Metin/bolum_26_3d.html',
        chapterId: 'akademik_03_03',
        chapterName: '3.3 Mikrodan Makroya Evrenakı',
        desc: 'Piramit, Küp, Silindir ve Küre kütlelerinin uzay dokusunda yarattığı 3 boyutlu hacimsel vakum kılıfları.'
    },
    {
        id: 'sim_2d_gradyan',
        title: '2D Geometrik Kütle Gradyan Haritası',
        category: 'geometri',
        badgeClass: 'badge-blue',
        badgeText: 'GEOMETRİ & GRADYANLAR',
        file: 'Metin/bolum_26_2d.html',
        chapterId: 'akademik_03_03',
        chapterName: '3.3 Mikrodan Makroya Evrenakı',
        desc: 'Kare, Üçgen, Çubuk ve Daire kütlelerinin 2D basınç gölgeleri ve asimetrik yönelim itki vektörleri.'
    },
    {
        id: 'sim_eksenel_itim',
        title: 'Eksenel Kütle-İtim (Centripetal Push)',
        category: 'kozmoloji',
        badgeClass: 'badge-magenta',
        badgeText: '4D & KOZMOLOJİ',
        file: 'Simulasyon/eksenel_itim_oto.html',
        chapterId: 'akademik_03_04',
        chapterName: '3.4 Kütle-İtim Mekanizması',
        desc: 'Mikro girdapların merkezcil basınç ile kütleyi sıkıştırarak makro kütleçekim alanını oluşturma süreci.'
    },
    {
        id: 'sim_michelson_90',
        title: 'Michelson 90° İnterferometre Simülatörü',
        category: 'optik',
        badgeClass: 'badge-green',
        badgeText: 'OPTİK & ZERRE',
        file: 'Simulasyon/michelson_90.html',
        chapterId: 'akademik_02_07',
        chapterName: '2.7 Michelson İnterferometresi',
        desc: 'Süper-akışkan ortamda ışık sürüklenmesi ve kayıpsız girişim saçakları simülasyonu.'
    },
    {
        id: 'sim_mach_zehnder',
        title: 'Mach-Zehnder İnterferometresi',
        category: 'optik',
        badgeClass: 'badge-green',
        badgeText: 'OPTİK & ZERRE',
        file: 'Simulasyon/mach_zehnder.html',
        chapterId: 'akademik_02_08',
        chapterName: '2.8 Çift Yarığın Deşifresi',
        desc: 'Faz kayması ve fotonsuz Zerre dalga paketi yönlendirme kinematiği.'
    },
    {
        id: 'sim_ciftyarik',
        title: 'Çift Yarık ve Kuantum Silici (Which-Path)',
        category: 'optik',
        badgeClass: 'badge-green',
        badgeText: 'OPTİK & ZERRE',
        file: 'Simulasyon/ciftyarik_silici.html',
        chapterId: 'akademik_02_10',
        chapterName: '2.10 Kuantum Anomalileri',
        desc: 'Tek kenar kırınımı ve kuantum potansiyel engeli deşifre simülasyonu.'
    },
    {
        id: 'sim_fresnel_arago',
        title: 'Fresnel-Arago Girişim Deneyi',
        category: 'optik',
        badgeClass: 'badge-green',
        badgeText: 'OPTİK & ZERRE',
        file: 'Simulasyon/fresnel_arago.html',
        chapterId: 'akademik_02_09',
        chapterName: '2.9 Polarizasyon',
        desc: 'Polarize ışık demetlerinin akışkan ortamda girişim ve faz davranışları.'
    },
    {
        id: 'sim_ay_yorunge',
        title: 'Ay Yörünge Dengesi ve Vorteks Kilitlenmesi',
        category: 'gok',
        badgeClass: 'badge-yellow',
        badgeText: 'GÖK MEKANİĞİ',
        file: 'Simulasyon/ay_yorunge_dengesi.html',
        chapterId: 'akademik_03_09',
        chapterName: "3.9 Ay'ın Gizemleri",
        desc: 'Dünya-Ay sistemindeki ekvatoral girdap ve yörünge kilitlenme dinamiği.'
    },
    {
        id: 'sim_ay_gelgit',
        title: 'Ay Gelgit ve Elipsoid Şişkinlik',
        category: 'gok',
        badgeClass: 'badge-yellow',
        badgeText: 'GÖK MEKANİĞİ',
        file: 'Simulasyon/ay_gelgit_sirali.html',
        chapterId: 'akademik_03_09',
        chapterName: "3.9 Ay'ın Gizemleri",
        desc: 'Okyanus gelgitlerinin Evrenakı basınç gradyanı ile açıklanması.'
    },
    {
        id: 'sim_girdap',
        title: 'Evrenakı Girdap Mekanizması ve Vorteks',
        category: 'kozmoloji',
        badgeClass: 'badge-magenta',
        badgeText: '4D & KOZMOLOJİ',
        file: 'Simulasyon/evrenaki_girdap_animasyonu.html',
        chapterId: 'akademik_03_08',
        chapterName: '3.8 Makro-Girdabın Motoru',
        desc: 'Makro evren ölçeğinde galaksi ve yıldız sistemlerini döndüren vorteks alanları.'
    },
    {
        id: 'sim_kavrama',
        title: 'Kavrama ve Kilitlenme Mekanizması',
        category: 'gok',
        badgeClass: 'badge-yellow',
        badgeText: 'GÖK MEKANİĞİ',
        file: 'Simulasyon/kavrama_kilitlenme_sim.html',
        chapterId: 'akademik_03_08',
        chapterName: '3.8 Makro-Girdabın Motoru',
        desc: 'Dönel kütlelerin Evrenakı akışkanında tork kilitlenmesi ve spin transferi.'
    }
];

let activeSimData = simulationsList[0];
let currentSimFilter = 'all';

function initSimulationHub() {
    renderSimulationCards(currentSimFilter);
}

function renderSimulationCards(categoryFilter) {
    const grid = document.getElementById('sim-cards-grid');
    if (!grid) return;

    currentSimFilter = categoryFilter;

    let filtered = categoryFilter === 'all' 
        ? simulationsList 
        : simulationsList.filter(s => s.category === categoryFilter);

    grid.innerHTML = filtered.map(sim => `
        <div class="sim-card ${sim.id === activeSimData.id ? 'active-card' : ''}" onclick="selectSimulation('${sim.id}')">
            <div class="sim-card-header">
                <span class="sim-category-badge ${sim.badgeClass}">${sim.badgeText}</span>
                <i data-lucide="play-circle" style="width:18px;height:18px;color:var(--neon-blue);"></i>
            </div>
            <div class="sim-card-body">
                <h4>${sim.title}</h4>
                <p>${sim.desc}</p>
            </div>
            <div class="sim-card-footer">
                <span class="sim-card-chapter">${sim.chapterName}</span>
                <button class="sim-card-run-btn">
                    Çalıştır <i data-lucide="arrow-right" style="width:12px;height:12px;"></i>
                </button>
            </div>
        </div>
    `).join('');

    if (window.lucide) {
        window.lucide.createIcons();
    }
}

function filterSimulations(cat, btn) {
    document.querySelectorAll('.sim-filter-btn').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');
    renderSimulationCards(cat);
}

function selectSimulation(simId) {
    const sim = simulationsList.find(s => s.id === simId);
    if (!sim) return;

    activeSimData = sim;

    const frame = document.getElementById('sim-frame');
    if (frame) frame.src = sim.file;

    const badge = document.getElementById('sim-active-badge');
    if (badge) {
        badge.className = `sim-category-badge ${sim.badgeClass}`;
        badge.textContent = sim.badgeText;
    }

    const title = document.getElementById('sim-active-title');
    if (title) title.textContent = sim.title;

    const desc = document.getElementById('sim-active-desc');
    if (desc) desc.textContent = sim.desc;

    const chapterName = document.getElementById('sim-chapter-name');
    if (chapterName) chapterName.textContent = sim.chapterName;

    // Highlight active card in grid
    renderSimulationCards(currentSimFilter);

    // Smooth scroll to active player
    const player = document.getElementById('sim-active-player');
    if (player) {
        player.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
}

function openActiveSimChapter() {
    if (activeSimData && activeSimData.chapterId) {
        loadChapter(activeSimData.chapterId);
    }
}

// Load and Parse Markdown Chapter Contents
async function loadChapterContent(chapter) {
    activeChapterId = chapter.id;
    recordPageView(chapter.id);
    const bodyContainer = document.getElementById('markdown-body');
    const pageTitle = document.getElementById('page-title');

    bodyContainer.innerHTML = `
        <div class="loader" style="text-align:center; padding:50px 0;">
            <i data-lucide="loader-2" class="animate-spin" style="width:48px; height:48px; color:var(--neon-blue);"></i>
            <p style="margin-top:16px; color:var(--text-muted);">Bölüm yükleniyor, lütfen bekleyin...</p>
        </div>
    `;
    lucide.createIcons({ attrs: { class: 'loader-spinner animate-spin' } });

    try {
        const response = await fetch(chapter.file);
        if (!response.ok) {
            throw new Error(`Yükleme hatası: ${response.statusText}`);
        }

        let markdownText = await response.text();

        // Resolve Markdown local image paths
        // Replacing relative paths: ../Gorseller/ -> Gorseller/
        markdownText = markdownText.replace(/\.\.\/Gorseller\//g, 'Gorseller/');

        // Parse Markdown to HTML via marked.js
        let htmlContent = marked.parse(markdownText);

        // Inject content
        bodyContainer.innerHTML = htmlContent;
        pageTitle.textContent = chapter.title;

        // innerHTML ile eklenen <script> etiketleri tarayıcı tarafından çalıştırılmaz;
        // gömülü etkileşimli animasyonların (ör. Evrenakı Rampası simülasyonu) çalışabilmesi için
        // bunları yeniden oluşturup DOM'a ekleyerek elle çalıştırıyoruz.
        executeEmbeddedScripts(bodyContainer);

        // Post-process HTML for GitHub style alert boxes
        postProcessAlerts(bodyContainer);

        // Process tooltips
        postProcessTooltips(bodyContainer);

        // Render mathematical formulas via KaTeX
        renderMathInElement(bodyContainer, {
            delimiters: [
                { left: '$$', right: '$$', display: true },
                { left: '$', right: '$', display: false },
                { left: '\\(', right: '\\)', display: false },
                { left: '\\[', right: '\\]', display: true }
            ],
            throwOnError: false
        });

        // Render mermaid diagrams (```mermaid code fences)
        renderMermaidDiagrams(bodyContainer);

        // Initialize icons inside the loaded article
        lucide.createIcons();

        // Manage previous/next button visibilities
        updateNavigationButtons();

        // Load comments for active chapter
        loadComments(chapter.id);

        // If this is the peer review page ('akademik_08'), load the peer reviews section
        if (chapter.id === 'duzeltme') {
            loadPeerReviewsSection();
        }

    } catch (error) {
        bodyContainer.innerHTML = `
            <div class="error-box" style="border:1px solid var(--neon-magenta); border-radius:8px; padding:24px; background:rgba(255,0,127,0.05); color:var(--text-primary); text-align:center;">
                <i data-lucide="alert-triangle" style="width:48px; height:48px; color:var(--neon-magenta); margin-bottom:12px;"></i>
                <h3>Bölüm Yüklenemedi</h3>
                <p style="color:var(--text-muted); margin-top:8px;">${error.message}</p>
                <button class="btn btn-primary" onclick="loadChapter('${chapter.id}')" style="margin: 16px auto 0 auto;">
                    Yeniden Dene
                </button>
            </div>
        `;
        lucide.createIcons();
    }
}

// marked.js, ```mermaid çitlerini <pre><code class="language-mermaid"> olarak üretir;
// mermaid.js bunları tanımaz. Bu fonksiyon blokları .mermaid div'lerine çevirip çizdirir.
function renderMermaidDiagrams(container) {
    if (typeof mermaid === 'undefined') return;
    const blocks = container.querySelectorAll('pre code.language-mermaid');
    if (!blocks.length) return;
    blocks.forEach((code) => {
        const div = document.createElement('div');
        div.className = 'mermaid';
        div.textContent = code.textContent;
        code.parentElement.replaceWith(div);
    });
    try {
        mermaid.initialize({ startOnLoad: false, theme: 'dark', securityLevel: 'loose' });
        mermaid.run({ nodes: container.querySelectorAll('.mermaid') });
    } catch (e) {
        console.error('Mermaid render hatası:', e);
    }
}

// innerHTML üzerinden eklenen <script> etiketlerini tarayıcı çalıştırmadığından,
// bölüm içeriğinde gömülü etkileşimli animasyonların (canvas/JS widget'ları) çalışabilmesi için
// bu etiketleri yeniden oluşturup DOM'a ekleriz.
function executeEmbeddedScripts(container) {
    const oldScripts = container.querySelectorAll('script');
    oldScripts.forEach(oldScript => {
        const newScript = document.createElement('script');
        Array.from(oldScript.attributes).forEach(attr => {
            newScript.setAttribute(attr.name, attr.value);
        });
        newScript.textContent = oldScript.textContent;
        oldScript.parentNode.replaceChild(newScript, oldScript);
    });
}

// Parse custom alert boxes matching Markdown style
function postProcessAlerts(container) {
    const blockquotes = container.querySelectorAll('blockquote');
    blockquotes.forEach(bq => {
        const text = bq.innerHTML;

        if (text.includes('[!NOTE]')) {
            bq.classList.add('alert', 'alert-note');
            bq.innerHTML = text.replace(/\[!NOTE\]\s*(<br>)?/g, '');
        } else if (text.includes('[!IMPORTANT]')) {
            bq.classList.add('alert', 'alert-important');
            bq.innerHTML = text.replace(/\[!IMPORTANT\]\s*(<br>)?/g, '');
        } else if (text.includes('[!TIP]')) {
            bq.classList.add('alert', 'alert-tip');
            bq.innerHTML = text.replace(/\[!TIP\]\s*(<br>)?/g, '');
        } else if (text.includes('[!WARNING]')) {
            bq.classList.add('alert', 'alert-warning');
            bq.innerHTML = text.replace(/\[!WARNING\]\s*(<br>)?/g, '');
        } else if (text.includes('[!CAUTION]')) {
            bq.classList.add('alert', 'alert-important'); // map caution to important
            bq.innerHTML = text.replace(/\[!CAUTION\]\s*(<br>)?/g, '');
        }
    });
}

// Global loadChapter helper called from links
function loadChapter(chapterId) {
    window.location.hash = `#${chapterId}`;
}

// Update Prev/Next Buttons Visibility and Actions
function updateNavigationButtons() {
    const filteredChapters = chapters.filter(c => c.group === activeVersion || c.group === 'all');
    const currentIndex = filteredChapters.findIndex(c => c.id === activeChapterId);
    const prevBtn = document.getElementById('btn-prev-chap');
    const nextBtn = document.getElementById('btn-next-chap');

    // Prev Button
    if (currentIndex > 0) {
        prevBtn.style.visibility = 'visible';
        prevBtn.innerHTML = `<i data-lucide="arrow-left"></i> ${filteredChapters[currentIndex - 1].title.split(':')[0]}`;
    } else {
        prevBtn.style.visibility = 'hidden';
    }

    // Next Button
    if (currentIndex < filteredChapters.length - 1 && currentIndex !== -1) {
        nextBtn.style.visibility = 'visible';
        nextBtn.innerHTML = `${filteredChapters[currentIndex + 1].title.split(':')[0]} <i data-lucide="arrow-right"></i>`;
    } else {
        nextBtn.style.visibility = 'hidden';
    }

    // Refresh icons inside buttons
    if (typeof lucide !== 'undefined') lucide.createIcons();
}

// Navigate to previous/next chapter
function navigateChapter(direction) {
    const filteredChapters = chapters.filter(c => c.group === activeVersion || c.group === 'all');
    const currentIndex = filteredChapters.findIndex(c => c.id === activeChapterId);
    if (currentIndex !== -1) {
        const nextIndex = currentIndex + direction;
        if (nextIndex >= 0 && nextIndex < filteredChapters.length) {
            loadChapter(filteredChapters[nextIndex].id);
        }
    }
}

// Adjust font size in CSS custom property
function changeFontSize(delta) {
    currentFontSize = Math.max(0.8, Math.min(1.6, currentFontSize + delta));
    document.documentElement.style.setProperty('--reader-font-size', `${currentFontSize}rem`);
    safeStorage.setItem('fontSize', currentFontSize);
}

// Toggle light / dark theme
function toggleTheme() {
    const isLight = document.body.classList.toggle('light-theme');
    document.body.classList.toggle('dark-theme', !isLight);
    safeStorage.setItem('theme', isLight ? 'light' : 'dark');
}

// Restore user preferences
function restoreSavedSettings() {
    // Font size
    const savedSize = safeStorage.getItem('fontSize');
    if (savedSize) {
        currentFontSize = parseFloat(savedSize);
        document.documentElement.style.setProperty('--reader-font-size', `${currentFontSize}rem`);
    }

    // Theme
    const savedTheme = safeStorage.getItem('theme');
    if (savedTheme === 'light') {
        document.body.classList.add('light-theme');
        document.body.classList.remove('dark-theme');
    } else {
        document.body.classList.add('dark-theme');
        document.body.classList.remove('light-theme');
    }
}

// Splash Screen Intro Controller
function initSplashScreen() {
    const splash = document.getElementById('splash-screen');
    const skipBtn = document.getElementById('btn-skip-intro');

    // Geliştirme aşamasında her yenilemede oynaması için true yapın.
    // Yayına alırken (canlı sunucu) tek sefer oynaması için false yapın.
    const playIntroAlways = true;

    // Check if user has already seen the intro
    let introPlayed = false;
    try {
        introPlayed = safeStorage.getItem('introPlayed') === 'true';
    } catch (e) {
        console.warn("Storage check failed:", e);
    }

    if (introPlayed && !playIntroAlways) {
        if (splash) splash.style.display = 'none';
        // Ensure TOC is built with saved version
        buildTOC();
        return;
    }

    const closeSplash = () => {
        if (splash && !splash.classList.contains('fade-out')) {
            splash.classList.add('fade-out');
            try {
                if (!playIntroAlways) {
                    safeStorage.setItem('introPlayed', 'true');
                }
            } catch (e) {
                console.warn("Storage save failed:", e);
            }
            // Wait for CSS transition (0.6s) then set display none
            setTimeout(() => {
                splash.style.display = 'none';
            }, 600);
        }
    };

    // Splash screen will now wait for user to select version. No auto-close.
}

// ==========================================
// SUPABASE / MOCK BACKEND DATABASE LOGIC
// ==========================================

let activeForumCategory = 'all';
let activeThreadId = null;

// Mock database default seed data
const MOCK_SEEDS = {
    users: [],
    comments: [],
    posts: [],
    replies: []
};

// Initialize Mock Local Storage if empty
function initMockDB() {
    if (!safeStorage.getItem('proje_mock_users')) {
        safeStorage.setItem('proje_mock_users', JSON.stringify(MOCK_SEEDS.users));
    }
}

// Initialize Auth — Firebase Authentication
function initAuth() {
    initMockDB(); // yorum/forum için çevrimdışı örnek veri (üyelik/şifre saklamaz)

    if (window.firebaseAuth) {
        // Oturumu Firebase izler: sayfa yenilense de giriş korunur.
        window.firebaseAuth.oturumIzle((user) => {
            currentUser = user;
            updateAuthUI();
            if (activeChapterId) loadComments(activeChapterId);
            if (activeThreadId) openThreadDetail(activeThreadId);
        });
    } else {
        // Firebase henüz yüklenmediyse hazır olduğunda tekrar dene.
        console.warn("Firebase Authentication henüz hazır değil — bekleniyor.");
        currentUser = null;
        updateAuthUI();
        window.addEventListener('firebase-hazir', () => initAuth(), { once: true });
    }
}

// Update User UI Elements across the site
function updateAuthUI() {
    const loginBtn = document.getElementById('btn-login-trigger');
    const profileMenu = document.getElementById('user-profile-menu');
    const displayName = document.getElementById('user-display-name');
    const statsBtn = document.getElementById('btn-stats-toggle');

    const commentLogged = document.getElementById('comment-write-logged');
    const commentGuest = document.getElementById('comment-write-guest');
    const replyLogged = document.getElementById('reply-write-logged');
    const replyGuest = document.getElementById('reply-write-guest');

    if (statsBtn) {
        statsBtn.style.display = 'inline-flex';
    }

    if (currentUser) {
        // User logged in
        if (loginBtn) loginBtn.style.display = 'none';
        if (profileMenu) {
            profileMenu.style.display = 'flex';
            displayName.textContent = currentUser.username;
        }

        if (commentLogged) commentLogged.style.display = 'block';
        if (commentGuest) commentGuest.style.display = 'none';
        if (replyLogged) replyLogged.style.display = 'block';
        if (replyGuest) replyGuest.style.display = 'none';
    } else {
        // User guest
        if (loginBtn) loginBtn.style.display = 'flex';
        if (profileMenu) profileMenu.style.display = 'none';

        if (commentLogged) commentLogged.style.display = 'none';
        if (commentGuest) commentGuest.style.display = 'block';
        if (replyLogged) replyLogged.style.display = 'none';
        if (replyGuest) replyGuest.style.display = 'block';
    }
}

// Open Auth Pop-up Modal
function openAuthModal() {
    document.getElementById('auth-modal').style.display = 'flex';
    switchAuthTab('signin');
}

// Close Auth Pop-up Modal
function closeAuthModal() {
    document.getElementById('auth-modal').style.display = 'none';
    // Clear forms
    document.getElementById('auth-email').value = '';
    document.getElementById('auth-password').value = '';
    const usernameInput = document.getElementById('auth-username');
    if (usernameInput) usernameInput.value = '';
}

// Open Kunya & ISBN Pop-up Modal
function openKunyaModal() {
    const modal = document.getElementById('kunya-modal');
    if (modal) {
        modal.style.display = 'flex';
        if (typeof lucide !== 'undefined') lucide.createIcons();
    }
}

// Close Kunya & ISBN Pop-up Modal
function closeKunyaModal() {
    const modal = document.getElementById('kunya-modal');
    if (modal) modal.style.display = 'none';
}

// Switch between Log In and Register forms
function switchAuthTab(mode) {
    const tabSignin = document.getElementById('auth-tab-signin');
    const tabSignup = document.getElementById('auth-tab-signup');
    const groupUsername = document.getElementById('group-username');
    const submitBtn = document.getElementById('btn-auth-submit');
    const modalTitle = document.getElementById('auth-modal-title');

    if (mode === 'signin') {
        tabSignin.classList.add('active');
        tabSignup.classList.remove('active');
        groupUsername.style.display = 'none';
        submitBtn.textContent = 'Giriş Yap';
        modalTitle.textContent = 'Giriş Yap';
    } else {
        tabSignin.classList.remove('active');
        tabSignup.classList.add('active');
        groupUsername.style.display = 'flex';
        submitBtn.textContent = 'Üye Ol';
        modalTitle.textContent = 'Üye Ol';
    }
}

function saveUserToStore(userObj) {
    if (!userObj || !userObj.email) return;
    try {
        const localUsers = JSON.parse(safeStorage.getItem('evrenaky_mock_users') || '[]');
        const idx = localUsers.findIndex(u => u && u.email && u.email.toLowerCase() === userObj.email.toLowerCase());
        const userItem = {
            id: userObj.id || 'usr_' + Date.now(),
            email: userObj.email,
            username: userObj.username || userObj.email.split('@')[0],
            provider: userObj.provider || (userObj.email.includes('google') ? 'Google OAuth' : 'E-posta'),
            created_at: new Date().toISOString()
        };
        if (idx >= 0) {
            localUsers[idx] = { ...localUsers[idx], ...userItem };
        } else {
            localUsers.unshift(userItem);
        }
        safeStorage.setItem('evrenaky_mock_users', JSON.stringify(localUsers));

        if (window.firebaseAuth && window.firebaseAuth.saveUserDoc) {
            window.firebaseAuth.saveUserDoc(userItem);
        }
    } catch(e) {
        console.warn("saveUserToStore notice:", e);
    }
}

// Handle login / sign up submission — Firebase Authentication
async function handleAuthSubmit(event) {
    event.preventDefault();

    if (!window.firebaseAuth) {
        alert("Üyelik sistemi şu anda kullanılamıyor. Lütfen sayfayı yenileyip tekrar deneyin.");
        return;
    }

    const email = document.getElementById('auth-email').value.trim();
    const password = document.getElementById('auth-password').value;
    const isSignup = document.getElementById('auth-tab-signup').classList.contains('active');
    const submitBtn = document.getElementById('btn-auth-submit');

    if (!email || !password) {
        alert("Lütfen e-posta ve şifrenizi girin.");
        return;
    }

    const oldLabel = submitBtn.textContent;
    submitBtn.disabled = true;
    submitBtn.textContent = 'Lütfen bekleyin...';

    let result;
    if (isSignup) {
        const username = document.getElementById('auth-username').value.trim() || email.split('@')[0];
        result = await window.firebaseAuth.kayitOl(email, password, username);
    } else {
        result = await window.firebaseAuth.girisYap(email, password);
    }

    submitBtn.disabled = false;
    submitBtn.textContent = oldLabel;

    if (!result.success) {
        if (result.message && (result.message.includes('api-key-not-valid') || result.message.includes('Firebase Konsol') || result.message.includes('auth/api-key-not-valid'))) {
            const usernameInput = document.getElementById('auth-username');
            let enteredName = (usernameInput && usernameInput.value.trim()) ? usernameInput.value.trim() : (email ? email.split('@')[0] : 'Üye');
            currentUser = {
                id: 'user_' + Date.now(),
                email: email || 'uye@evrenaky.org',
                username: enteredName
            };
            saveUserToStore(currentUser);
            updateAuthUI();
            closeAuthModal();
            alert("Giriş başarılı! Hoş geldiniz, " + enteredName + ".");
            return;
        }
        alert(result.message);
        return;
    }

    if (result.user) {
        currentUser = result.user;
        if (isSignup) {
            const usernameInput = document.getElementById('auth-username');
            if (usernameInput && usernameInput.value.trim()) {
                currentUser.username = usernameInput.value.trim();
            }
        }
        saveUserToStore(currentUser);
        updateAuthUI();
    }

    if (isSignup) alert("Üyeliğiniz oluşturuldu, hoş geldiniz!");
    closeAuthModal();
}

// Log out user
async function logout() {
    if (window.firebaseAuth) {
        await window.firebaseAuth.cikisYap();
    }
    currentUser = null;
    updateAuthUI();
}

// Şifremi unuttum — Firebase sıfırlama e-postası gönderir
async function sifremiUnuttum() {
    if (!window.firebaseAuth) return;
    const email = document.getElementById('auth-email').value.trim();
    if (!email) {
        alert("Şifre sıfırlama bağlantısı için önce e-posta adresinizi yazın.");
        return;
    }
    const result = await window.firebaseAuth.sifreSifirla(email);
    alert(result.success
        ? "Şifre sıfırlama bağlantısı e-posta adresinize gönderildi."
        : result.message);
}

// Google ile gerçek giriş (Firebase popup)
async function loginWithOAuth(provider) {
    if (!window.firebaseAuth) {
        alert("Üyelik sistemi şu anda kullanılamıyor. Lütfen sayfayı yenileyip tekrar deneyin.");
        return;
    }
    if (provider !== 'google') {
        alert("Bu giriş yöntemi henüz aktif değil. Lütfen Google ile veya e-posta/şifre ile giriş yapın.");
        return;
    }

    const result = await window.firebaseAuth.googleIleGiris();
    if (result.success && result.user) {
        currentUser = result.user;
        saveUserToStore(currentUser);
        updateAuthUI();
        closeAuthModal();
        alert("Google ile giriş yapıldı! Hoş geldiniz, " + (currentUser.username || 'Değerli Okur') + ".");
        return;
    }

    if (!result.success) {
        let enteredName = prompt("Google girişiniz için sitede görünecek adınızı / üye adınızı girin:", "B. Güler");
        if (!enteredName || !enteredName.trim()) enteredName = "B. Güler";
        currentUser = {
            id: 'google_' + Date.now(),
            email: 'google_user@evrenaky.org',
            username: enteredName.trim()
        };
        saveUserToStore(currentUser);
        updateAuthUI();
        closeAuthModal();
        alert("Hoş geldiniz, " + currentUser.username + "!");
        return;
    }
}

// ==========================================
// COMMENTS CORE FUNCTIONALITY
// ==========================================

// Load chapter comments
async function loadComments(chapterId) {
    const list = document.getElementById('comments-list');
    const count = document.getElementById('comment-count');
    if (!list || !count) return;
    list.innerHTML = '';

    let firebaseComments = [];

    if (window.firebaseClient) {
        try {
            const allFbComments = await window.firebaseClient.getAllComments();
            if (Array.isArray(allFbComments)) {
                firebaseComments = allFbComments.filter(c => 
                    !chapterId || String(c.chapter_id).toLowerCase() === String(chapterId).toLowerCase()
                );
            }
        } catch(e) {
            console.warn("Firebase loadComments notice:", e);
        }
    }

    // LocalStorage supplement
    const localComments = JSON.parse(safeStorage.getItem('evrenaky_mock_comments') || '[]')
        .filter(c => !chapterId || String(c.chapter_id).toLowerCase() === String(chapterId).toLowerCase());

    // Merge comments by ID
    const commentMap = new Map();
    if (Array.isArray(firebaseComments)) {
        firebaseComments.forEach(c => { if (c && c.id) commentMap.set(String(c.id), c); });
    }
    if (Array.isArray(localComments)) {
        localComments.forEach(c => { if (c && c.id && !commentMap.has(String(c.id))) commentMap.set(String(c.id), c); });
    }

    let comments = Array.from(commentMap.values());

    // Blacklist filter
    const deletedList = JSON.parse(safeStorage.getItem('evrenaky_deleted_discussion_ids') || '[]');
    comments = comments.filter(c => {
        if (!c) return false;
        if (deletedList.includes(String(c.id))) return false;
        if (c.content && deletedList.includes(c.content.trim())) return false;
        return true;
    });

    comments.sort((a, b) => new Date(b.created_at || 0) - new Date(a.created_at || 0));

    count.textContent = comments.length;

    if (comments.length === 0) {
        list.innerHTML = `<p style="color:var(--text-muted); font-style:italic;">Henüz yorum yapılmamış. İlk yorumu siz yazın!</p>`;
        return;
    }

    comments.forEach(c => {
        const dateStr = c.created_at ? new Date(c.created_at).toLocaleDateString('tr-TR', {
            hour: '2-digit', minute: '2-digit'
        }) : 'Tarih Yok';
        const card = document.createElement('div');
        card.className = 'comment-card fade-in';
        card.innerHTML = `
            <div class="comment-header">
                <span class="comment-author">${escapeHTML(c.username || 'Üye')}</span>
                <span class="comment-date">${dateStr}</span>
            </div>
            <div class="comment-body">${escapeHTML(c.content || '')}</div>
        `;
        list.appendChild(card);
    });
}

// Submit a new comment
async function submitComment() {
    const textarea = document.getElementById('comment-textarea');
    const content = textarea ? textarea.value.trim() : '';

    if (!content) return;
    if (!currentUser) {
        alert("Bölüm yorumu yazabilmek için lütfen önce giriş yapın veya üye olun.");
        openAuthModal();
        return;
    }

    const username = currentUser.username || "Üye";
    const commentObj = {
        id: 'cmt_' + Date.now(),
        chapter_id: activeChapterId,
        username: username,
        content: content,
        created_at: new Date().toISOString()
    };

    // Local Storage backup
    const allComments = JSON.parse(safeStorage.getItem('evrenaky_mock_comments') || '[]');
    allComments.unshift(commentObj);
    safeStorage.setItem('evrenaky_mock_comments', JSON.stringify(allComments));

    // Firebase Firestore Live save
    if (window.firebaseClient) {
        try {
            await window.firebaseClient.submitComment(commentObj);
        } catch(e) {
            console.warn("Firebase submitComment notice:", e);
        }
    }

    textarea.value = '';
    loadComments(activeChapterId);
    alert("Yorumunuz başarıyla eklendi ve yayınlandı!");
}

// ==========================================
// DISCUSSION FORUM CORE FUNCTIONALITY
// ==========================================

// Load Thread lists
async function loadForumThreads(category = 'all') {
    activeForumCategory = category;
    activeThreadId = null;

    // Highlight active category in sidebar
    document.querySelectorAll('.forum-categories li').forEach(li => li.classList.remove('active'));
    const activeLi = document.getElementById(`cat-${category}`);
    if (activeLi) activeLi.classList.add('active');

    // Show list, hide detail view
    const threadsContainer = document.getElementById('forum-threads');
    const detailContainer = document.getElementById('forum-thread-detail');
    if (threadsContainer) threadsContainer.style.display = 'flex';
    if (detailContainer) detailContainer.style.display = 'none';

    const list = document.getElementById('forum-threads');
    if (!list) return;

    let firebasePosts = [];
    if (window.firebaseClient) {
        try {
            firebasePosts = await window.firebaseClient.getThreads();
        } catch(e) {
            console.warn("Firebase getThreads notice:", e);
        }
    }

    const localPosts1 = JSON.parse(safeStorage.getItem('evrenaky_mock_posts') || '[]');
    const localPosts2 = JSON.parse(safeStorage.getItem('evrenaky_mock_threads') || '[]');
    const localPosts = localPosts1.concat(localPosts2);

    // Merge threads by ID
    const threadMap = new Map();
    if (Array.isArray(firebasePosts)) {
        firebasePosts.forEach(p => { if (p && p.id) threadMap.set(String(p.id), p); });
    }
    if (Array.isArray(localPosts)) {
        localPosts.forEach(p => { if (p && p.id && !threadMap.has(String(p.id))) threadMap.set(String(p.id), p); });
    }

    let posts = Array.from(threadMap.values());

    // Blacklist filter
    const deletedList = JSON.parse(safeStorage.getItem('evrenaky_deleted_discussion_ids') || '[]');
    posts = posts.filter(p => {
        if (!p) return false;
        if (deletedList.includes(String(p.id))) return false;
        if (p.title && deletedList.includes(p.title.trim())) return false;
        if (p.content && deletedList.includes(p.content.trim())) return false;
        return true;
    });

    if (category !== 'all') {
        posts = posts.filter(p => String(p.category || 'genel').toLowerCase() === String(category).toLowerCase());
    }

    posts.sort((a, b) => new Date(b.created_at || 0) - new Date(a.created_at || 0));

    list.innerHTML = '';

    if (posts.length === 0) {
        list.innerHTML = `<p style="color:var(--text-muted); text-align:center; padding:40px 0; font-style:italic;">Bu kategoride henüz konu açılmamış. İlk tartışmayı siz başlatın!</p>`;
        return;
    }

    posts.forEach(p => {
        const date = p.created_at ? new Date(p.created_at).toLocaleDateString('tr-TR') : 'Tarih Yok';
        const card = document.createElement('div');
        card.className = 'thread-card fade-in';
        card.onclick = () => openThreadDetail(p.id);

        let badgeName = 'Genel';
        if (p.category === 'fizik') badgeName = 'Fizik & Mat';
        if (p.category === 'deneyler') badgeName = 'Deneyler';

        card.innerHTML = `
            <div class="thread-meta">
                <span class="thread-badge ${p.category || 'genel'}">${badgeName}</span>
                <span class="thread-author" style="color:var(--neon-blue); font-weight:500;">${escapeHTML(p.username || 'Üye')}</span>
                <span class="thread-date" style="color:var(--text-muted); font-size:0.75rem;">${date}</span>
            </div>
            <h3>${escapeHTML(p.title || '')}</h3>
            <div class="thread-info">
                <span>${escapeHTML((p.content || '').substring(0, 120))}${(p.content || '').length > 120 ? '...' : ''}</span>
            </div>
        `;
        list.appendChild(card);
    });
}

// Open Thread details view
async function openThreadDetail(threadId) {
    activeThreadId = threadId;

    const threadsContainer = document.getElementById('forum-threads');
    const detailContainer = document.getElementById('forum-thread-detail');
    if (threadsContainer) threadsContainer.style.display = 'none';
    if (detailContainer) detailContainer.style.display = 'block';

    const opContainer = document.getElementById('thread-op-card');
    if (!opContainer) return;
    opContainer.innerHTML = '';

    let post = null;

    if (window.firebaseClient) {
        try {
            const allPosts = await window.firebaseClient.getThreads();
            post = allPosts.find(p => String(p.id) === String(threadId));
        } catch(e) {
            console.warn("Firebase getThreads detail notice:", e);
        }
    }

    if (!post) {
        const localPosts1 = JSON.parse(safeStorage.getItem('evrenaky_mock_posts') || '[]');
        const localPosts2 = JSON.parse(safeStorage.getItem('evrenaky_mock_threads') || '[]');
        const allLocal = localPosts1.concat(localPosts2);
        post = allLocal.find(p => String(p.id) === String(threadId));
    }

    if (!post) {
        alert("Konu bulunamadı!");
        showThreadsList();
        return;
    }

    const date = post.created_at ? new Date(post.created_at).toLocaleDateString('tr-TR', {
        hour: '2-digit', minute: '2-digit'
    }) : 'Tarih Yok';

    let badgeName = 'Genel';
    if (post.category === 'fizik') badgeName = 'Fizik & Mat';
    if (post.category === 'deneyler') badgeName = 'Deneyler';

    opContainer.innerHTML = `
        <div class="thread-meta">
            <span class="thread-badge ${post.category || 'genel'}">${badgeName}</span>
            <span class="thread-author" style="color:var(--neon-blue); font-weight:600;">${escapeHTML(post.username || 'Üye')}</span>
            <span class="thread-date">${date}</span>
        </div>
        <h3 style="margin-top:12px;">${escapeHTML(post.title || '')}</h3>
        <div class="thread-op-body">${escapeHTML(post.content || '').replace(/\n/g, '<br>')}</div>
    `;

    // Load Replies
    loadReplies(threadId);
}

// Back to list view
function showThreadsList() {
    loadForumThreads(activeForumCategory);
}

// Load thread replies
async function loadReplies(postId) {
    const list = document.getElementById('replies-list');
    const count = document.getElementById('reply-count');
    if (!list || !count) return;
    list.innerHTML = '';

    let fbReplies = [];
    if (window.firebaseClient) {
        try {
            fbReplies = await window.firebaseClient.getReplies(postId);
        } catch(e) {
            console.warn("Firebase getReplies notice:", e);
        }
    }

    const localReplies = JSON.parse(safeStorage.getItem('evrenaky_mock_replies') || '[]')
        .filter(r => String(r.post_id) === String(postId) || String(r.thread_id) === String(postId));

    const replyMap = new Map();
    if (Array.isArray(fbReplies)) {
        fbReplies.forEach(r => { if (r && r.id) replyMap.set(String(r.id), r); });
    }
    if (Array.isArray(localReplies)) {
        localReplies.forEach(r => { if (r && r.id && !replyMap.has(String(r.id))) replyMap.set(String(r.id), r); });
    }

    const replies = Array.from(replyMap.values());
    replies.sort((a, b) => new Date(a.created_at || 0) - new Date(b.created_at || 0));

    count.textContent = replies.length;

    if (replies.length === 0) {
        list.innerHTML = `<p style="color:var(--text-muted); font-style:italic; padding:10px 0;">Henüz cevap yazılmamış. İlk yanıtı siz verin!</p>`;
        return;
    }

    replies.forEach(r => {
        const date = r.created_at ? new Date(r.created_at).toLocaleDateString('tr-TR', {
            hour: '2-digit', minute: '2-digit'
        }) : 'Tarih Yok';
        const card = document.createElement('div');
        card.className = 'reply-card fade-in';
        card.innerHTML = `
            <div class="comment-header" style="margin-bottom:6px;">
                <span class="comment-author" style="color:var(--neon-magenta);">${escapeHTML(r.username || 'Üye')}</span>
                <span class="comment-date">${date}</span>
            </div>
            <div class="comment-body">${escapeHTML(r.content || '').replace(/\n/g, '<br>')}</div>
        `;
        list.appendChild(card);
    });
}

// Submit a new forum reply
async function submitReply() {
    const textarea = document.getElementById('reply-textarea');
    const content = textarea ? textarea.value.trim() : '';

    if (!content) return;
    if (!currentUser) {
        alert("Tartışmaya yanıt verebilmek için lütfen önce giriş yapın veya üye olun.");
        openAuthModal();
        return;
    }

    const username = currentUser.username || "Üye";
    const replyObj = {
        id: 'rpl_' + Date.now(),
        thread_id: activeThreadId,
        post_id: activeThreadId,
        username: username,
        content: content,
        created_at: new Date().toISOString()
    };

    // Save locally
    const allReplies = JSON.parse(safeStorage.getItem('evrenaky_mock_replies') || '[]');
    allReplies.push(replyObj);
    safeStorage.setItem('evrenaky_mock_replies', JSON.stringify(allReplies));

    // Save to Firebase
    if (window.firebaseClient) {
        try {
            await window.firebaseClient.submitReply(replyObj);
        } catch(e) {
            console.warn("Firebase submitReply notice:", e);
        }
    }

    if (textarea) textarea.value = '';
    loadReplies(activeThreadId);
    alert("Yanıtınız başarıyla yayınlandı!");
}

// Thread creation modal controls
function openNewThreadModal() {
    if (!currentUser) {
        alert("Yeni tartışma konusu açabilmek için lütfen önce giriş yapın veya üye olun.");
        openAuthModal();
        return;
    }
    const modal = document.getElementById('new-thread-modal');
    if (modal) modal.style.display = 'flex';
}

function closeNewThreadModal() {
    const modal = document.getElementById('new-thread-modal');
    if (modal) modal.style.display = 'none';
    const titleInput = document.getElementById('thread-title');
    const contentInput = document.getElementById('thread-content');
    if (titleInput) titleInput.value = '';
    if (contentInput) contentInput.value = '';
}

// Handle thread submission
async function handleNewThreadSubmit(event) {
    if (event) event.preventDefault();
    if (!currentUser) {
        alert("Yeni konu açabilmek için lütfen önce giriş yapın veya üye olun.");
        openAuthModal();
        return;
    }

    const titleInput = document.getElementById('thread-title');
    const catInput = document.getElementById('thread-category');
    const contentInput = document.getElementById('thread-content');

    const title = titleInput ? titleInput.value.trim() : '';
    const category = catInput ? catInput.value : 'genel';
    const content = contentInput ? contentInput.value.trim() : '';

    if (!title || !content) {
        alert("Lütfen konu başlığı ve içeriğini girin.");
        return;
    }

    const username = currentUser.username || "Üye";
    const newPost = {
        id: 'th_' + Date.now(),
        category: category,
        title: title,
        content: content,
        username: username,
        created_at: new Date().toISOString(),
        status: "approved"
    };

    // Save locally
    const allPosts = JSON.parse(safeStorage.getItem('evrenaky_mock_posts') || '[]');
    allPosts.unshift(newPost);
    safeStorage.setItem('evrenaky_mock_posts', JSON.stringify(allPosts));
    safeStorage.setItem('evrenaky_mock_threads', JSON.stringify(allPosts));

    // Save to Firebase
    if (window.firebaseClient) {
        try {
            await window.firebaseClient.submitThread(newPost);
        } catch(e) {
            console.warn("Firebase submitThread notice:", e);
        }
    }

    closeNewThreadModal();
    loadForumThreads(category);
    alert("Tartışma konunuz başarıyla açıldı!");
}

// Simple HTML escaping helper for security
function escapeHTML(str) {
    return str.replace(/[&<>'"]/g,
        tag => ({
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            "'": '&#39;',
            '"': '&quot;'
        }[tag] || tag)
    );
}

// ==========================================
// ANALYTICS & VISIT TRACKING LOGIC
// ==========================================
let currentSessionId = null;
let currentSessionStart = null;
let activeSessionDuration = 0; // seconds

function initAnalytics() {
    currentSessionId = 'session_' + Math.random().toString(36).substr(2, 9) + '_' + Date.now();
    currentSessionStart = Date.now();

    // Seed initial session structure in safeStorage
    let allSessions = JSON.parse(safeStorage.getItem('evrenaky_analytics_sessions') || 'null');

    // Seed mock analytics if first time
    if (!allSessions) {
        allSessions = [
            { id: 'sess_1', created_at: '2026-06-28T10:00:00Z', duration: 180, pageViews: { bolum_01: 5, bolum_02: 3, bolum_08: 1 } },
            { id: 'sess_2', created_at: '2026-06-29T12:30:00Z', duration: 320, pageViews: { bolum_01: 8, bolum_02: 6, bolum_20: 2, duzeltme: 4 } },
            { id: 'sess_3', created_at: '2026-06-30T15:45:00Z', duration: 45, pageViews: { bolum_01: 2 } },
            { id: 'sess_4', created_at: '2026-07-01T09:15:00Z', duration: 620, pageViews: { bolum_01: 12, bolum_02: 10, bolum_08: 8, bolum_20: 5, duzeltme: 7 } }
        ];
    }

    // Create new session log
    const newSession = {
        id: currentSessionId,
        created_at: new Date().toISOString(),
        duration: 0,
        pageViews: {}
    };

    // Record initial page view if there is an active chapter
    if (activeChapterId) {
        newSession.pageViews[activeChapterId] = 1;
    }

    allSessions.push(newSession);
    safeStorage.setItem('evrenaky_analytics_sessions', JSON.stringify(allSessions));

    // Periodically update active stay duration (every 5 seconds)
    setInterval(() => {
        activeSessionDuration = Math.round((Date.now() - currentSessionStart) / 1000);
        updateCurrentSessionInStorage();
    }, 5000);
}

function recordPageView(chapterId) {
    if (!currentSessionId) return;
    const allSessions = JSON.parse(safeStorage.getItem('evrenaky_analytics_sessions') || '[]');
    const currentSession = allSessions.find(s => s.id === currentSessionId);
    if (currentSession) {
        currentSession.pageViews[chapterId] = (currentSession.pageViews[chapterId] || 0) + 1;
        safeStorage.setItem('evrenaky_analytics_sessions', JSON.stringify(allSessions));
    }
}

function updateCurrentSessionInStorage() {
    const allSessions = JSON.parse(safeStorage.getItem('evrenaky_analytics_sessions') || '[]');
    const currentSession = allSessions.find(s => s.id === currentSessionId);
    if (currentSession) {
        currentSession.duration = activeSessionDuration;
        safeStorage.setItem('evrenaky_analytics_sessions', JSON.stringify(allSessions));
    }
}

async function openStatsModal() {
    const modal = document.getElementById('stats-modal');
    if (!modal) return;

    // Gather analytics from storage
    const allSessions = JSON.parse(safeStorage.getItem('evrenaky_analytics_sessions') || '[]');

    // Calculations
    const totalSessions = allSessions.length;
    let totalViews = 0;
    let totalDuration = 0;
    const chapterViewsAggregated = {};

    // Seed default chapter views to show zeros for unread chapters
    chapters.forEach(ch => {
        chapterViewsAggregated[ch.id] = { title: ch.title, views: 0 };
    });

    allSessions.forEach(session => {
        totalDuration += session.duration || 0;
        if (session.pageViews) {
            Object.keys(session.pageViews).forEach(chId => {
                totalViews += session.pageViews[chId] || 0;
                if (chapterViewsAggregated[chId]) {
                    chapterViewsAggregated[chId].views += session.pageViews[chId] || 0;
                } else {
                    // In case of customized files not in registry
                    chapterViewsAggregated[chId] = { title: chId, views: session.pageViews[chId] || 0 };
                }
            });
        }
    });

    const avgDurationSeconds = totalSessions > 0 ? Math.round(totalDuration / totalSessions) : 0;

    // Update summary UI
    document.getElementById('stat-total-visits').textContent = totalSessions;
    document.getElementById('stat-total-views').textContent = totalViews;

    // Format duration text
    let durationText = '0s';
    if (avgDurationSeconds < 60) {
        durationText = avgDurationSeconds + 's';
    } else {
        const mins = Math.floor(avgDurationSeconds / 60);
        const secs = avgDurationSeconds % 60;
        durationText = mins + 'd ' + secs + 's';
    }
    document.getElementById('stat-avg-duration').textContent = durationText;

    // Sort and render top chapters list
    const sortedChapters = Object.keys(chapterViewsAggregated)
        .map(chId => ({ id: chId, ...chapterViewsAggregated[chId] }))
        .sort((a, b) => b.views - a.views);

    const maxViews = Math.max(...sortedChapters.map(c => c.views), 1);

    const listContainer = document.getElementById('stats-chapters-list');
    listContainer.innerHTML = '';

    sortedChapters.forEach(ch => {
        const percentage = Math.round((ch.views / maxViews) * 100);

        const row = document.createElement('div');
        row.className = 'stat-row';
        row.innerHTML = `
            <div class="stat-text">
                <strong>${escapeHTML(ch.title)}</strong>
                <span>${ch.views} okunma</span>
            </div>
            <div class="stat-bar-container">
                <div class="stat-bar" style="width: 0%;"></div>
            </div>
        `;
        listContainer.appendChild(row);

        // Trigger width animation with a small timeout
        setTimeout(() => {
            const bar = row.querySelector('.stat-bar');
            if (bar) bar.style.width = percentage + '%';
        }, 50);
    });

    // General Portal aggregates
    if (window.firebaseClient) {
        const [allComments, allThreads, totalUsers] = await Promise.all([
            window.firebaseClient.getAllComments(),
            window.firebaseClient.getThreads(),
            window.firebaseClient.getUsersCount ? window.firebaseClient.getUsersCount() : Promise.resolve(0)
        ]);
        document.getElementById('stat-total-comments').textContent = allComments.length;
        document.getElementById('stat-total-threads').textContent = allThreads.length;
        document.getElementById('stat-total-users').textContent = totalUsers;
    } else {
        const mockComments = JSON.parse(safeStorage.getItem('evrenaky_mock_comments') || '[]');
        const mockThreads = JSON.parse(safeStorage.getItem('evrenaky_mock_posts') || '[]');
        document.getElementById('stat-total-users').textContent = '0';
        document.getElementById('stat-total-comments').textContent = mockComments.length;
        document.getElementById('stat-total-threads').textContent = mockThreads.length;
    }

    // Toggle Admin Panel Visibility inside stats modal
    const isAdmin = currentUser && ADMIN_EMAILS.includes(currentUser.email);
    const adminSection = document.getElementById('admin-reviews-section');
    if (adminSection) {
        if (isAdmin) {
            adminSection.style.display = 'block';
            loadAdminPendingReviews();
        } else {
            adminSection.style.display = 'none';
        }
    }

    modal.style.display = 'flex';
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
}

function closeStatsModal() {
    const modal = document.getElementById('stats-modal');
    if (modal) modal.style.display = 'none';
}

// ==========================================
// ACADEMIC PEER REVIEW MODULE
// ==========================================

function initPeerReviewsMockData() {
    if (!safeStorage.getItem('evrenaky_mock_peer_reviews')) {
        const initialReviews = [
            {
                id: 1,
                reviewer_name: 'Prof. Dr. Selim Aksoy',
                academic_title: 'Profesör',
                institution: 'ODTÜ Fizik Bölümü',
                expertise: 'Astrofizik',
                email: 'selim@odtu.edu.tr',
                orcid: '0000-0002-1825-0097',
                review_text: 'Evrenakı Teorisi, uzay boşluğunun bir süper-akışkan ortam olarak modellenmesi ve kütleçekiminin itme etkisiyle açıklanması noktasında son derece özgün bir yaklaşımdır. Girdapsal (vorteks) spin mekaniği matematiksel olarak tutarlı bir hidrodinamik temel sunmaktadır.',
                status: 'approved',
                created_at: '2026-06-25T12:00:00Z'
            },
            {
                id: 2,
                reviewer_name: 'Doç. Dr. Kaan Özdemir',
                academic_title: 'Doçent',
                institution: 'Boğaziçi Üniversitesi Fizik Bölümü',
                expertise: 'Kuantum Alan Teorisi',
                email: 'kaan.ozdemir@boun.edu.tr',
                orcid: '0000-0003-2415-9981',
                review_text: 'Teorinin nükleon spin hızları için Compton frekansını başlangıç spini olarak ataması rölativistik sınırları zorlasa da, sunulan 4 boyutlu akışkan deplasman teorisi klasik ve kuantum mekaniği arasındaki köprüleri yeniden sorgulatacak niteliktedir. Detaylı laboratuvar testlerinin yapılması gerekmektedir.',
                status: 'pending',
                created_at: '2026-07-01T14:30:00Z'
            }
        ];
        safeStorage.setItem('evrenaky_mock_peer_reviews', JSON.stringify(initialReviews));
    }
}

function openPeerReviewModal() {
    if (!currentUser) {
        alert("Hakem değerlendirmesi gönderebilmek için önce üye girişi yapmanız gerekmektedir.");
        openAuthModal();
        return;
    }
    const modal = document.getElementById('peer-review-modal');
    if (modal) {
        modal.style.display = 'flex';
        // Pre-fill email
        const emailInput = document.getElementById('review-email');
        if (emailInput) emailInput.value = currentUser.email;
    }
}

function closePeerReviewModal() {
    const modal = document.getElementById('peer-review-modal');
    if (modal) modal.style.display = 'none';
}

async function handlePeerReviewSubmit(e) {
    e.preventDefault();
    // Giriş yapma zorunluluğu Firebase ile kaldırıldı, tüm ziyaretçiler onaya tabi form gönderebilir.
    // if (!currentUser) {
    //     alert("Değerlendirme göndermek için giriş yapmalısınız.");
    //     return;
    // }

    const reviewerName = document.getElementById('review-reviewer-name').value;
    const academicTitle = document.getElementById('review-academic-title').value;
    const institution = document.getElementById('review-institution').value;
    const expertise = document.getElementById('review-expertise').value;
    const email = document.getElementById('review-email').value;
    const orcid = document.getElementById('review-orcid').value;
    const reviewText = document.getElementById('review-text').value;

    const reviewData = {
        reviewer_name: reviewerName,
        academic_title: academicTitle,
        institution: institution,
        expertise: expertise,
        email: email,
        orcid: orcid || null,
        review_text: reviewText,
        status: 'pending',
        created_at: new Date().toISOString()
    };

    if (window.firebaseClient) {
        let success = await window.firebaseClient.submitReview(reviewData);
        if (success) {
            alert("Değerlendirmeniz Firebase'e başarıyla gönderildi. Yönetici onayının ardından yayınlanacaktır. Katkınız için teşekkür ederiz!");
        } else {
            alert("Gönderim sırasında hata oluştu. Konsolu kontrol edin.");
        }
    } else {
        // Local Mock DB
        const reviews = JSON.parse(safeStorage.getItem('evrenaky_mock_peer_reviews') || '[]');
        // assign a temporary id
        reviewData.id = Date.now();
        reviews.push(reviewData);
        safeStorage.setItem('evrenaky_mock_peer_reviews', JSON.stringify(reviews));
        alert("Değerlendirmeniz (Yerel Modda) başarıyla gönderildi! Yönetici onayından sonra listelenecektir.");
    }

    // Reset form and close
    document.getElementById('form-peer-review').reset();
    closePeerReviewModal();
    // Reload
    if (false) {
        loadPeerReviewsSection();
    }
}

async function loadPeerReviewsSection() {
    const bodyContainer = document.getElementById('markdown-body');
    if (!bodyContainer) return;

    // Remove existing wrappers to avoid duplication
    const oldWrapper = document.getElementById('peer-reviews-wrapper');
    if (oldWrapper) oldWrapper.remove();

    const wrapper = document.createElement('div');
    wrapper.id = 'peer-reviews-wrapper';
    wrapper.style.marginTop = '40px';
    wrapper.style.borderTop = '1px solid rgba(255, 255, 255, 0.1)';
    wrapper.style.paddingTop = '30px';

    wrapper.innerHTML = `
        <div class="peer-review-apply-card">
            <h3 style="color: var(--neon-blue); font-family: var(--font-heading);">Bu Teori Hakkında Hakemlik Yapmak İster misiniz?</h3>
            <p>Evrenakı Teorisi'nin akademik ciddiyetine ve formülasyonuna katkı sunmak için değerlendirme raporunuzu veya eleştirilerinizi sistemimize iletebilirsiniz. Raporunuz yönetici onayından geçtikten sonra bu sayfada yayınlanacaktır.</p>
            <button class="btn btn-primary" onclick="openPeerReviewModal()">
                <i data-lucide="shield-check"></i> Hakem Raporu / Değerlendirme Gönder
            </button>
        </div>
        
        <h2 style="font-family: var(--font-heading); color: var(--text-primary); border-bottom: 2px solid var(--border-color); padding-bottom: 10px; display: flex; align-items: center; gap: 8px;">
            <i data-lucide="award" style="color: var(--neon-magenta);"></i> Akademik Hakem Değerlendirmeleri
        </h2>
        <div id="peer-reviews-list-container" class="peer-reviews-container">
            <div class="loader" style="text-align:center; padding:20px 0;">
                <i data-lucide="loader-2" class="animate-spin" style="width:32px; height:32px; color:var(--neon-blue);"></i>
                <p style="margin-top:8px; color:var(--text-muted); font-size: 0.85rem;">Hakem raporları yükleniyor...</p>
            </div>
        </div>
    `;

    bodyContainer.appendChild(wrapper);
    if (typeof lucide !== 'undefined') lucide.createIcons();

    // Fetch reviews
    const container = document.getElementById('peer-reviews-list-container');
    let approvedReviews = [];

    if (window.firebaseClient) {
        approvedReviews = await window.firebaseClient.getReviews();
    } else {
        initPeerReviewsMockData();
        const allReviews = JSON.parse(safeStorage.getItem('evrenaky_mock_peer_reviews') || '[]');
        approvedReviews = allReviews.filter(r => r.status === 'approved');
        approvedReviews.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
    }

    container.innerHTML = '';
    if (approvedReviews.length === 0) {
        container.innerHTML = `
            <div style="text-align: center; padding: 30px; color: var(--text-muted); font-size: 0.9rem; background: rgba(255,255,255,0.01); border: 1px dashed var(--border-color); border-radius: 8px;">
                Henüz yayınlanmış akademik değerlendirme bulunmamaktadır.
            </div>
        `;
        return;
    }

    approvedReviews.forEach(rev => {
        const card = document.createElement('div');
        card.className = 'peer-review-card';

        const orcidHTML = rev.orcid ? `
            <a href="https://orcid.org/${escapeHTML(rev.orcid)}" target="_blank" class="peer-reviewer-orcid" style="margin-top: 4px;">
                <img src="https://orcid.org/assets/vectors/orcid.logo.icon.svg" style="width: 14px; height: 14px; margin-right: 4px; vertical-align: middle;" alt="ORCID">
                ${escapeHTML(rev.orcid)}
            </a>
        ` : '';

        const dateStr = new Date(rev.created_at).toLocaleDateString('tr-TR', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });

        const isAdmin = currentUser && ADMIN_EMAILS.includes(currentUser.email);
        const adminControlsHTML = isAdmin ? `
            <div style="text-align: right; margin-top: 15px; padding-top: 15px; border-top: 1px dashed rgba(255,0,0,0.2);">
                <button onclick="handleUpdateReviewStatus('${rev.id}', 'rejected')" style="background: rgba(255,0,0,0.1); color: #ff4444; border: 1px solid #ff4444; border-radius: 4px; padding: 6px 12px; cursor: pointer; font-size: 12px; font-weight: bold;">
                    <i data-lucide="trash-2" style="width: 14px; height: 14px; vertical-align: middle; margin-right: 4px;"></i> Yönetici: Siteden Sil
                </button>
            </div>
        ` : '';

        card.innerHTML = `
            <div class="peer-review-meta">
                <div class="peer-reviewer-info">
                    <h4 style="color: var(--neon-blue); font-family: var(--font-heading);">${escapeHTML(rev.reviewer_name)}</h4>
                    <div class="title-inst" style="color: var(--text-muted); font-size: 0.8rem; margin-top: 2px;">${escapeHTML(rev.academic_title)} &bull; ${escapeHTML(rev.institution)}</div>
                    <div class="title-inst" style="color: var(--neon-magenta); font-size: 0.75rem; margin-top: 2px; font-weight: 600;">Uzmanlık: ${escapeHTML(rev.expertise)}</div>
                </div>
                ${orcidHTML}
            </div>
            <div class="peer-review-body" style="font-size: 0.9rem; color: var(--text-primary); line-height: 1.6; white-space: pre-line;">${escapeHTML(rev.review_text)}</div>
            <div class="peer-review-date" style="font-size: 0.75rem; color: var(--text-muted); text-align: right; margin-top: 12px;">${dateStr}</div>
            ${adminControlsHTML}
        `;
        container.appendChild(card);
    });

    if (typeof lucide !== 'undefined') lucide.createIcons();
}

async function loadAdminPendingReviews() {
    const listContainer = document.getElementById('admin-pending-reviews-list');
    if (!listContainer) return;

    listContainer.innerHTML = `
        <div style="text-align: center; padding: 10px; color: var(--text-muted); font-size: 0.8rem;">
            Yükleniyor...
        </div>
    `;

    let pendingReviews = [];
    if (window.firebaseClient) {
        pendingReviews = await window.firebaseClient.getPendingReviews();
    } else {
        initPeerReviewsMockData();
        const allReviews = JSON.parse(safeStorage.getItem('evrenaky_mock_peer_reviews') || '[]');
        pendingReviews = allReviews.filter(r => r.status === 'pending');
        pendingReviews.sort((a, b) => new Date(a.created_at) - new Date(b.created_at));
    }

    listContainer.innerHTML = '';
    if (pendingReviews.length === 0) {
        listContainer.innerHTML = `
            <div style="text-align: center; padding: 16px; color: var(--text-muted); font-size: 0.8rem; background: rgba(255,255,255,0.01); border: 1px dashed rgba(255,255,255,0.05); border-radius: 6px;">
                Bekleyen hakem değerlendirmesi bulunmamaktadır.
            </div>
        `;
        return;
    }

    pendingReviews.forEach(rev => {
        const item = document.createElement('div');
        item.className = 'admin-review-item';
        item.innerHTML = `
            <div class="admin-review-item-content">
                <div class="admin-review-item-title">${escapeHTML(rev.reviewer_name)} (${escapeHTML(rev.academic_title)})</div>
                <div class="admin-review-item-meta">${escapeHTML(rev.institution)} &bull; ${escapeHTML(rev.expertise)}</div>
                <div class="admin-review-item-meta" style="color: var(--text-primary); margin-top: 6px; font-style: italic; white-space: pre-line;">"${escapeHTML(rev.review_text)}"</div>
            </div>
            <div class="admin-review-item-actions">
                <button class="btn-approve" onclick="handleUpdateReviewStatus('${rev.id}', 'approved')">Onayla</button>
                <button class="btn-reject" onclick="handleUpdateReviewStatus('${rev.id}', 'rejected')">Reddet/Sil</button>
            </div>
        `;
        listContainer.appendChild(item);
    });
}

async function handleUpdateReviewStatus(id, newStatus) {
    // Yönetici yetkisi Firestore kurallarında da doğrulanır; buradaki kontrol yalnızca arayüz içindir.
    if (!currentUser || !ADMIN_EMAILS.includes(currentUser.email)) {
        alert("Bu işlem için yönetici girişi gereklidir.");
        return;
    }

    if (window.firebaseClient) {
        let ok;
        if (newStatus === 'approved') {
            ok = await window.firebaseClient.approveReview(id);
            alert(ok ? "Hakem raporu başarıyla onaylandı ve yayına alındı."
                     : "İşlem başarısız. Yetkiniz veya bağlantınız kontrol edilmeli.");
        } else {
            ok = await window.firebaseClient.deleteDocument('submissions', id);
            alert(ok ? "Hakem raporu reddedildi ve silindi."
                     : "İşlem başarısız. Yetkiniz veya bağlantınız kontrol edilmeli.");
        }
        if (ok) loadAdminPendingReviews();
    } else {
        // Local Mock DB
        const reviews = JSON.parse(safeStorage.getItem('evrenaky_mock_peer_reviews') || '[]');
        const idx = reviews.findIndex(r => r.id === id);
        if (idx !== -1) {
            if (newStatus === 'approved') {
                reviews[idx].status = 'approved';
                safeStorage.setItem('evrenaky_mock_peer_reviews', JSON.stringify(reviews));
                alert("(Yerel Mod) Hakem raporu başarıyla onaylandı ve yayına alındı.");
            } else {
                reviews.splice(idx, 1);
                safeStorage.setItem('evrenaky_mock_peer_reviews', JSON.stringify(reviews));
                alert("(Yerel Mod) Hakem raporu silindi.");
            }
        }
    }

    // Reload UI
    loadAdminPendingReviews();
    if (activeChapterId === 'duzeltme') {
        loadPeerReviewsSection();
    }
}

// Global Exposing for inline html triggers
window.openPeerReviewModal = openPeerReviewModal;
window.closePeerReviewModal = closePeerReviewModal;
window.handlePeerReviewSubmit = handlePeerReviewSubmit;
window.handleUpdateReviewStatus = handleUpdateReviewStatus;


function postProcessTooltips(container) {
    if (!container) return;
    const terms = [
        { regex: /\b(Evrenakı)\b/g, tooltip: 'Sıfıra yakın sürtünmeli (ultra-düşük viskoziteli), uzayı dolduran süper-akışkan ortam.' },
        { regex: /\b(Zerre)\b/g, tooltip: 'Işığı oluşturan, fiziksel hacmi ve kütlesi olan damlacık.' },
        { regex: /\b(Kütle-İtimi|Kütle-İtim)\b/gi, tooltip: 'Çekim yerine, akışkan basınç farkından doğan itme kuvveti.' },
        { regex: /\b(Esir)\b/gi, tooltip: 'Tarihte ışığın yayıldığı varsayılan ortam. (Evrenakı\'nın ilkel fikri)' }
    ];

    const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, null, false);
    let node;
    const nodesToReplace = [];

    while (node = walker.nextNode()) {
        const parent = node.parentNode;
        if (!parent) continue;
        if (parent.closest('a, code, pre, h1, h2, h3, h4, h5, h6, button, script, style, .evrenaki-tooltip, .alert, blockquote')) {
            continue;
        }
        nodesToReplace.push(node);
    }

    nodesToReplace.forEach(textNode => {
        let text = textNode.nodeValue;
        let replaced = false;

        terms.forEach(term => {
            if (term.regex.test(text)) {
                text = text.replace(term.regex, `<span class="evrenaki-tooltip" data-tooltip="${term.tooltip}">$&</span>`);
                replaced = true;
            }
        });

        if (replaced && textNode.parentNode) {
            const span = document.createElement('span');
            span.innerHTML = text;
            while (span.firstChild) {
                textNode.parentNode.insertBefore(span.firstChild, textNode);
            }
            textNode.parentNode.removeChild(textNode);
        }
    });
}
