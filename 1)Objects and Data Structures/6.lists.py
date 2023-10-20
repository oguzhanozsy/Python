#Stringler konusundan bildiğimiz kadarıyla stringler değiştirilemez bir veri tipidir. Ancak, listelerimiz değiştirilebilir bir veritipidir.

#  1.LİSTE OLUŞTURMA
# Listeler bir [] köşeli parantez içine veriler veya değerler konarak oluşturulabilir.

# liste değişkeni. Değişik veri tiplerinden değerleri saklayabiliyoruz.
liste =  [3,4,5,6,"Elma",3.14,5.324]
print(liste)

liste2 = [3,4,5,6,7,8,9]
print(liste2)

# Boş liste
bos_liste = []
print(bos_liste)

# Boş liste . list() fonksiyonuyla da oluşturulabilir.
bos_liste = list()
print(bos_liste)

# len fonksiyonu listeler üzerinde de kullanılabilir.
liste3 = [3,4,5,6,6,7,8,9,0,0,0]
print(len(liste3))

# Bir string list() fonksiyonu yardımıyla listeye dönüştürülebilir.
s =  "Merhaba"
lst =  list(s)
print(lst)




# 2)LİSTELERİ INDEKSLEME VE PARÇALAMA

liste = [3,4,5,6,7,8,9,10]
print(liste)

# 0. eleman
print(liste[0])

# 4. eleman
print(liste[4])

# Sonuncu Eleman
print(liste[len(liste)-1])

# Sonuncu Eleman
print(liste[-1])

# İlk Eleman
print(liste[-len(liste)])

# Baştan 4. indekse kadar (dahil değil)
print(liste[:4])

# 1.indeksten 5.indekse kadar
print(liste[1:5])

print(liste[5:])

print(liste[::2])

print(liste[::-1])



# 3) TEMEL LİSTE METODLARI VE İŞLEMLERİ

# Bir listeyi birbirine toplama işlemini stringlerdeki gibi yapabiliriz.
liste1 =  [1,2,3,4,5]
liste2 =  [6,7,8,9,10]
print(liste1 + liste2)

# Bir listeye bir tane eleman eklemek içinse aşağıdaki işlemi uygulayabiliriz.
liste = [1,2,3,4]
liste =  liste + ["Murat"]
print(liste)

# Listeler direk olarak değiştirilebilirler.
liste[0] = 10
print(liste)

# Şöyle bir kullanım da mümkündür.
liste[:2] = [40,50]
print(liste)

# Bir listeyi bir tamsayıyla da çarpabiliriz.
liste = [1,2,3,4,5]
liste * 3
print(liste) # Ama gördüğümüz gibi listemiz değişmiyor.
liste = liste * 3
print(liste) # Eşitleme yaptığımız için liste değişti.






# pop metodu;
#Bu metod, içine değer vermezsek listenin son indeksindeki elemanı, değer verirsek verdiğimiz değere karşılık gelen indeksteki elemanı listeden atar ve attığı elemanı ekrana basar.
liste = [1,2,3,4,5]
print(liste.pop())

eleman = liste.pop(2)
print(eleman)

liste.append("Murat")
print(liste)
liste.pop()
print(liste)



# sort metodu;
#sort metodu listenin elemanlarını sıralamamızı sağlar

liste = [34,1,56,334,23,2,3,19]
liste.sort() # Küçükten büyüğe sıralar.
print(liste)

liste.sort(reverse = True) # Büyükten küçüğe sıralar.
print(liste)

liste = ["Elma","Armut","Muz","Kiraz"]
liste.sort() # Alfabetic olarak küçükten büyüğe
print(liste)

liste = ["Elma","Armut","Muz","Kiraz"]
liste.sort(reverse = True) # Alfabetic olarak büyükten küçüğe
print(liste)




# 4)İÇ İÇE LİSTELER
# 3 Tane liste oluşturalım.

liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = [7,8,9]

yeniliste = [liste1,liste2,liste3]
print(yeniliste)

# Şimdi, 2. listenin ilk elemanına nasıl ulaşacağımıza bakalım.
# 1.elemanın 0.elemanı
print(yeniliste[1][0])



