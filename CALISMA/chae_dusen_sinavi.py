# -*- coding: utf-8 -*-
"""
CHAE DUSEN-EGRI SINAVI — M-49'un disk imzasi (87_ETKIN_YASA is 17)
Protokol: SINIF_CALISMASI/87_ETKIN_YASA/CHAE_DUSEN_PROTOKOL.md (kestiriciler ONCE yazildi).

VERI: Chae+2021b (ApJ 921,104; arXiv 2109.04745 kaynak tex'inden cikarildi):
  veri/_chae2021b_env.tsv  — tab:env, 109 galaksi, bagimsiz log(e_N,env) (LSS'den)
  veri/_chae2021b_fit.tsv  — tab:fit, 162 galaksi, egri-fitli e~ (yalniz H2'de gozlem tarafi)
  + SPARC rotmod (sinif klasorleri) — s_obs dogrudan olcumden.

Kurallar (protokolden):
  dis bolge: R >= (2/3) R_son; >=4 nokta. s_obs: agirlikli EKK logV~logR egimi.
  s_P: pencereli resmi denklem (P) ayni yaricaplarda; s_PE: P + M-49 W_dis,
  g_ext = 10^logeN_max * 1.2e-10 m/s^2 (yayinin a0 normalizasyonu).
  Guc kapisi: medyan|Delta s_MOND| >= medyan sigma_s  (MOND etkisi: nu(y+e)-ailesi).
  Birincil: rho_s[s_obs - s_P, logeN_max], iki yonlu perm p (10000, tohum 42).
  Ikincil:  rho_s[e~_fit, -s_P], tek yonlu pozitif.

Cikti: SINIF_CALISMASI/87_ETKIN_YASA/SONUC_CHAE_DUSEN.csv
"""
import os, sys, io, csv, glob, math, warnings
import numpy as np
from scipy.stats import spearmanr

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

KOK = os.path.dirname(os.path.abspath(__file__))
SK = os.path.join(KOK, 'SINIF_CALISMASI')
G = 4.300917e-6
ACC = 1e6 / 3.0856776e19
A0 = 1.75 * 1.038 * (2.99792458e8 * (70e3 / 3.0857e22)) / ACC / 16.1   # resmi (km/s)^2/kpc
A0_MOND_SI = 1.2e-10                    # Chae normalizasyonu (yalniz e_N cevirisi + AQUAL kiyasi)
RB, UPS = 1.4, 0.50
AD = ['01_erken_spiral', '02_orta_spiral', '03_gec_spiral', '04_cok_gec_spiral',
      '05_macellan', '06_duzensiz']

# ---- rotmod ----
GAL = {}
for sn in AD:
    for f in sorted(glob.glob(os.path.join(SK, sn, 'veri', '*_rotmod.dat'))):
        d = np.loadtxt(f)
        R, Vo, eV, Vg, Vd, Vb = [d[:, i] for i in range(6)]
        eV = np.maximum(eV, 1.0)
        Rp = R * 1e3
        SBd, SBb = d[:, 6], d[:, 7]
        L = lambda S: np.concatenate([[0.0], np.cumsum(
            np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * 0.5 * (S[1:] + S[:-1]))])
        vb2 = np.sign(Vg) * Vg ** 2 + UPS * Vd ** 2 + RB * UPS * Vb ** 2
        Mk = UPS * L(SBd) + RB * UPS * L(SBb) + np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.0)
        GAL[os.path.basename(f)[:-11]] = dict(R=R, Vo=Vo, eV=eV, vb2=vb2, Mk=Mk)

# ---- Chae tablolari ----
def tsv(ad):
    r = list(csv.DictReader(io.open(os.path.join(KOK, 'veri', ad), encoding='utf-8'),
                            delimiter='\t'))
    return {x['galaxy']: x for x in r}

ENV = tsv('_chae2021b_env.tsv')
FIT = tsv('_chae2021b_fit.tsv')

