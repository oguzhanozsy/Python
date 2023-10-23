#FONKSİYONLARIN TANIMLANMASI

"""
    def fonksiyon_adı(parametre1,parametre2..... (opsiyonel)):
      # Fonksiyon bloğu
      Yapılacak işlemler
      # dönüş değeri - Opsiyonel
"""

def selamla():
    print("Selam arkadaşlar...")
    print("Nasılsınız?")

print(type(selamla))# Fonksiyonumuz tanımlandı.

#FUNCTION CALL
#fonksiyon_adı(Argüman1,Argüman2....)

type(selamla) # Tanımlı
selamla() # Fonksiyon parametre almadığında içine argümanlarımızı göndermiyoruz.

selamla()
selamla()
selamla()
selamla()

#PARAMETRELER VE ARGÜMANLAR
"""
Bizim fonksiyon tanımlarken tanımladığımız herbir değişken birer Parametre , fonksiyon çağrısı yaptığımız zaman içine 
gönderdiğimiz değerler ise Argüman olmaktadır. 
"""

def selamla(isim): # isim değişkenimiz burada parametre olmaktadır
    print("Merhaba:",isim)

selamla("Kemal") # "Kemal" değeri burada  argüman olmaktadır.
selamla("Ayşe") # "Ayşe" değeri burada  argüman olmaktadır.



# Toplama fonksiyonu
def toplama(a,b,c):
    print("Toplamları:",a+b+c)

toplama(3,4,5)
toplama(10,11,29)
toplama(4,9,40)


def faktoriyel(sayı):
    faktoriyel = 1
    if (sayı == 0 or sayı == 1):
        print("Faktoriyel",faktoriyel)
    else:
        while (sayı >= 1):
            faktoriyel *= sayı
            sayı -=1
        print("Faktoriyel", faktoriyel)

faktoriyel(5)
faktoriyel(6)
faktoriyel(1)
faktoriyel(0)

        

