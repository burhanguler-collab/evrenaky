# -*- coding: utf-8 -*-
"""
EFE kayit-oncesi sinavi — 87_ETKIN_YASA/EFE_PROTOKOL.md'nin kosumu.

Protokol kilitleri (veriye bakilmadan once yazildi):
  H1: rho_s[log k, log e_env] < 0 (tek yonlu)
  Birincil: Spearman + permutasyon p (10000, tohum 42)
  Ikincil (ayirici): kismi Spearman | (v/sigma, log M_bar, tip)
     - v/sigma yalniz 18 galakside var (85/VSIGMA.csv): tam kontrol o altkumede,
       genis orneklemde kontrol (log M_bar, tip) ile yapilir ve sinirlilik kaydedilir.
  Kapilar: (1) e_env bagimsizligi (Desmond 2018 buyuk-olcek hesabi — literatur kaydi)
           (2) eslesen n >= 40   (3) e_env dinamik araligi >= 1 dex

Girdiler:
  k     : SINIF_CALISMASI/94_YEREL_LOMEGA/SONUC.csv  (B_carpan — yerel/nihai kurulum, kayitli)
  e_env : SINIF_CALISMASI/87_ETKIN_YASA/veri_chae2021_tablo2.txt
          (Chae ve ark. 2020, ApJ 904, 51 — ERRATUM ile duzeltilmis Tablo 2:
           Chae ve ark. 2021, ApJ 910, 81, DOI 10.3847/1538-4357/abebdc;
           IOP suppdata apjabebdct1_ascii.txt. Orijinal tablodaki e_env eslesme
           hatasi nedeniyle YALNIZ duzeltilmis tablo kullanilir.)
  M_bar, tip : veri/_sparc.mrt  (M_bar = 0.5*L36 + 1.33*MHI, 1e9 Msun)
  v/sigma    : SINIF_CALISMASI/85_TUTARLILIK_YASASI/VSIGMA.csv (n=18)

Cikti: SINIF_CALISMASI/87_ETKIN_YASA/SONUC_EFE.csv + stdout ozeti.
"""
import csv, io, math, os, random, re

B = os.path.dirname(os.path.abspath(__file__))
P87 = os.path.join(B, 'SINIF_CALISMASI', '87_ETKIN_YASA')

# ---------- 1) girdiler ----------
def norm(ad):
    return ad.replace(' ', '').replace('^a', '').strip()

