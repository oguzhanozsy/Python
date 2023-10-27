"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
"""

def ebobb(minimum,maximum):

    for i in range(1,minimum+1):
        if( minimum % i == 0 and maximum % i == 0):
            ebob = i

    print("EBOB({},{})={}".format(minimum,maximum,ebob))




sayı1 = int(input("1.Sayıyı Giriniz:"))
sayı2 = int(input("2.Sayıyı Giriniz:"))

minimum = min(sayı1,sayı2)
maximum = max(sayı1,sayı2)

ebobb(minimum,maximum)
