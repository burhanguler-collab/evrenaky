# 12. Popüler Bilim Sözlüğü, Sıkça Sorulan Sorular ve İnteraktif Fizik Testi

Bu son bölümde, Evrenakı Teorisi yolculuğunuz boyunca karşılaştığınız bazı "havalı" kelimelerin en basit tanımlarını bulacaksınız. Ardından okuduklarınızı sınayabileceğiniz son bir Büyük Test sizi bekliyor.

---

## 📖 Popüler Bilim Sözlüğü (Evrenakı Terimleri)

**Evrenakı (Plenum):** Uzay boşluğu sandığınız o devasa, görünmez, sürtünmesi (viskozitesi) sıfıra çok yakın sıvı okyanustur. Evrenin sahnesi değil, bizzat oyuncusudur.

**Zerre:** Işık dalgası filan değil; Evrenakı okyanusunda mermi gibi fırlatılan, kütlesi ve hacmi olan minik fiziksel su damlalarıdır. Foton masalının gerçek yüzüdür.

**Kütle-İtimi:** Uzaktaki nesnelerin (Star Wars'taki Jedi'lar gibi) birbirini çekemeyeceğini söyleyen; gezegenleri bir arada tutan şeyin Evrenakı'nın onları birbirine doğru iten basıncı olduğunu belirten gerçek kütleçekim kanunudur.

**Makro-Girdap (Galaktik Vorteks):** Astronomların kırıntı gibi aradığı "Karanlık Madde" masalının ardındaki gerçek; dönen kara deliklerin ve gezegenlerin etraflarındaki Evrenakı denizinde oluşturdukları o devasa çay bardağı girdabıdır.

**Mach Konisi (Pruva Dalgası):** Işığın kendisi sanılan, ama aslında Zerre mermisinin Evrenakı içinde ses hızında (Mach 1) giderken önünde yarattığı V şeklindeki şok dalgasıdır. Çift yarık sihirbazlığını bozan şeydir.

**Dördüncü Boyut (W Ekseni):** Zaman yolculuğu yapılan mistik bir tünel değil; maddenin durmaksızın takla attığı, Evrenakı'yı karıştıran o görünmez makine dairesidir. Bize "titreşim" (Zitterbewegung) ve eksen yalpalaması olarak yansır.

---

## ❓ Sıkça Sorulan Sorular (SSS)

**Soru: Eğer uzay sıvıysa, uzay gemileri neden sürtünmeden alev almıyor?**
**Cevap:** Çünkü Evrenakı'nın sürtünmesi (viskozitesi) sudan, havadan, hatta bildiğimiz her şeyden trilyonlarca kat daha düşüktür ($\approx 10^{-11}$). Çok kaygan bir makine yağı gibidir. (Sürtünme tam sıfır olsaydı evren genişleyemezdi).

**Soru: Görelilik (Relativite) tamamen yalan mı?**
**Cevap:** Denklemler ve ölçümler (ışığın yavaşlaması vb.) yalan değil. Yalan olan, bu fiziksel olaylara "zaman bükülmesi" veya "uzay-zaman çarşafı" gibi mistik isimler takılmasıdır. Zaman mutlaktır, sadece saatiniz yorulur. 

**Soru: Kuantum mekaniğindeki süperpozisyon (Aynı anda iki yerde olma) durumu nasıl açıklanıyor?**
**Cevap:** Aynı anda iki yerde olma durumu yoktur. Olan şey, bir Zerrenin (merminin) Evrenakı denizinde yarattığı dalgalanmaların (Mach konisi) iki farklı yarıktan geçerek karışmasıdır. Madde tek yerdedir, dalgası (izdüşümü) ise etrafa yayılır.

---

## 🎯 BÜYÜK SINAV: Evrenakı'dan Mezun Olma Vakti

Popüler bölümü başarıyla tamamladınız! Şimdi eski fiziğin "Yalıtım Bandı" tabularını ne kadar yıktığınızı görme zamanı.

