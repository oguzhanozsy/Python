#Mantıksal Değerler(Boolean)

#İki değere sahiptir.(True/False)

a = True
print(type(a))

b = False
print(type(b))


#Python'da bir sayı değeri eğer 0'dan farklıysa True,0 = ise False olarak anlam kazanır.

print(bool(12.4))
print(bool(0.0))
print(bool(121212))
print(bool(-1))
print(bool(0))

#Bool değerleri ayrıca bir karşılaştırma operatöründen sonra ortaya çıkan sonuç değeridir.

print(1 > 2) # 1 2 den büyük olmadığı için sonuç False olacaktır.
print(1 < 2) # 1 2 den küçük olduğu için sonuç True olacaktır.

#Ayrıca Pythonda eğer bir değişkenin değerini sonradan belirlemek isterseniz geçici olarak bu değişken None (atanmamış anlamında) değerine eşitleyebilirsiniz.

a = None #Henüz değer atamadık
print(a)

a = 4 #Şimdi değer atıyoruz
print(a)



#KARŞILAŞTIRMA OPERATÖRLERİ

"""
(==)	İki değer birbirine eşitse True, değilse False değer döner.
(!=)	İki değer birbirine eşit değilse True, diğer durumda False döner.
(>) 	Soldaki değer sağdaki değerden büyükse True, değilse False döner.
(<) 	Soldaki değer sağdaki değerden küçükse True, değilse False döner.
(>=)	Soldaki değer sağdaki değerden büyükse veya sağdaki değere eşitse True, değilse False döner.
(<=)	Soldaki değer sağdaki değerden küçükse veya sağdaki değere eşitse True, değilse False döner.
"""

print("Mehmet" == "Mehmet")
print("Mehmet" == "Murat")
print("Mehmet" != "Murat")
print("Oğuz" < "Murat") #Alfabetik olarak bakar
print(2 < 3)
print(54 >= 54)
print(98 > 32)
print(34 <= 45)