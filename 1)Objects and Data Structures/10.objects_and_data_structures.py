#1.PROGRAM ÖRNEĞİ

print("OYUNCU KAYDETME PROGRAMI")

ad = input("Oyuncunun Adı:")
soyad = input("Oyuncunun Soyadı:")
takım = input("Oyuncunun Takımı:")

bilgiler = [ad,soyad,takım]

print("Bilgiler Kaydediliyor...")

print("Ad:{}\nSoyad:{}\nTakım:{}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler Kaydedildi...")

#2.PROGRAM ÖRNEĞİ

"""
2. dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem: ax^2 + bx + c
Deltayı Hesaplama: b ** 2 - 4 * a * c

Birinici Kök: ( -b - delta ** 0.5) / (2 * a))
İkinic Kök: ( -b + delta ** 0.5) / (2 * a))

"""

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = (b ** 2) - (4 * a * c)

x1 = (-b - (delta) ** 0.5) / (2 * a)
x2 = (-b + (delta) ** 0.5) / (2 * a)

print("Birinci Kök:{}\nİkinci Kök:{}".format(x1,x2))