"""  Aslında, iteratorler, bir veri yapısındaki öğelerin üzerinde 
dolaşmamıza ve her bir öğeye sırayla erişmemize olanak tanır.

Python'da birçok veri yapısı, örneğin listeler, demetler, sözlükler vb., bir iterator oluşturmak
için kullanılabilir. Bu iteratorler, iter() fonksiyonuyla elde edilir. Ardından, next() 
fonksiyonu kullanılarak her bir öğe sırayla alınabilir. """

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


#Even strings are iterable objects, and can return an iterator:


mystr = "banana"
myit2 = iter(mystr)


print(next(myit2))
print(next(myit2))
print(next(myit2))
print(next(myit2))
print(next(myit2))
