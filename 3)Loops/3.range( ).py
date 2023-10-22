#range() Fonksiyonu
"""
Bu yapı başlangıç, bitiş ve opsiyonel olarak artırma değeri alarak listelere benzeyen bir sayı dizisi oluşturur
"""

# Yazdırmak için başına "*" koymamız gerekiyor.
print(*range(0,20))

# list fonksiyonuyla listeye dönüştürülebilir.
liste = list(range(0,20))
print(liste)

print(*range(5,10))
print(*range(15)) # Başlangıç değeri vermediğimiz 0'dan başlar
print(*range(5,20,2)) # 5'ten 20'ye kadar olan sayıları 2 atlayarak oluşturur.
print(*range(5,100,5)) # 5'ten 100'e kadar olan ve 5 ile bölünebilen sayılar
print(*range(20,0,-1)) # 20'den geri gelen sayıları oluşturur.


for sayı in range(0,10):
    print(sayı)

for sayı in range(1,20):
    print("* " * sayı)