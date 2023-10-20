"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre
yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar
ödemesini gerektiğini hesaplayın.
"""

yakıt = float(input("KM'de ne kadar yakıyor:"))
km = int(input("Kaç KM yol gitti:"))

tutar = yakıt * km

print("Toplam Tutar:{} TL".format(tutar))