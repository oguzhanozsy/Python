print("***********\nATM SİSTEMİNE HOŞGELDİNİZ\n**********")
print("""
İŞLEMLER:
1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme

Programdan Çıkmak İçin q'ya basını
""")

bakiye  = 1000

while True:
    islem = input("İşlem Giriniz:")

    if (islem == "q"):
        print("Yine Bekleriz...")
        break
    elif (islem == "1"):
        print("Bakiyeniz {} TL'dir".format(bakiye))
    elif (islem == "2"):
        miktar = int(input("Yatırmak İstediğiniz Tutar:"))

        bakiye += miktar
    elif (islem == 3):
        miktar = int(input("Çekmek İstediğiniz Tutar:"))
        if (bakiye - miktar < 0):
            print("Bu kadar para çekemezsiniz...")
            print("Bakiyeniz {} tldir".format(bakiye))
            continue
        bakiye -= miktar
    else:
        print("Lütfen geçerli bir işlem giriniz.")