k94 = {}
with io.open(os.path.join(B, 'SINIF_CALISMASI', '94_YEREL_LOMEGA', 'SONUC.csv'), encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        k94[norm(r['Galaksi'])] = float(r['B_carpan'])

eenv = {}
rx = re.compile(r'\$(-?)\{([0-9.]+)\}')
with io.open(os.path.join(P87, 'veri_chae2021_tablo2.txt'), encoding='utf-8', errors='replace') as f:
    for line in f:
        p = line.rstrip('\n').split('\t')
        if len(p) < 9 or p[0].startswith(('Table', 'Galaxy', 'Notes', '^')):
            continue
        m = rx.match(p[3].strip())
        if not m:
            continue
        val = float(m.group(2)) * (-1 if m.group(1) else 1)
        eenv[norm(p[0])] = val

mbar, tip = {}, {}
with io.open(os.path.join(B, 'veri', '_sparc.mrt'), encoding='utf-8', errors='replace') as f:
    # dosyanin veri bloklari bosluk-ayrimlidir (adlar tek belirtec):
    # ad T D e_D f_D Inc e_Inc L36 e_L36 Reff SBeff Rdisk SBdisk MHI RHI Vflat e_Vflat Q Ref
    for line in f:
        p = line.split()
        if len(p) < 18:
            continue
        try:
            T = int(p[1]); L36 = float(p[7]); MHI = float(p[13])
        except ValueError:
            continue
        mbar[norm(p[0])] = 0.5 * L36 + 1.33 * MHI
        tip[norm(p[0])] = T

vsig = {}
with io.open(os.path.join(B, 'SINIF_CALISMASI', '85_TUTARLILIK_YASASI', 'VSIGMA.csv'), encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        vsig[norm(r['galaksi'])] = float(r['v_sigma'])

# ---------- 2) eslestirme + kapilar ----------
ortak = sorted(set(k94) & set(eenv) & set(mbar))
n = len(ortak)
ev = [eenv[g] for g in ortak]
poz = [e for e in ev if e > 0]
aralik_dex = math.log10(max(poz) / min(poz))
print('eslesen n = %d (k:141, e_env:%d)' % (n, len(eenv)))
print('KAPI 2 (n>=40): %s' % ('GECTI' if n >= 40 else 'KALDI'))
print('KAPI 3 (e_env araligi >= 1 dex): %.2f dex -> %s' % (aralik_dex, 'GECTI' if aralik_dex >= 1 else 'KALDI'))
negatif_e = [g for g in ortak if eenv[g] <= 0]
if negatif_e:
    print('  not: e_env<=0 olan %d galaksi log icin dusuruldu: %s' % (len(negatif_e), negatif_e))
ortak = [g for g in ortak if eenv[g] > 0]
n = len(ortak)

# ---------- 3) yardimcilar ----------
def rankla(x):
    sirali = sorted(range(len(x)), key=lambda i: x[i])
    r = [0.0] * len(x); i = 0
    while i < len(x):
        j = i
        while j + 1 < len(x) and x[sirali[j + 1]] == x[sirali[i]]:
            j += 1
        ort = (i + j) / 2.0 + 1
        for t in range(i, j + 1):
            r[sirali[t]] = ort
        i = j + 1
    return r

def pearson(a, b):
    na = len(a); ma = sum(a) / na; mb = sum(b) / na
    ca = [x - ma for x in a]; cb = [x - mb for x in b]
    pay = sum(x * y for x, y in zip(ca, cb))
    payda = math.sqrt(sum(x * x for x in ca) * sum(y * y for y in cb))
    return pay / payda if payda else 0.0

def spearman(a, b):
    return pearson(rankla(a), rankla(b))

def artik(y, Xs):
    # y'den Xs kolonlarini (coklu dogrusal) dus — Gram-Schmidt ile
    ort = [list(c) for c in Xs]
    for i in range(len(ort)):
        for j in range(i):
            pj = sum(a * b for a, b in zip(ort[i], ort[j])) / sum(b * b for b in ort[j])
            ort[i] = [a - pj * b for a, b in zip(ort[i], ort[j])]
    res = list(y)
    m = sum(res) / len(res); res = [v - m for v in res]
    for c in ort:
        mc = sum(c) / len(c); c0 = [v - mc for v in c]
        den = sum(v * v for v in c0)
        if den == 0: continue
        p = sum(a * b for a, b in zip(res, c0)) / den
        res = [a - p * b for a, b in zip(res, c0)]
    return res

def kismi_spearman(a, b, kontrols):
    ra, rb = rankla(a), rankla(b)
    rk = [rankla(c) for c in kontrols]
    return pearson(artik(ra, rk), artik(rb, rk))

# ---------- 4) birincil sinav ----------
lk = [math.log10(k94[g]) for g in ortak]
le = [math.log10(eenv[g]) for g in ortak]
rho = spearman(lk, le)
random.seed(42)
NP = 10000; asiri = 0
kopya = lk[:]
for _ in range(NP):
    random.shuffle(kopya)
    if spearman(kopya, le) <= rho:
        asiri += 1
p_tek = asiri / NP  # H1 negatif yonlu
print('\nBIRINCIL: Spearman rho[log k, log e_env] = %+.3f  (n=%d)' % (rho, n))
print('tek yonlu permutasyon p (H1: negatif) = %.4f  [10000 perm, tohum 42]' % p_tek)

# ---------- 5) ikincil (ayirici) ----------
lm = [math.log10(mbar[g]) for g in ortak]
tt = [float(tip[g]) for g in ortak]
rho_k1 = kismi_spearman(lk, le, [lm, tt])
print('\nIKINCIL A (genis orneklem, kontrol: log M_bar + tip): kismi rho = %+.3f' % rho_k1)

alt = [g for g in ortak if g in vsig]
if len(alt) >= 8:
    lka = [math.log10(k94[g]) for g in alt]
    lea = [math.log10(eenv[g]) for g in alt]
    vsa = [vsig[g] for g in alt]
    lma = [math.log10(mbar[g]) for g in alt]
    rho_ham_alt = spearman(lka, lea)
    rho_k2 = kismi_spearman(lka, lea, [vsa, lma])
    print('IKINCIL B (v/sigma altkumesi, n=%d): ham rho = %+.3f -> kismi (v/sigma, logMbar) = %+.3f' % (len(alt), rho_ham_alt, rho_k2))
else:
    print('IKINCIL B: v/sigma altkumesi cok kucuk (n=%d) — kosulmadi' % len(alt))

# ---------- 6) cikti ----------
yol = os.path.join(P87, 'SONUC_EFE.csv')
with io.open(yol, 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Galaksi', 'k_94B', 'e_env_duzeltilmis', 'logMbar_1e9', 'Tip_T', 'v_sigma'])
    for g in ortak:
        w.writerow([g, '%.4f' % k94[g], '%.4f' % eenv[g], '%.3f' % math.log10(mbar[g]),
                    tip[g], '%.2f' % vsig[g] if g in vsig else ''])
print('\nyazildi: %s' % yol)
