print("**********\nKULLANICI GİRİŞİ\n**********")

ad = "oğuzhan"
sifre = "123456"
giris_hakki = 3

while True:
        kullanıcı_adı = input("Ad:")
        parola = input("Şifre:")

        if (kullanıcı_adı != ad and parola == sifre):
            print("Kullanıcı Adı Hatalı...")
            giris_hakki -= 1
            print("Kalan Giriş Hakkı:",giris_hakki)
        elif (kullanıcı_adı == ad and parola != sifre):
            print("Şifre Hatalı...")
            giris_hakki -= 1
            print("Kalan Giriş Hakkı:", giris_hakki)
        elif (kullanıcı_adı != ad and parola != sifre):
            print("Kullanıcı adı ve şifre hatalı...")
            giris_hakki -= 1
            print("Kalan Giriş Hakkı:", giris_hakki)
        else:
            print("Başarıyla Giriş Yaptınız...")
            break
        if giris_hakki == 0:
            print("Giriş Hakkınız Bitti...")
            break