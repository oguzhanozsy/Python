"""
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın.
Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın.
"""

sayı1 = int(input("Sayı1:"))
sayı2 = int(input("Sayı2:"))
sayı3 = int(input("Sayı3:"))

çarpım = sayı1 * sayı2 * sayı3

print("{} x {} x {} = {}".format(sayı1,sayı2,sayı3,çarpım))
