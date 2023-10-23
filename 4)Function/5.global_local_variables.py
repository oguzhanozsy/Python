a = 5  # Global isim alanında bir değişken .
def fonksiyon():
    print(a)  # a değişkeni globalde tanımlandığı için burada tanımlı.
fonksiyon()


c = 10 # Globalde tanımlanmış bir değişken
def fonksiyon():
    c = 2 # Yerelde tanımlanmış bir değişken
    print(c)  # Yerel değişken kullanılıyor.

fonksiyon()
print(c)

#GLOBAL DEYİMİ
"""Peki bir fonksiyonda globalde tanımlanmış bir değişkeni nasıl kullanacağız ?
Bunun için Pythonda global ifadesi bulunmaktadır
"""

d = 10
def fonksiyon():
    global d
    d = 4
    print(d)
fonksiyon()
print(d)

"""
 if ve while bloklarında tanımlanan değişkenler 
 yerel bir değişken yerine global bir değişken olmaktadır.
"""

if True:
    t = 10
    print(t)
print(t)

while True:
    deger =  10
    print(deger)
    break
print(deger)

