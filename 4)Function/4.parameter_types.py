def selamla(isim = "İsimsiz"):
    print("Selam",isim)
selamla() # Hiç bir değer göndermedik. "isim" parametresinin değeri varsayılan olarak "İsimsiz" olarak belirlendi
selamla("Serhat") # Değer verirsek varsayılan değerin yerine bizim verdiğimiz değer geçer.



def bilgilerigöster(ad = "Bilgi Yok",soyad = "Bilgi Yok",numara =  "Bilgi Yok"):
    print("Ad:",ad,"Soyad:",soyad,"Numara:",numara)
bilgilerigöster() # Bütün parametreler varsayılan değerle ekrana basılacak.
bilgilerigöster("OĞUZHAN","ÖZSOY","123456") # ad ve soyad değerini verdik ancak numara parametresi varsayılan değer oldu.


bilgilerigöster(numara = "123456") # numara parametresini özel olarak belirtiyoruz.
bilgilerigöster(ad = "OĞUZHAN",numara = "123456")


#SEP PARAMETRESİ
print("Mustafa","Murat","Coşkun") # sep parametresine değer vermeyince varsayılan olarak boşluk karakteri verildi.
print("Mustafa","Murat","Coşkun",sep = "/") # sep parametresine özel olarak değer atadık.


#ESNEK SAYIDA DEĞERLER

def toplama(a, b, c):
    print(a + b + c)
toplama(3, 4, 5)

def toplama(a,b,c,d):
    print(a+b+c+d)
toplama(3,4,5,6)



#YILDIZLI PARAMETRE

"""
bir fonksiyonu esnek sayıda argümanla kullanmak istersem ne yapacağım ?
Bunun için de Yıldızlı Parametre kullanmam gerekiyor
"""

def toplama(*parametreler): # Artık parametreler değişkenini bir demet gibi kullanabilirim.
    toplam =  0
    print("Parametreler:",parametreler)
    for i in parametreler:
        toplam += i
    return toplam
print(toplama(3,4,5,6,7,8,9,10))
print(toplama())
print(toplama(1,2,3))
