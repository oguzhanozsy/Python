print(35)

a = 5
b = 10
print(a + b)

# Aynı satırda birden fazla değeri bastırmayı araya virgül atarak yaparız
print("Merhaba" , 21 , "Yaşım")

#String Özel Karakterler

# \n
# Eğer print() fonksiyonu stringlerde böyle bir karakterle karşılaşırsa alt satırdan ekrana yazdırma işlemine devam eder
print("Merhaba\nNasılsın\nİyi misin")

# \t
# Eğer print() fonksiyonu stringlerde böyle bir karakterle karşılaşırsa bir tab boşluk bırakarak ekrana yazdırma işlemine devam eder
print("Ocak\tMart\tŞubat")


# type() fonksiyonu
# type() fonksiyonu içine gönderilen değerin hangi veri tipinden olduğunu söyler.

# Integer (Tamsayı) türü
a = 65
print(type(a))





# Print() Fonksiyonunun Özellikleri;

# 1) sep parametresi:
# print() fonksiyonunda kullanılabilen sep parametresi yazdırdığımız değerlerin arasına istediğimiz karakterlerin
# yerleştirilmesini sağlar. Eğer bu parametreyi kullanmazsak değerlerin arasına varsayılan olarak boşluk yerleştirilir.

print(3,4,5,6,7,8,9)

# sep parametresi sayesinde değerlerin arasına nokta konuyor.
print(3,4,5,6,7,8,9,sep = ".")

# Değerlerin arasında "/" sembolü yerleştiriliyor.
print("06","04","2015",sep = "/")

print("Mustafa","Murat","Coşkun",sep = "\n")

# Yıldızlı Parametreler:
# Eğer bir stringin başına * işareti koyup, print fonksiyonuna gönderirsek bu string karakterlerine ayrılacak ve her bir karakter ayrı birer string olarak davranılarak ekrana basılacaktır.

# Varsayılan olarak karakterlerin arasına boşluk konuluyor.
print(*"Python")
print(*"Python",sep = "\n")
print(*"TBMM",sep =".")




#FORMATLAMA
("Programlama yaparken bazı yerlerde bir stringin içinde daha önceden tanımlı string,float, int vs. değerleri yerleştirmek "
 "isteyebiliriz. Böyle durumlar için Pythonda format() fonksiyonu bulunmaktadır. Örneğin, programımızda 3 tane tamsayı değerimiz "
 "var ve biz bunları bir string içinde ekrana basmak istiyoruz. Bunun için format() fonksiyonunu kullanabiliriz. format() fonksiyonunun "
 "çok fazla özelliği olduğu için, ben burada sadece en çok kullandığımız özelliğini göstereceğim.")

# Burada 3 tane süslü parantezimiz ({}) var ve bunların yerine sırasıyla format fonksiyonun içindeki değerler geçiyor.
"{} {} {}".format(3.1423,5.324,7.324324)

a = 3
b = 4
print("{} + {} 'nin toplamı {} 'dır".format(a,b,a+b))

# Süslü parantezlerin içindeki sayılar format fonksiyonun içinden hangi sıradaki değerin geleceğini söylüyor.
"{1} {0} {2}".format(43,"Murat",54)

# Süslü parantezlerin içindeki kullanım ondalıklı kısmın sadece 2 basamağına kadar almak istediğimiz söylüyor.
"{:.2f} {:.2f} {:.3f}".format(3.1463,5.324,7.324324)



















