fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
ali = fruits.copy()
print(fruits)
if True:
    print("test")



""" Eğer bir öğeyi indeksine göre silmek istiyorsanız, del ifadesi veya pop() metodu kullanılabilir. Örneğin, 1. indeksteki öğeyi silmek için:

del kullanarak:
python
Copy code
fruits = ["apple", "banana", "cherry"]
del fruits[1]
print(fruits)
Çıktı olarak ['apple', 'cherry'] alırsınız.
pop() kullanarak:
python
Copy code
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits)
pop() metodu aynı zamanda kaldırılan öğeyi de döndürür. Bu kodun çıktısı da ['apple', 'cherry'] olur.
Her iki yöntem de istenilen indeksteki öğeyi kaldırmak için kullanılabilir. """