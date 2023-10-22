sayi_1 = 1
sayi_2 = 1

fibanocci = [sayi_1,sayi_2]

for i in range(10):

    sayi_1,sayi_2 = sayi_2,sayi_1+sayi_2

    fibanocci.append(sayi_2)

print(fibanocci)