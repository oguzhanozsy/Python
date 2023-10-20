#Tamsayıyı Ondalıklı Sayıya Çevirme
a = 43
print(float(a))

#Ondalıklı Sayıyı Tamsayıya Çevirme
#Çevirme işleminin sonucunda sayının sadece tam kısmını alır.
print(int(4.7))

a = 4
b = 3
print(int(a / b))

#Sayıları Stringe Çevirme
#Bir sayıyı string'e çevirmek için str() fonksiyonunu kullanabiliriz.Sayıyı oluşturan tüm rakamlar veya noktalar birer karaktere dönüşecek.
a = 32324324
b = str(a)
print(b)
print(len(b))

t = 3.14343
y = str(t)
print(t)
print(len(y))

#Stringleri Tamsayıya Çevirme
#Bir string'i tamsayıya çevirmek istediğimiz zaman int() fonksiyonunu kullanabiliriz.Ancak biraz dikkatli olmamızda fayda var.Dönüştürme işlemini yaparken stringin herbir karakterini bir rakam olduğundan emin olmalıyız.
a = "3223423423423"
b = int(a)
print(a)

#Stringleri Ondalıklı Sayıya Çevirme
a = "3.14342342"
b = float(a)
print(b)