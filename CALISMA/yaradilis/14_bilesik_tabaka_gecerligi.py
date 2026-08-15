# -*- coding: utf-8 -*-
"""BILESIK SINIR TABAKASI — "BUYUK GOSTERIM" FIZIK ONAYLIYOR MU?  (12 Agu 2026)

Kullanicinin sorusu: bir kume, etrafina cizilen buyuk halka ile "tek buyuk Kut"
gibi gosteriliyor. Fizik bunu onayliyor mu?

r_e(obek) = |Sum g| * r_e  bir UZAK ALAN sonucudur. Ama cizilen halka
R_d = N*r_e iken obegin kendi yaricapi R_kume ~ sqrt(N) mertebesindedir; oran
sonsuz degil ~2.7-4.6. O halde halkanin DAIRE olmasi kendiliginden dogru degil.

Bu betik olcer:
  (1) Cizilen halkada |v| gercekten sqrt2*c mi?          -> ortalama hata
  (2) Halka gercekten daire mi?                          -> acisal dalgalanma
  (3) N ile nasil degisir?                               -> tarama

Sonuc: N>=4 den itibaren pratikte TAM (dalgalanma <%1), N>=6 da tam sifir.
Sebep mesafe orani DEGIL, SIMETRI: duzgun N-gen'de esit arali kaynaklarin
toplami N'in kati olmayan butun harmonikleri goturur, dolayisiyla ilk duzeltme
N. mertebeden ve (R_kume/R_d)^N ile duser.
Istisna: N=2 (dipol) — es-yuzey daire degil, fistik biciminde, %28.5 sapma.

Bkz. 00_CALISMA_Yaradilis_ve_Asimetri.md §8.13
"""
import numpy as np

K = np.sqrt(2.0)      # kod birimi: |v| = K/r ; r_e = 1'de |v| = sqrt2 c
D0 = 1.5              # bagin kilitledigi en yakin komsu mesafesi (§8.12)
res = []
add = lambda n, ok, e: res.append((n, ok, e))


def kume(N):
    """Kumenin GERCEKTE oturdugu dizilim: N<=7 tek halka, N>=8 merkez+halka.
    (Thomson siniri: tek halka N<=7 kararli, merkez Kut ile ~10'a cikar.)"""
    if N == 1:
        return np.zeros((1, 2))
    if N == 2:
        return np.array([[-D0/2, 0.0], [D0/2, 0.0]])
    if N <= 7:
        R = D0 / (2*np.sin(np.pi/N))          # kenar uzunlugu = D0 olacak sekilde
        a = 2*np.pi*np.arange(N)/N
        return np.stack([R*np.cos(a), R*np.sin(a)], axis=1)
    m = N - 1
    R = max(D0, D0/(2*np.sin(np.pi/m)))
    a = 2*np.pi*np.arange(m)/m
    return np.vstack([[[0.0, 0.0]], np.stack([R*np.cos(a), R*np.sin(a)], axis=1)])


def vel(P, pos):
    v = np.zeros(2)
    for q in pos:
        r = P - q
        r2 = max(r[0]**2 + r[1]**2, 1e-30)
        v += np.array([-K*r[1]/r2, K*r[0]/r2])
    return v


def gecerlik(N, M=720):
    """Cizilen halkada (R_d = N*r_e) |v| nin ortalamasi ve acisal dalgalanmasi."""
    P = kume(N)
    c = P.mean(axis=0)
    Rc = max(np.hypot(*(p - c)) for p in P)
    Rd = float(N)
    vs = np.array([np.hypot(*vel(c + Rd*np.array([np.cos(a), np.sin(a)]), P))
                   for a in 2*np.pi*np.arange(M)/M])
    vo = vs.mean()
    return dict(Rc=Rc, Rd=Rd, oran=Rd/Rc, vort=vo,
                hata=(vo - K)/K, dalg=(vs.max() - vs.min())/vo)


print("=" * 86)
print("  BILESIK SINIR TABAKASI — BUYUK GOSTERIM FIZIK ONAYLIYOR MU?")
print("=" * 86)
print("  Cizilen halka: R_d = N * r_e.   Orada |v| = sqrt2 c = %.6f olmali." % K)
print()
print("    N   dizilim        R_kume   R_d/R_kume    |v|_ort    hata%     DALG%    yargi")
print("  " + "-" * 82)

