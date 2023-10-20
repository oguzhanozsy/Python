"""
Kullanıcıdan iki tane sayı isteyin ve bu
sayıların değerlerini birbirleriyle değiştirin.
"""

a = input("a:")
b = input("b:")

print("Değiştirilmeden Önce\na:{}\nb:{}\n".format(a,b))

a,b = b,a

print("Değiştirildikten Sonra\na:{}\nb:{}".format(a,b))