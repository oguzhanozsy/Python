#Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if(a >= b and a >= c) :
    print("En Büyük Sayı {}'dır".format(a))
elif (b >= a and b >= c) :
    print("En Büyük Sayı {}'dır".format(b))
else :
    print("En Büyük Sayı {}'dır".format(c))

