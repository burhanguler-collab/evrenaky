import re

file_path = r"c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_3_Makro_Evren\01_Evrenin_Makine_Dairesi.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's do replacements manually or with regex. We can just use exact string replacement for safety.

replacements = [
    ("## Mikrodan Makroya Geçiş: Sorunun Cevabı", "### 3.1.1 Mikrodan Makroya Geçiş: Sorunun Cevabı"),
    ("## 29.9 Nükleonik Çift Dönüş: Mikroskobik Motorun Anatomisi", "### 3.1.2 Nükleonik Çift Dönüş: Mikroskobik Motorun Anatomisi"),
    ("## 29.10 Kütlenin Birleşmesi ve Kinetik Ayrışma (Kinetic Decoupling)", "### 3.1.3 Kütlenin Birleşmesi ve Kinetik Ayrışma (Kinetic Decoupling)"),
    ("### A) W-Salınımının Akustik Pompası: Statik Kütle-İtiminin (Yerçekimi) Doğuşu", "#### A) W-Salınımının Akustik Pompası: Statik Kütle-İtiminin (Yerçekimi) Doğuşu"),
    ("### B) Hızlı Dönüşün ($\\omega_1$) Kusulması: Makro-Vorteks ve Yörüngelerin Doğuşu", "#### B) Hızlı Dönüşün ($\\omega_1$) Kusulması: Makro-Vorteks ve Yörüngelerin Doğuşu"),
    ("### C) Kütlede Kalan Dönüş: Görünür Eksen Dönüşü ve Devinim", "#### C) Kütlede Kalan Dönüş: Görünür Eksen Dönüşü ve Devinim"),
    ("## 29.11 Evrenin Makine Dairesi", "### 3.1.4 Evrenin Makine Dairesi"),
    ("## 29.12 Gözlemsel Kanıt: Kütle Arttıkça Dönüş Neden Hızlanır?", "### 3.1.5 Gözlemsel Kanıt: Kütle Arttıkça Dönüş Neden Hızlanır?"),
    ("### Evrenakı Hidrodinamik Dengesi: Girdap ve Basıncın Evrensel Rekabeti", "#### Evrenakı Hidrodinamik Dengesi: Girdap ve Basıncın Evrensel Rekabeti"),
    ("## 29.13 Güneş Paradoksunun Çözümü: Gezegen ve Yıldız Kategorileri", "### 3.1.6 Güneş Paradoksunun Çözümü: Gezegen ve Yıldız Kategorileri"),
    ("## 29.14 Evrenakı Dinamiklerine Geçiş: Klasik İtirazlar ve Kuantum İzdüşümü", "### 3.1.7 Evrenakı Dinamiklerine Geçiş: Klasik İtirazlar ve Kuantum İzdüşümü"),
    ("## 29.15 Gözlemsel Anomalilerin Çöküşü: Kendi Kendine Hızlanan Kütleler ve Karanlık Madde", "### 3.1.8 Gözlemsel Anomalilerin Çöküşü: Kendi Kendine Hızlanan Kütleler ve Karanlık Madde"),
    ("### 1. Karanlık Madde İllüzyonu (Galaksilerin Aşırı Hızlı Dönüşü)", "#### 1. Karanlık Madde İllüzyonu (Galaksilerin Aşırı Hızlı Dönüşü)"),
    ("### 2. Kendi Kendine Hızlanan ve Parçalanan Asteroitler (YORP Etkisi)", "#### 2. Kendi Kendine Hızlanan ve Parçalanan Asteroitler (YORP Etkisi)"),
    ("### 3. Pulsar Glitch (Atarca Hızlanma Anomalisi)", "#### 3. Pulsar Glitch (Atarca Hızlanma Anomalisi)"),
    ("### Parametrik Bir Davet: $\\eta_E$ (Evrenakı Vizkozitesi) ve Gaia Verileri", "#### Parametrik Bir Davet: $\\eta_E$ (Evrenakı Vizkozitesi) ve Gaia Verileri"),
    ("### Parametrik Bir Davet: $\\kappa_d$ (İçsel Deşarj Sabiti) ve Katalog Verileri", "#### Parametrik Bir Davet: $\\kappa_d$ (İçsel Deşarj Sabiti) ve Katalog Verileri"),
    ("### Parametrik Bir Davet: Ayırt Edici Bir İmza Arayışı", "#### Parametrik Bir Davet: Ayırt Edici Bir İmza Arayışı"),
    ("### 3.1.1 Zitterbewegung'un Geometrik Sırrı: \"Dönüş Görünmez, Salınım Olarak İz Bırakır\"", "### 3.1.9 Zitterbewegung'un Geometrik Sırrı: \"Dönüş Görünmez, Salınım Olarak İz Bırakır\""),
    ("### 3.1.2 Makro Evren'e Açılan Kapı: Kütle-İtimi ve Vortekslere Giden Yol", "### 3.1.10 Makro Evren'e Açılan Kapı: Kütle-İtimi ve Vortekslere Giden Yol"),
    ("### 3.1.3 Termodinamik Bağlantı ve Titreşim Frekansları", "### 3.1.11 Termodinamik Bağlantı ve Titreşim Frekansları"),
]

for old, new in replacements:
    content = content.replace(old, new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Headers updated successfully!")
