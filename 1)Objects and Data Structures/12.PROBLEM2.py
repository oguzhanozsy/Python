"""

Kullanıcıdan aldığınız boy ve kilo değerlerine
göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

"""

kilo = int(input("Kilo:"))
boy = float(input("Boy:"))

bki = (kilo) / (boy * boy)

print("BEDEN KİTLE İNDEKSİ: ",bki)