# ---- egim kestiricileri ----
def egim_w(lx, ly, sy):
    w = 1.0 / np.maximum(sy, 1e-4) ** 2
    W = w.sum(); mx = (w * lx).sum() / W; my = (w * ly).sum() / W
    s = (w * (lx - mx) * (ly - my)).sum() / (w * (lx - mx) ** 2).sum()
    se = math.sqrt(1.0 / (w * (lx - mx) ** 2).sum())
    return s, se

def egim(lx, ly):
    return float(np.polyfit(lx, ly, 1)[0])

def v2P(g, m, gext=None):
    """pencereli resmi denklem; gext verilirse M-49 W_dis eklenir ((km/s)^2/kpc)."""
    R, vb2, Mk = g['R'][m], g['vb2'][m], np.maximum(g['Mk'][m], 1e-9)
    gk = G * Mk / R ** 2
    W = np.minimum(1.0, A0 / gk)
    if gext is not None:
        W = W * np.minimum(1.0, np.sqrt(gk / max(gext, 1e-12)))
    return np.maximum(vb2 + np.sqrt(G * Mk * A0) * W, 1e-9)

def nu_eN(y, eN):
    """Chae+2021b eq. (2) — AQUAL 1B'nin e_N'li STANDART bicimi (protokolun kastettigi).

    DUZELTME KAYDI: ilk kosumda kaba nu(y+e) kullanilmisti; protokol metni 'e_N'li
    standart bicim' der — o bicim budur. Duzeltme, ilk kosumun sayilari gorulmus
    HALDEYKEN yapildi; surec lekesi SONUC bolumune islenir."""
    aeN = abs(eN)
    C = math.sqrt(1.0 + aeN / 4.0)
    D = 1.0 + aeN / y
    return 0.5 + np.sqrt(D * D / 4.0 + D / y) - (eN / math.sqrt(aeN) if aeN > 0 else 0.0) * C / y

SAT, S = [], []
for ad, g in sorted(GAL.items()):
    if ad not in ENV or ad not in FIT:
        continue
    m = g['R'] >= (2.0 / 3.0) * g['R'][-1]
    if m.sum() < 4 or np.any(g['vb2'][m] <= 0):
        continue
    lR = np.log10(g['R'][m]); lV = np.log10(g['Vo'][m])
    sV = g['eV'][m] / (g['Vo'][m] * math.log(10))
    s_obs, se = egim_w(lR, lV, sV)
    leN = float(ENV[ad]['logeN_max']); leN_no = float(ENV[ad]['logeN_no'])
    gext = 10 ** leN * A0_MOND_SI / ACC              # (km/s)^2/kpc
    s_P = egim(lR, 0.5 * np.log10(v2P(g, m)))
    s_PE = egim(lR, 0.5 * np.log10(v2P(g, m, gext)))
    # MOND etki buyuklugu (guc kapisi): eq. nueN — standart AQUAL 1B bicimi
    gb = np.maximum(g['vb2'][m], 1e-9) / g['R'][m] * ACC / A0_MOND_SI
    e = 10 ** leN
    sM0 = egim(lR, 0.5 * np.log10(gb * nu_eN(gb, 0.0) * A0_MOND_SI / ACC * g['R'][m]))
    sM1 = egim(lR, 0.5 * np.log10(gb * nu_eN(gb, e) * A0_MOND_SI / ACC * g['R'][m]))
    Wd = np.minimum(1.0, np.sqrt((G * np.maximum(g['Mk'][m], 1e-9) / g['R'][m] ** 2) / gext))
    et = float(FIT[ad]['et'])
    S.append(dict(ad=ad, s_obs=s_obs, se=se, s_P=s_P, s_PE=s_PE, leN=leN, leN_no=leN_no,
                  dM=sM1 - sM0, et=et, Wd=float(Wd.min()), n=int(m.sum())))
    SAT.append([ad, m.sum(), '%.3f' % s_obs, '%.3f' % se, '%.3f' % s_P, '%.3f' % s_PE,
                '%.3f' % leN, '%.4f' % (sM1 - sM0), '%.3f' % et, '%.3f' % Wd.min()])

