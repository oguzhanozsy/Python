#KULLANICIDAN GİRDİ ALMA - input() FONKSİYONU


# input() fonksiyonunu çalıştırdığımız zaman bizden bir girdi bekler
input()

# eğer istersek fonksiyonun içine bir değer gönderebiliriz
a = input("Lütfen Bir Sayı Giriniz:")
print(a)

# Kullanıcının girdiği değer input fonksiyonundan string olarak bize döner.
a = input("Lütfen bir sayı giriniz:")
print(type(a))


#Eğer biz bir sayı ile işlem yapacaksak kullanıcıdan aldığımız değere (stringi) float ya da int fonksiyonuyla veri tipi dönüştürme işlemi yapmamız gerekir.

# Hatalı Çalışma
a = input("Lütfen bir sayı giriniz:")
print(a * 3) # Girdiğimiz değer 5 ise sonucu 15 bekleriz. Ancak sonuç 555 şeklinde ortaya çıkar

# Doğru Çalışma
a = int(input("Lütfen bir sayı giriniz:")) # Veri tipi dönüşümü
print(a * 3)

# Hatalı Çalışma
a = input("Lütfen bir sayı giriniz:")
print(a * 3) # Girdiğimiz değer 5.4 ise sonucu 16.2 bekleriz. Ancak sonuç 5.45.45.4 şeklinde ortaya çıkar.

# Doğru Çalışma
a = float(input("Lütfen bir sayı giriniz:"))
print(a * 3) # Girdiğimiz değer 5.4 ise sonucu 16.2 bekleriz. Ancak sonuç 5.45.45.4 şeklinde ortaya çıkar.

# ÖRNEK:
a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı:"))
c = int(input("Üçüncü Sayı:"))

print("Toplamları:",a+b+c)