import os
import re

path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Populer'
files = [f for f in os.listdir(path) if f.endswith('.md')]
files.sort()

replacements = {
    "kocaman bir yanlış": "eksik bir kavrayış",
    "yutturulan bu masalın": "ezberletilen bu varsayımın",
    "bir utanç yaşıyor ama bunu itiraf edecek cesareti bulamıyor": "ciddi bir açmazla karşı karşıya",
    "teslim bayrağıdır": "fiziği çıkmaza sokmuştur",
    "modern fiziğin kaçtığı": "klasik fiziğin açıklamakta zorlandığı",
    "kem küm eder": "tatmin edici bir cevap bulamaz",
    "sihirli bir muamma değildir": "çözülemez bir gizem değildir",
    "yüzünüze bir tokat gibi çarpar": "klasik ezberleri sarsar",
    "mistisizmi çöpe atar": "soyut kabulleri bir kenara bırakır"
}

summaries = {
    "populer_01.md": [
        "**Eski Fizik:** Uzay boş bir vakumdur; gezegenler bu hiçliğin içinde süzülür.",
        "**Evrenakı Teorisi:** Uzay, Evrenakı adı verilen sürtünmesiz bir süper-akışkanla doludur. Gezegenler bu akışkanın içindeki devasa girdaplardır."
    ],
    "populer_02.md": [
        "**Eski Fizik:** Cisimler birbirini gizemli, temas gerektirmeyen bir kütleçekim kuvvetiyle 'çeker'.",
        "**Evrenakı Teorisi:** Çekim yoktur; basınç farkından doğan bir 'itme' vardır (Kütle-İtimi). Gezegenlerin çevresindeki girdap, cisimleri merkeze doğru iter."
    ],
    "populer_03.md": [
        "**Eski Fizik:** Işık aynı anda hem dalga hem de kütlesiz bir parçacıktır (Dalga-Parçacık ikiliği).",
        "**Evrenakı Teorisi:** Işık, kütlesi ve hacmi olan, tıpkı mermiler gibi art arda dizilmiş sıvı damlacıklarıdır (Zerre Katarı)."
    ],
    "populer_04.md": [
        "**Eski Fizik:** Işığın davranışı, yansıma, kırılma ve yutulma için ayrı ayrı karmaşık modeller gerektirir.",
        "**Evrenakı Teorisi:** Tüm bu olaylar, Zerrelerin (mermilerin) çarptığı yüzeyin atomik yoğunluğuna bağlı tek bir mekanik kuralla (Akışkanlar Mekaniği) açıklanır."
    ],
    "populer_05.md": [
        "**Eski Fizik:** Dördüncü boyut zaman olabilir ya da uzay-zaman eğrisidir.",
        "**Evrenakı Teorisi:** Boyutlar matematiksel değil, fizikseldir. Evrenin enerjisini sağlayan sürekli bir akış mekanizması vardır."
    ],
    "populer_06.md": [
        "**Eski Fizik:** Yüksek hızlarda veya yüksek çekimde 'Zaman'ın kendisi bükülür ve yavaşlar.",
        "**Evrenakı Teorisi:** Zaman bükülmez, mekanik saatlerin işleyişi yavaşlar. Madde, yoğun Evrenakı akıntıları içinde daha fazla dirençle karşılaştığı için yavaş hareket eder."
    ],
    "populer_07.md": [
        "**Eski Fizik:** Galaksilerin dağılmamasını sağlayan, göremediğimiz devasa 'Karanlık Madde' haleleri vardır.",
        "**Evrenakı Teorisi:** Karanlık madde yoktur. Galaksilerin dönüşünü sabitleyen şey, içlerinde yüzdükleri Evrenakı sıvısının devasa makro-girdap etkileridir."
    ],
    "populer_08.md": [
        "**Eski Fizik:** Doğada birbirinden bağımsız 4 temel kuvvet vardır (Kütleçekim, Elektromanyetik, Güçlü, Zayıf).",
        "**Evrenakı Teorisi:** Evreni şekillendiren bu kuvvetlerin hepsi, tek bir temel ilkeye, yani Evrenakı sıvısındaki basınç ve akıntı mekanizmalarına dayanır."
    ],
    "populer_09.md": [
        "**Eski Fizik:** Ay ve Satürn'ün halkaları gibi yapıların kökeni bağımsız gök mekaniği olaylarıyla açıklanır.",
        "**Evrenakı Teorisi:** Bu yapılar, Kütle-İtimi ve sıvı girdaplarının yarattığı akışkan mekaniği yasalarının doğrudan ve doğal bir sonucudur."
    ],
    "populer_10.md": [
        "**Eski Fizik:** Esir (Ether) deneyi başarısız oldu, uzayda ışığı taşıyan bir ortam yoktur.",
        "**Evrenakı Teorisi:** Esir kavramı yanlış anlaşıldı. Modern fizik bile 'kuantum vakumu' diyerek uzayın boş olmadığını itiraf etmek zorunda kalmıştır; bu ortam Evrenakı'nın ta kendisidir."
    ],
    "populer_11.md": [
        "**Eski Fizik:** Teoriler sadece soyut matematiksel formüllerle geçerliliğini korur.",
        "**Evrenakı Teorisi:** Sadece teorik bir kurgu değil, bağımsız deneylerle ölçülebilen ve fiziksel olarak ispatlanabilen (Mai'nin Kanıtı) somut bir gerçekliktir."
    ]
}

def get_academic_link(filename):
    match = re.search(r'populer_(\d+)', filename)
    if match:
        num = match.group(1)
        return f"akademik_{num}"
    return "akademik_01"

for file in files:
    filepath = os.path.join(path, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply text replacements for tone softening
    for old_text, new_text in replacements.items():
        content = content.replace(old_text, new_text)

    # Check if we already have the summary/links
    if "## Bu Bölümde Ne Öğrendik?" not in content:
        summary_lines = summaries.get(file, ["**Eski Fizik:** Bilinmiyor.", "**Evrenakı Teorisi:** Akışkan mekaniğine dayanır."])
        
        academic_hash = get_academic_link(file)
        
        summary_block = f"""

---

## Bu Bölümde Ne Öğrendik?

> [!NOTE]
> - {summary_lines[0]}
> - {summary_lines[1]}

> [!TIP]
> Bu bölümün matematiksel ispatlarını ve akademik dildeki detaylı açıklamalarını görmek için **[Akademik Sürüm Kısım {int(academic_hash[-2:])}'ye geçiş yapın](#{academic_hash})**.
"""
        content += summary_block
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Tüm 11 dosya başarıyla güncellendi (Üslup, Özetler, Linkler).")