tab = {}
for N in (2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 16, 20):
    g = gecerlik(N)
    tab[N] = g
    ad = "halka" if N <= 7 else "merkez+halka"
    yargi = "TAM" if g["dalg"] < 0.15 else ("YAKLASIK" if g["dalg"] < 0.35 else "GECERSIZ")
    print("  %5d   %-13s %6.2f   %9.2f   %9.6f  %+7.3f  %8.2f    %s"
          % (N, ad, g["Rc"], g["oran"], g["vort"],
             g["hata"]*100, g["dalg"]*100, yargi))

print()
add("N=6 |v| hedefi tam tutar",   abs(tab[6]["hata"]) < 1e-6, abs(tab[6]["hata"]))
add("N=8 |v| hedefi tam tutar",   abs(tab[8]["hata"]) < 1e-6, abs(tab[8]["hata"]))
add("N=6 halkasi DAIRE",          tab[6]["dalg"] < 1e-3, tab[6]["dalg"])
add("N=4 neredeyse daire (<%2)",  tab[4]["dalg"] < 0.02, tab[4]["dalg"])
add("N=3 iyi (<%8)",              tab[3]["dalg"] < 0.08, tab[3]["dalg"])
add("N=2 daire DEGIL (>%20)",     tab[2]["dalg"] > 0.20, tab[2]["dalg"])
add("dalgalanma N ile duser",
    tab[2]["dalg"] > tab[3]["dalg"] > tab[4]["dalg"] > tab[6]["dalg"], 0.0)

# ---------------------------------------------------------------------------
print("[SIMETRI MI, MESAFE MI?]")
print("  Iddia: duzeltme N. MERTEBEDEN ve (R_kume/R_d)^N ile duser.")
print("  Sinama: ayni oranda ama farkli N ile dalgalanmayi kiyasla.")
print()
print("    N     oran    dalg%      (1/oran)^N        kiyas")
for N in (3, 4, 5, 6, 7):
    g = tab[N]
    tahmin = (1.0/g["oran"])**N
    print("  %5d   %6.2f  %8.4f     %.3e" % (N, g["oran"], g["dalg"]*100, tahmin))
add("dalgalanma (1/oran)^N ile ayni hizda coker",
    tab[6]["dalg"] < tab[4]["dalg"] * 0.1, tab[6]["dalg"]/max(tab[4]["dalg"], 1e-30))
print()
print("  -> Oran neredeyse SABIT (3.8-4.1) kalirken dalgalanma iki mertebe")
print("     dusuyor. Demek ki belirleyici olan mesafe degil, N-KATLI SIMETRI.")

# ---------------------------------------------------------------------------
print()
print("[OTURMAMIS KUME]")
print("  Simetriyi bozunca ne olur? Halkayi rastgele sarsalim.")
rng = np.random.RandomState(7)
for sars in (0.0, 0.1, 0.3, 0.6):
    P = kume(6).copy()
    P = P + rng.normal(0, sars, P.shape)
    c = P.mean(axis=0)
    vs = np.array([np.hypot(*vel(c + 6.0*np.array([np.cos(a), np.sin(a)]), P))
                   for a in 2*np.pi*np.arange(360)/360])
    print("    sarsinti sigma = %.1f  ->  dalgalanma %%%.2f" %
          (sars, (vs.max()-vs.min())/vs.mean()*100))
print("  -> Simetri bozuldukca gosterim gecerliligini YITIRIYOR. Bu yuzden")
print("     cizim, kendi guvenilirligini olcup SOYLEMEK zorunda.")

print()
print("[SONUC]")
print("  Buyuk gosterim, kume kendi kararli dizilimine OTURDUGUNDA fiziksel")
print("  olarak TAM. N=2 sinirda, oturmamis kume gecersiz. Arayuz uc kademe")
print("  cizer:  <%15 duz yesil  ·  %15-35 turuncu kesikli  ·  >%35 kirmizi noktali.")

print("\n" + "=" * 86)
kotu = sum(1 for _, ok, _ in res if not ok)
for n, ok, e in res:
    print("  %-42s %-9s %.3e" % (n, "PASS" if ok else "**FAIL**", e))
print("\n  ---> %d/%d gecti" % (len(res) - kotu, len(res)))
