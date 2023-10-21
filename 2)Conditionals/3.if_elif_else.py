#Python Programlarının çalışma mantığı
"""

Çoğu zaman Python programlarımız belirli bloklardan oluşur ve bu bloklar her zaman çalışmak zorunda olmaz.
Peki bu bloklar nasıl tanımlanır ? Pythonda bir blok tanımlama işlemi Girintiler sayesinde olmaktadır.

"""
a = 2 # Blok 1 'e ait kod

if (a == 2):
    print(a) # Blok 2'ye ait kod
print("Merhaba") # Blok 1 ' ait kod



a = 2 # Blok 1 'e ait kod

if (a == 3):
    print(a) # Blok 2'ye ait kod
print("Merhaba") # Blok 1 ' ait kod


#KOŞULLU DURUMLAR


#if BLOĞU
"""
 if (koşul): 
           # if bloğu - Koşul sağlanınca (True) çalışır. Bu hizadaki her işlem bu if bloğuna ait.
           # if bloğu - Girintiyle oluşturulur.
           Yapılacak İşlemler
"""

# 18 yaş kontrolü
yaş = int(input("Yaşınızı giriniz:"))

if (yaş < 18):
    # if bloğu -  Girinti ile sağlanıyor.
    print("Bu mekana giremezsiniz.")

#########################################

# 18 yaş kontrolü
yaş = int(input("Yaşınızı giriniz:"))

if (yaş < 18):
    # if bloğu -  Girinti ile sağlanıyor.
    print("Bu mekana giremezsiniz.")

#########################################

# Negatif mi değil mi ?
sayı = int (input("Sayıyı giriniz:"))

if (sayı < 0):
    print("Negatif Sayı")

#########################################

# 18 yaş kontrolü
yaş = int(input("Yaşınızı giriniz:"))

if (yaş < 18):
    # if bloğu -  Girinti ile sağlanıyor.
    print("Bu mekana giremezsiniz.")
print("Mekana hoşgeldiniz.")

#########################################

# 18 yaş kontrolü
yaş = int(input("Yaşınızı giriniz:"))

if (yaş < 18):
    # if bloğu -  Girinti ile sağlanıyor.
    print("Bu mekana giremezsiniz.")
print("Mekana hoşgeldiniz.")


#else BLOĞU

"""
else:
           # else bloğu - Yukarısındaki herhangi bir if bloğu (veya ilerde göreceğimiz elif bloğu) çalışmadığı
           # zaman çalışır. 
           # else bloğu - Girintiyle oluşturulur.
               Yapılacak İşlemler
"""

# 18 yaş kontrolü
yaş = int(input("Yaşınızı giriniz:"))

if (yaş < 18):
    # if bloğu -  Girinti ile sağlanıyor.
    print("Bu mekana giremezsiniz.")
else:
    # else bloğu -  if koşulu sağlanmazsa çalışacak.
    print("Mekana hoşgeldiniz.")

#########################################

# 18 yaş kontrolü
yaş = int(input("Yaşınızı giriniz:"))

if (yaş < 18):
    # if bloğu -  Girinti ile sağlanıyor.
    print("Bu mekana giremezsiniz.")
else:
    # else bloğu -  if koşulu sağlanmazsa çalışacak.
    print("Mekana hoşgeldiniz.")

#########################################



# if-elif-else BLOKLARI

"""
           if koşul: 
               Yapılacak İşlemler
           elif başka bir koşul:
               Yapılacak İşlemler
           elif başka bir koşul:
               Yapılacak İşlemler

                //
                //
           else:
               Yapılacak İşlemler 
"""

işlem =  int(input("İşlem seçiniz:")) # 3 tane işlemimiz olsun.

if işlem == 1:
    print("1. işlem seçildi.")
elif işlem == 2:
    print("2. işlem seçildi.")
elif işlem == 3:
    print("3. işlem seçildi.")
else:
    print("Geçersiz İşlem!")

#########################################

#if-if-if blokları

note = float(input("Notunuzu giriniz:"))

if note >= 90:
    print("AA")
if note >= 85:
    print("BA")
if note >= 90:
    print("BA")
if note >= 80:
    print("BB")
if note >= 75:
    print("CB")
if note >= 70:
    print("CC")
if note >= 65:
    print("DC")
if note >= 60:
    print("DD")
else:
    print("Dersten Kaldınız")
