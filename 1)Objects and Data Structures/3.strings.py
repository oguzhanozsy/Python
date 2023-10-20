#Tek Tırnak İle Oluşur
print('OĞUZHAN')

#Çift Tırnak İle Oluşur
print("OĞUZHAN")

#Üç Tırnak İle Oluşur
print("""OĞUZHAN""")

#Tırnakların kesme işareti ile karışmaması için kesme işaretinden önce \ kullan
print('oğuzhan\'ın')

a = "elma"
print(a)

#String indexleme ve parçalama

a = "ali"
print(a[1])

#Pythonda stringler baştan olduğu gibi sondan da indekslenebilirler. Sondan başlayarak -1,-2,... şeklinde indekslenebilir.
#sondaki eleman "-1" eleman
a = "murat"
print(a[-1])

#Peki uzun bir string'in sadece belirli bir kısmını elde etmek için bu formülü kullanacağız-> [başlama indeksi : bitiş indeksi : atlama değeri]
#burdaki formülde başlangıç indeksi dahildir ama bitiş indeksi dahil değildir.

a = "Python Progralama Dili"
#4. indeksten başla 10.indekse kadar(dahil değil) al.
print(a[4:10])

#Başlangıç değeri belirtilmemişse en baştan başlayarak alır.
print(a[:10])

# Bitiş değeri belirtilmemişse en sonuna kadar alır.
print(a[4:])

# İki değer de belirtilmemişse tüm stringi al.
print(a[:])

#Son karaktere kadar al.
print(a[:-1])

# Baştan sona 2 değer atlaya atlaya stringi al.
a[::2]

# 4.indeksten 12'nci indekse 3'er atlayarak stringi al.
a[4:12:3]

# Baştan sona -1 atlayarak stringi al. (String'i ters çevirme)
print(a[::-1])

#STRING ÖZELLİKLERİ

#len() fonksiyonunu kullanma.
a = "Python Programlama Dili"
print(len(a))

#Stringleri direkt olarak değiştiremeyiz.

# Stringleri toplayalım yani birbirine ekleyelim.
a = "Python "
b = "Progrmalama "
c = "Dili "
print(a + b + c)

x = "Oğuzhan "
x = x + "Özsoy"
print(x)

# Bir stringi bir sayıyla çarpabiliriz
# Python * 3 aslında Python + Python + Python işlemine eşdeğerdir.
print("python " * 3)