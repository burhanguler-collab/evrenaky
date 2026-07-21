import os

path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_9_Hakem_Degerlendirmeleri\01_Prof_Riza_Demirbilek_Degerlendirmesi.md'
text_to_append = """

---

## Yazarın Teşekkürü

Evrenakı Teorisi'nin tohumlarının atıldığı o ilk günlerde, tam 18 yıl önce tanışma onuruna eriştiğim çok saygın ve değerli bilim insanı, kıymetli hocam Prof. Dr. Rıza Demirbilek'e en derin minnetlerimi sunarım.

Kendisi, engin bilgi birikimini hiçbir zaman esirgememiş; tüm şeffaflığıyla ve cömertçe benimle paylaşmıştır. Teorinin en kritik ve tıkandığı düşünülen kavşaklarında bana hep doğru yolu göstermiş; ilk bakışta olumsuz ya da sert gibi görünen ama aslında son derece yapıcı olan o muazzam eleştirileriyle, Evrenakı Teorisi'nin ayaklarının yere sağlam basmasını sağlamıştır.

Bu uzun, zorlu ve çoğu zaman meşakkatli gelişim yolculuğunda bana her daim destek olmuş; bilimsel tavizsizliği ve objektif duruşu sayesinde önümü aydınlatarak teorinin bugünkü olgunluğuna erişmesine vesile olmuştur. Kendisine duyduğum saygı ve minnet kelimelerle ifade edilemez. Şayet günün birinde bu teori deneysel olarak tam anlamıyla doğrulanır ve fizik dünyasında yerini alırsa, hiç şüphesiz bu tarihsel gelişimin en büyük pay sahiplerinden biri kıymetli hocam Prof. Dr. Rıza Demirbilek olacaktır.

Bilime ve hakikate olan sarsılmaz inancınız, birikiminiz ve bu esere kattığınız eşsiz vizyon için size sonsuz teşekkür ederim.
"""

with open(path, 'a', encoding='utf-8') as f:
    f.write(text_to_append)

print('Teşekkür yazısı eklendi.')