<div id="quiz-container" style="background: #111827; border: 1px solid #374151; padding: 25px; border-radius: 12px; margin-top: 25px; box-shadow: 0 4px 20px rgba(0,0,0,0.5);">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 1px solid #374151; padding-bottom: 15px;">
        <h3 style="margin: 0; color: #fff; display: flex; align-items: center; gap: 10px;">
            <i data-lucide="brain-circuit" style="color: var(--neon-magenta);"></i> 
            Karanlık Maddeyi Çöpe Atma Testi
        </h3>
        <span id="quiz-score-badge" style="background: rgba(0, 229, 255, 0.1); color: var(--neon-blue); padding: 4px 12px; border-radius: 20px; font-weight: bold; font-size: 0.9rem;">Soru 1 / 4</span>
    </div>
    <div id="quiz-body">
        <p id="quiz-question" style="font-size: 1.1rem; font-weight: 500; margin-bottom: 20px; line-height: 1.5; color: #e5e7eb;"></p>
        <div id="quiz-options" style="display: flex; flex-direction: column; gap: 10px;"></div>
        <div id="quiz-feedback" style="display: none; margin-top: 20px; padding: 15px; border-radius: 8px; font-weight: 500;"></div>
        <div style="margin-top: 20px; text-align: right;">
            <button id="quiz-next-btn" class="btn btn-primary" style="display: none; align-items: center; gap: 8px;" onclick="nextQuizQuestion()">
                Sonraki Soru <i data-lucide="arrow-right" style="width: 18px;"></i>
            </button>
        </div>
    </div>
</div>

