# Değişken ismi ve Değişkenin Değeri
i = 10
print(i)

# pytonda C deki gibi önceden veri tipinin şeklini söylemeye gerek yoktur kendisi otomatik algılar...
i = 3.4
print(i)

print(i * i * i)

a = 4
b = 3
c = a + 2 * b
print(c)


# 1. Değişken isimleri bir sayı ile başlayamaz.
# 2. Değişken ismi kelimelerden oluşuyorsa aralarında boşluk olamaz.
# 3. :'",<>/?|\()!@#$%^&*~-+ Buradaki semboller değişken ismi içinde kullanılamaz.(Sadece _ sembolü kullanılabilir)
# 4. Pythonda tanımlı anahtar kelimeler değişken ismi olarak kullanılamaz.(while, not vs. )

#EXAMPLE
pi_sayisi = 3.14
cap = 4
cevre = pi_sayisi * cap
print(cevre)

#İKİ SAYININ YERİNİ DEĞİŞTİRME
a = 4
b = 3
print(a,b)

a,b = b,a
print(a,b)

#SAYININ DEĞERİNİ ARTTIRMA
a = 5
print(a)

a += 1
print(a)

#TEKLİ YORUM SATIRI
"""
ÇOKLU YORUM SATIRI
"""
