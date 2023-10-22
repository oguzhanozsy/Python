# in Operatörü
# Pythondaki in operatörü , bir elemanın başka bir listede,demette veya stringte (karakter dizileri) bulunup bulunmadığını kontrol eder.

print("a" in "merhaba")
print("mer" in "merhaba")
print("t" in "merhaba")
print(4 in [1,2,3,4])
print(10 in [1,2,3,4])
print(4 in (1,2,3))

# for Döngüsü

"""
for Döngüsü , listelerin ,demetlerin, stringlerin ve hatta sözlüklerin üzerinde dolaşmamızı sağlayan bir döngü türüdür. Yapısı şu şekildedir.

        for eleman in veri_yapısı(liste,demet vs):
            Yapılacak İşlemler
Bu yapı bize şunu söyler;

        eleman değişkeni her döngünün başında listenin,demetin vs. her bir elemanına eşit olacak ve her döngüde 
        bu elemanla işlem yapılacak.
"""

#LİSTELER ÜZERİNDE GEZİNMEK

liste = [1,2,3,4,5,6,7]
for eleman in liste:
    print("Eleman",eleman)

# Liste elemanlarını toplama

liste = [1,2,3,4,5,6,7]
toplam = 0
for eleman in liste:
    toplam += eleman
print("Toplam:",toplam)

#Çift Elemanları Bastırma

liste = [12,3,4,5,6,7,83,22,31,44,66]
for eleman in liste:
    if eleman % 2 == 0:
        print(eleman)


#KARAKTER DİZİLERİ ÜZERİNDE GEZİNMEK(STRİNGLER)
s = "Python"
for karakter in s:
    print(karakter)

# Her bir karakterleri 3 ile çarp
s = "Python"
for karakter in s:
    print(karakter * 3)

#DEMETLER ÜZERİNDE GEZİNMEK(Demetler)
# Listelerle aynı mantık
demet = (1,2,3,4,5,6,7)
for eleman in demet:
    print(eleman)

#Listelerin için 2 boyutlu demetler
liste = [(1,2),(3,4),(5,6),(7,8)]
for eleman in liste:
    print(eleman) #Herbir elemanın demet olduğunu görebiliyoruz

# Demet içindeki herbir elemanı almak için pratik yöntem
liste = [(1,2),(3,4),(5,6),(7,8)]
for (i,j) in liste:
    print("i:{} j:{}".format(i,j))


#Demet içindeki elemanları çarpma
liste = [(1,2,3),(4,5,6),(7,8,9,),(10,11,12)]
for (i,j,k) in liste:
    print(i * j * k)




#SÖZLÜKLER ÜZERİNDE GEZİNMEK(Dictionary)

#Metodları kullanmadan sözlük üzerinde gezinmek - Sadece anahtarları alabiliyoruz.
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}
for eleman in sözlük:
    print(eleman)

#keys()
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}
for eleman in sözlük.keys():
    print(eleman)

#values()
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}
for eleman in sözlük.values():
    print(eleman)

#items()
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}
for eleman in sözlük.items():
    print(eleman)

