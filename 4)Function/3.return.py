def toplama(a,b,c):
    return a+b+c # return'un kullanımı
def ikiyle_çarp(a):
    return a*2
toplam = toplama(3,4,5)
print(ikiyle_çarp(toplam))



def üçleçarp(a):
    print("1.fonksiyon çalıştı")
    return a*3
def ikiyletopla(a):
    print("2.fonksiyon çalıştı")
    return a + 2
def dördeböl(a):
    print("3.fonksiyon çalıştı")
    return a / 4
# 3 ünü beraber kullanalım.

print(dördeböl(ikiyletopla(üçleçarp(5))))


#return ifadesinden sonra yapılan herhangi bir işlem çalıştırılmaz.


def toplama(a, b, c):
    return a + b + c
    print("Toplama fonksiyonu")  # Çalıştırılmadı.

print(toplama(1, 2, 3))


def toplama(a, b, c):
    print("Toplama fonksiyonu")  # Çalıştırıldı.
    return a + b + c

print(toplama(1, 2, 3))