<script>
(function() {
    const questions = [
        {
            q: "1. Evrenakı teorisine göre, içinde yaşadığımız bu devasa 'Uzay' aslında tam olarak nedir?",
            options: [
                "Denklem kurtarmak için icat edilen yalıtım bantlarıyla dolu bir boşluk.",
                "Sürtünmesi sıfıra çok yakın (ama sıfır olmayan), son derece kaygan ve yoğun bir sıvı okyanus.",
                "İçine gezegen atılınca bükülen görünmez bir yatak çarşafı.",
                "Karanlık maddenin saklandığı mistik bir depo."
            ],
            answer: 1,
            explain: "Doğru! Uzay bir vakum değil, sürtünmesi çok düşük bir Plenum okyanusudur. O çarşafları ve yalıtım bantlarını çöpe attık."
        },
        {
            q: "2. Dalından kopan bir elma neden yere (Dünya'ya) düşer?",
            options: [
                "Dünya bir Jedi gibi onu görünmez halatlarla çektiği için.",
                "Uzay-zaman çarşafı büküldüğü için aşağı yuvarlanır.",
                "Evrenakı denizinin devasa basıncı elmayı Dünya'nın kafasına doğru ittiği (Kütle-İtimi) için.",
                "Elektromanyetik çekim kuvvetinden dolayı."
            ],
            answer: 2,
            explain: "Harika! Fizikte (akışkanlarda) çekim yoktur; gezegen etrafındaki alçak basınca doğru yüksek basınçlı okyanusça itilme vardır."
        },
        {
            q: "3. Çift Yarık deneyinde o meşhur 'aynı anda iki yerden geçme' sihirbazlığının gerçek sebebi nedir?",
            options: [
                "Evrenin bilincimize tepki verip bizimle oyun oynaması.",
                "Işığın mermi (Zerre) olmaktan vazgeçip hayalet olması.",
                "Zerrenin tek delikten geçmesine rağmen, yarattığı V şeklindeki dalganın (Mach Konisinin) iki delikten birden geçip yolu çalkalandırması.",
                "Paralel evrenlerin çarpışması."
            ],
            answer: 2,
            explain: "Tebrikler! Ne büyü ne de kuantum mistisizmi. Sürat teknesinin kendisi tek delikten geçer, ama yarattığı köpük (dalga) her yere yayılır."
        },
        {
            q: "4. Galaksilerin dış yıldızlarının savrulmadan hızlı dönebilmesini sağlayan o 'Karanlık Madde' efsanesinin aslı nedir?",
            options: [
                "Henüz keşfedilmemiş gizli atom altı hayalet parçacıklar.",
                "Evrenakı denizinde oluşan devasa su girdabının (Makro-Vorteks) akıntısı.",
                "Kara deliğin sihirli kütleçekim dalgaları.",
                "Uzay-zaman çarşafının çok gergin olması."
            ],
            answer: 1,
            explain: "Kesinlikle doğru! Çay bardağındaki yaprakları çeviren şey çayın akıntısıdır. Evrende eksik bir madde (yalıtım bandı) yok, harika bir akışkan var!"
        }
    ];

    let currentIdx = 0;
    let score = 0;

    function renderQuestion() {
        const qObj = questions[currentIdx];
        const qText = document.getElementById('quiz-question');
        const optionsDiv = document.getElementById('quiz-options');
        const badge = document.getElementById('quiz-score-badge');
        const feedback = document.getElementById('quiz-feedback');
        const nextBtn = document.getElementById('quiz-next-btn');

        if (!qText || !optionsDiv) return;

        badge.textContent = `Soru ${currentIdx + 1} / ${questions.length}`;
        qText.textContent = qObj.q;
        optionsDiv.innerHTML = '';
        feedback.style.display = 'none';
        nextBtn.style.display = 'none';

        qObj.options.forEach((opt, idx) => {
            const btn = document.createElement('button');
            btn.className = 'btn btn-secondary';
            btn.style.cssText = 'text-align: left; justify-content: flex-start; padding: 12px 16px; font-size: 0.95rem; width: 100%; border: 1px solid #374151; border-radius: 8px; transition: all 0.2s; background: #1f2937; color: white; cursor: pointer;';
            btn.textContent = opt;
            btn.onclick = () => selectOption(idx);
            optionsDiv.appendChild(btn);
        });
    }

    function selectOption(selectedIdx) {
        const qObj = questions[currentIdx];
        const optionsDiv = document.getElementById('quiz-options');
        const feedback = document.getElementById('quiz-feedback');
        const nextBtn = document.getElementById('quiz-next-btn');
        const btns = optionsDiv.querySelectorAll('button');

        btns.forEach((btn, idx) => {
            btn.disabled = true;
            if (idx === qObj.answer) {
                btn.style.background = 'rgba(16, 185, 129, 0.15)';
                btn.style.borderColor = '#10b981';
                btn.style.color = '#34d399';
            } else if (idx === selectedIdx) {
                btn.style.background = 'rgba(239, 68, 68, 0.15)';
                btn.style.borderColor = '#ef4444';
                btn.style.color = '#f87171';
            }
        });

        if (selectedIdx === qObj.answer) {
            score++;
            feedback.style.background = 'rgba(16, 185, 129, 0.1)';
            feedback.style.border = '1px solid rgba(16, 185, 129, 0.3)';
            feedback.style.color = '#34d399';
            feedback.innerHTML = `<strong>🎉 Doğru!</strong> ${qObj.explain}`;
        } else {
            feedback.style.background = 'rgba(239, 68, 68, 0.1)';
            feedback.style.border = '1px solid rgba(239, 68, 68, 0.3)';
            feedback.style.color = '#f87171';
            feedback.innerHTML = `<strong>❌ Yanlış.</strong> ${qObj.explain}`;
        }
        feedback.style.display = 'block';
        nextBtn.style.display = 'inline-flex';
    }

    window.nextQuizQuestion = function() {
        currentIdx++;
        if (currentIdx < questions.length) {
            renderQuestion();
        } else {
            showResults();
        }
    };

    function showResults() {
        const body = document.getElementById('quiz-body');
        const badge = document.getElementById('quiz-score-badge');
        const nextBtn = document.getElementById('quiz-next-btn');
        if (nextBtn) nextBtn.style.display = 'none';

        badge.textContent = 'Test Tamamlandı!';

        let msg = '';
        if (score === questions.length) {
            msg = '🏆 <strong>Mükemmel! 4/4 Yaptınız.</strong> Karanlık Madde yalıtım bandını tamamen söktünüz. Evrenin akışkan mekaniğini çözdünüz!';
        } else if (score >= 2) {
            msg = '👍 <strong>Tebrikler! ' + score + '/4 Yaptınız.</strong> Yeni fiziğe oldukça hakimsiniz, sadece birkaç kuantum masalı aklınızı karıştırmış.';
        } else {
            msg = '📚 <strong>' + score + '/4 Yaptınız.</strong> Einstein ve kuantumcuların masalları sizi biraz etkilemiş. Popüler bölümleri tekrar gözden geçirebilirsiniz.';
        }

        body.innerHTML = `
            <div style="text-align: center; padding: 20px 0;">
                <div style="font-size: 4rem; margin-bottom: 10px;">🎓</div>
                <h4 style="color: #60a5fa; font-size: 1.5rem; margin-bottom: 12px;">Test Sonucunuz: ${score} / ${questions.length}</h4>
                <p style="color: #e5e7eb; font-size: 1.1rem; line-height: 1.6;">${msg}</p>
                <button class="btn btn-primary" style="margin-top: 20px; padding: 10px 20px; font-size: 1rem; border-radius: 8px; cursor: pointer;" onclick="location.reload()">Testi Yeniden Çöz</button>
            </div>
        `;
    }

    // Bekleme ile DOM yüklemesini garanti et
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => setTimeout(renderQuestion, 100));
    } else {
        setTimeout(renderQuestion, 100);
    }
})();
</script>

---

> [!TIP]
> Popüler bilimin ötesine geçmeye hazırsanız, bu sarsıcı teorinin tüm hidrodinamik denklemlerini, diferansiyel ispatlarını ve deney raporlarını incelemek için **[Akademik Sürüm Ana Menüsüne](#akademik_01_01)** geçebilirsiniz. Evrenakı denizine hoş geldiniz.
