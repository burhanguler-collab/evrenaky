import math

# Sabitler
G = 6.67430e-11 # m^3/kg/s^2
M_E = 5.9722e24 # kg
M_M = 7.342e22  # kg
R_E = 6371e3    # m
R_M = 1737e3    # m
r = 384400e3    # m

# Yarı-küre kütle merkezleri
d_E = (3/8) * R_E
d_M = (3/8) * R_M

m_E_half = M_E / 2
m_M_half = M_M / 2

# Klasik Noktasal Kuvvet
F_classic = G * M_E * M_M / (r**2)
F_half_classic = F_classic / 2  # Her bir yarı kürenin kütle merkezinde hissetmesi gereken teorik kuvvet

print("=== KLASİK GELGİT (DİFERANSİYEL) KUVVET HESABI ===\n")
print(f"Klasik Toplam Çekim: {F_classic:.5e} N")
print(f"Yarı-küre Başına Düşen Merkezcil Kuvvet (F_merkez): {F_half_classic:.5e} N\n")

# 1. DÜNYA İKİYE BÖLÜNMÜŞ DURUM
r_front_E = r - d_E
r_back_E = r + d_E

F_E_front_gercek = G * M_M * m_E_half / (r_front_E**2)
F_E_back_gercek  = G * M_M * m_E_half / (r_back_E**2)

# Diferansiyel (Tidal) Kuvvetler (Gerçek Kuvvet - Merkezcil Kuvvet)
F_E_front_tidal = F_E_front_gercek - F_half_classic
F_E_back_tidal  = F_E_back_gercek - F_half_classic
F_E_toplam_tidal = F_E_front_tidal + F_E_back_tidal

print("--- 1. DÜNYA İÇİN DİFERANSİYEL (TİDAL) KUVVETLER ---")
print(f"Ön Yarıya Etkiyen Net Diferansiyel Kuvvet:  +{F_E_front_tidal:.5e} N (Ay'a Doğru)")
print(f"Arka Yarıya Etkiyen Net Diferansiyel Kuvvet: {F_E_back_tidal:.5e} N (Ay'dan Uzağa / Negatif)")
print(f"İki Yarının Diferansiyel Toplamı:          +{F_E_toplam_tidal:.5e} N (Sıfıra Çok Yakın)")
print(f"Kıyaslama: Toplam Diferansiyel Kuvvet, Klasik Kuvvetin SADECE %{(F_E_toplam_tidal/F_classic)*100:.6f}'sidir.\n")

# 2. AY İKİYE BÖLÜNMÜŞ DURUM
r_front_M = r - d_M
r_back_M = r + d_M

F_M_front_gercek = G * M_E * m_M_half / (r_front_M**2)
F_M_back_gercek  = G * M_E * m_M_half / (r_back_M**2)

F_M_front_tidal = F_M_front_gercek - F_half_classic
F_M_back_tidal  = F_M_back_gercek - F_half_classic
F_M_toplam_tidal = F_M_front_tidal + F_M_back_tidal

print("--- 2. AY İÇİN DİFERANSİYEL (TİDAL) KUVVETLER ---")
print(f"Ön Yarıya Etkiyen Net Diferansiyel Kuvvet:  +{F_M_front_tidal:.5e} N (Dünya'ya Doğru)")
print(f"Arka Yarıya Etkiyen Net Diferansiyel Kuvvet: {F_M_back_tidal:.5e} N (Dünya'dan Uzağa / Negatif)")
print(f"İki Yarının Diferansiyel Toplamı:          +{F_M_toplam_tidal:.5e} N (Sıfıra Çok Yakın)")
print(f"Kıyaslama: Toplam Diferansiyel Kuvvet, Klasik Kuvvetin SADECE %{(F_M_toplam_tidal/F_classic)*100:.6f}'sidir.\n")
