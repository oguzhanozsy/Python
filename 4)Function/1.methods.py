"""
Metodlar bir obje üzerinde belli işlemleri gerçekleştiren objelere özgü fonksiyonlardır
"""

#LİSTE OBJESİ
liste =  [1,2,3,4,5,6]
liste.insert(1,"Murat")
print(liste)

liste.pop()
print(liste)

#bir metodun ne iş yaptığını anlamak için help fonksiyonunu kullanabiliriz.
help(liste.insert)
