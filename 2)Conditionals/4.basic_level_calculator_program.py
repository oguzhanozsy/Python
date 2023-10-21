print("""********************
HESAP MAKİNESİ PROGRAMINA HOŞGELDİNİZ
İŞLEMLER;

1.TOPLAMA İŞLEMİ
2.ÇIKARMA İŞLEMİ
3.ÇARPMA İŞLEMİ
4.BÖLME İŞLEMİ

********************
""")

a = int(input("a:"))
b = int(input("b:"))
c = input("işlem:")

if (c == "1") :
    print("{} + {} = {}".format(a,b,a+b))
elif (c == "2") :
    print("{} - {} = {}".format(a,b,a-b))
elif (c == "3") :
    print("{} x {} = {}",a,b,a*b)
elif (c == "4") :
    print("{} / {} = {}",a,b,a/b)
else :
    print("Geçersiz İşlem Girişi...")
