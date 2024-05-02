""" - Liste: Dinamik veri saklamak veya değişen verileri işlemek için kullanılır.
- Tuple: Sabit verileri saklamak veya değişmez verileri işlemek için kullanılır. """

# Liste oluşturma DINAMIK
""" list1 = ["banana", "cherry"]
list1.append("apple")  # Listeye yeni bir öğe ekleyebiliriz
print(list1)  # Çıktı: ["banana", "cherry", "apple"] """

# Tuple oluşturma  STATIK
"""tuple1 = ("banana", "cherry")
tuple1.append("apple")  # Hata! Tuple'lara öğe eklenemez
 """

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Allow Duplicates (tekrara izin verir)

abdullah = ("apple", "banana", "cherry", "apple", "cherry")
print(abdullah)

ex = ("apple", "banana", "cherry")
print(len(ex))

#İçinde farklı data tiplerini tutabilir
tuple1 = ("abc", 34, True, 40, "male")
print(type(tuple1))


