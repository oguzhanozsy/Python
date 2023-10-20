#SÖZLÜKLER
("Sözlükler veya İngilizce ismiyle dictionaryler aynı gerçek hayattaki sözlükler gibi davranan bir veritipidir."
"Bu veritipi, şimdiye kadar gördüğümüz tüm veritiplerinden yapısı gereği farklıdır. Sözlüğün içindeki her bir eleman"
"indeks ile değil, anahtar (key), değer (value) olarak tutulur. Bu anlamda gerçek hayattaki sözlüklere oldukça benzerler."
"Örneğin, elimize bir ingilizce-Türkçe sözlük alıp freedom kelimesini(key ya da anahtar) aradığımız zaman karşılık değer"
"özgürlük (değer ya da value) olarak karşımıza çıkar. Sözlükleri de bu şekilde düşünebiliriz.")

#SÖZLÜK OLUŞTURMAK

# Süslü Parantez ve iki nokta (:) ile anahtar değerlerimizi yerleştirelim.
sözlük1 = {"sıfır":0,"bir":1,"iki":2,"üç":3}
print(sözlük1)
print(sözlük1["bir"])


# Boş bir sözlük
sözlük2 = {}
print(sözlük2)

# Boş bir sözlük - dict() ile de oluşturulabilir
sözlük2 = dict()
print(sözlük2)

# SÖZLÜK DEĞERLERİNE ERİŞMEK VE SÖZLÜĞE DEĞER EKLEMEK
print(sözlük1)

# "bir" anahtarına karşılık gelen değeri buluyoruz.
print(sözlük1["bir"])

# "iki" anahtarına karşılık gelen değeri buluyoruz.
print(sözlük1["iki"])



a = {"bir" : [1,2,3,4], "iki": [[1,2],[3,4],[5,6]],"üç" : 15}
# "iki" anahtarının değeri
print(a["iki"])

# İçiçe listeleri biliyoruz.
print(a["iki"][1][1])

print(a["üç"])
a["üç"] += 5
print(a)

# Bir sözlüğe dinamik olarak da eleman ekleyebiliriz.
# Sözlük oluşturalım.
a = {"bir":1,"iki":2,"üç":3}
a["sıfır"] = 0
print(a)
#Dikkat ederseniz yeni eklediğimiz anahtar ve değer sözlüğün sonuna eklenmedi. Burada sözlüklerin bir özelliğini daha görüyoruz. Sözlükler diğer veritiplerinden farklı olarak sıralı olmayan bir veritipidir.




# İÇ İÇE SÖZLÜKLER
a = {"sayılar":{"bir":1,"iki":2,"üç":3},"meyveler":{"kiraz":"yaz","portakal":"kış","erik":"yaz"}}
print(a["sayılar"]["bir"])
print(a["meyveler"]["kiraz"])


# TEMEL SÖZLÜK METODLARI

yeni_sözlük = {"bir":1,"iki":2,"üç":3}

# values() metodu sözlüğün değerlerini(value) bir liste olarak döner.
print(yeni_sözlük.values())

# keys() metodu sözlüğün anahtarlarını(key) bir liste olarak döner.
print(yeni_sözlük.keys())

# items() metodu sözlüğün anahtar ve değerlerini bir liste içinde demet olarak döner.
print(yeni_sözlük.items())