yol = os.path.join(SK, '87_ETKIN_YASA', 'SONUC_CHAE_DUSEN.csv')
with io.open(yol, 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['galaksi', 'n_dis', 's_obs', 'se', 's_P', 's_PE', 'logeN_max',
                'dSlope_MOND', 'et_fit', 'W_dis_min'])
    for s in SAT:
        w.writerow(s)

n = len(S)
print('KAPI 2 — orneklem: n=%d (esik 40): %s' % (n, 'GECTI' if n >= 40 else 'KALDI'))
dM = np.array([abs(x['dM']) for x in S]); sig = np.array([x['se'] for x in S])
print('KAPI 3 — guc: medyan|dS_MOND|=%.4f, medyan sigma_s=%.4f -> %s'
      % (np.median(dM), np.median(sig),
         'GECTI' if np.median(dM) >= np.median(sig) else 'KALDI (birincil uygulanamaz)'))
print('  W_dis<1 galaksi sayisi (teorinin etki bekledigi): %d/%d'
      % (sum(1 for x in S if x['Wd'] < 1), n))

rng = np.random.default_rng(42)
def perm_p(a, b, tek_yonlu_poz=False):
    r0 = spearmanr(a, b).statistic
    cnt = 0
    bb = np.array(b)
    for _ in range(10000):
        rp = spearmanr(a, rng.permutation(bb)).statistic
        if tek_yonlu_poz:
            cnt += (rp >= r0)
        else:
            cnt += (abs(rp) >= abs(r0))
    return r0, cnt / 10000.0

art = np.array([x['s_obs'] - x['s_P'] for x in S])
leN = np.array([x['leN'] for x in S])
r1, p1 = perm_p(art, leN)
print('\nBIRINCIL: rho_s[s_obs - s_P, logeN_max] = %+.3f · iki yonlu perm p = %.4f' % (r1, p1))
leNn = np.array([x['leN_no'] for x in S])
r1n, p1n = perm_p(art, leNn)
print('  duyarlilik (no clustering): rho = %+.3f · p = %.4f' % (r1n, p1n))

et = np.array([x['et'] for x in S]); mSP = np.array([-x['s_P'] for x in S])
r2, p2 = perm_p(et, mSP, tek_yonlu_poz=True)
print('IKINCIL: rho_s[e~_fit, -s_P] = %+.3f · tek yonlu perm p = %.4f' % (r2, p2))

print('\nBETIMLEYICI: medyan(s_obs-s_P) = %+.4f · medyan(s_obs-s_PE) = %+.4f'
      % (np.median(art), np.median([x['s_obs'] - x['s_PE'] for x in S])))
print('  medyan s_obs %+.3f · medyan s_P %+.3f' % (np.median([x['s_obs'] for x in S]),
                                                    np.median([x['s_P'] for x in S])))
ek = np.array([x['et'] for x in S])
et_env = math.sqrt(10 ** np.median(leN))          # e~_env = sqrt(e_N,env) — yayinin tanimi
print('  e~_fit medyani %.3f · e~_env medyani %.3f (ayni olcek: e~=sqrt(e_N); '
      'Paper II uyum iddiasinin bu altkumede gorunumu)' % (np.median(ek), et_env))
# HUKUM-DISI post-hoc: e~_fit gercek dis egimi izliyor mu? (yorum icin)
r3, p3 = perm_p(ek, np.array([-x['s_obs'] for x in S]), tek_yonlu_poz=True)
print('  [post-hoc, hukum disi] rho_s[e~_fit, -s_obs] = %+.3f · p = %.4f' % (r3, p3))
