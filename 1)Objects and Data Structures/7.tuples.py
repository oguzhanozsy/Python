#Demetler veya İngilizce ismiyle tuplelar listelere oldukça benzer ancak farkları demetlerin değiştirilemez oluşudur. Bu yüzden programlarımızda değiştirilmesini istemediğimiz değerleri bir demet içinde depolayabiliriz

# 1)Demet Oluşturma

# Demet elemanları parantez içine alınarak demet oluşturulabilir.
demet = (1,2,3,4,5,6,7,8,9)
print(demet)

# type() fonksiyonu yardımıyla türünü öğrenelim.
print(type(demet))

# Tek elemanlı demet bu şekilde tanımlanabilir.
demet = (5)
print(demet)

demet = (1,2,3,4,5,6,7)
# 0. indekse  ulaşma
print(demet[0])

# 4. indekse ulaşma
print(demet[4])

# sonuncu indekse ulaşma
print(demet[-1])

print(demet[2:])





# 2)DEMETLERİN TEMEL METODLARI

# Demeti oluşturalım.
demet = (1,2,3,"Mustafa","Murat","Coşkun")
# "Mustafa" elemanının indeksini buluyoruz.
print(demet.index("Mustafa"))
print(demet.index(1))

# count metoduyla içine verdiğimiz değerin demette kaç defa geçtiğini bulabiliriz.
demet = (1,23,34,34,2,1,4,5,1,1,34)
print(demet.count(1))
print(demet.count(34))