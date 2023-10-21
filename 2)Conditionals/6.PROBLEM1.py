"""
Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
"""

kilo = int(input("Kilonuzu Giriniz:"))
boy = float(input("Boyunuzu Giriniz:"))

bki = kilo / (boy * boy)

if (bki > 30) :
    print("OBEZSİNİZ...")
elif (bki > 25 and bki <= 30) :
    print("KİLONUZ FAZLA...")
elif (bki > 18.5 and bki <= 25) :
    print("KİLONUZ NORMAL...")
else :
    print("ZAYIFSINIZ...")