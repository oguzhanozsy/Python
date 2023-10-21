print("********************\nKULLANICI GİRİŞİ\n********************")

name = "oğuzhan"
password = "123456"

isim = input("Kullanıcı Adı Giriniz:")
sifre = input("Parolayı Giriniz:")

if (name != isim and password == sifre) :
    print("Kullanıcı Adı Hatalı...")
elif (name == isim and password != sifre) :
    print("Şifre Hatalı...")
elif (name != isim and password != sifre) :
    print("Kullanıcı Adı ve Şifre Hatalı...")
else :
    print("Başarıyla Giriş Yaptınız...")