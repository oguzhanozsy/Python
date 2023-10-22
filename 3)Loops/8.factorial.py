print("**********\nFAKTORİYEL PROGRAMINI HOŞGELDİNİZ\n**********")
print("\nÇıkış için q'ya basın")

while True:
    sayi = input("Sayı:")
    if (sayi == "q"):
        print("Programdan Çıkılıyor...")
        break

    sayi = int(sayi)

    faktoriyel = 1

    for i in range(2,sayi+1):
        faktoriyel *= i

    print("Faktoriyel:",faktoriyel)
