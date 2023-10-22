"""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""

sayı = int(input("Sayı:"))

i = 1
toplam = 0

while (i < sayı):

    if (sayı % i == 0):
        toplam += i
    i += 1

if (toplam == sayı):
    print("{} sayısı mükemmel sayıdır".format(sayı))
else:
    print("{} sayısı mükemmel değildir".format(sayı))