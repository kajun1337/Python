class MyClass:
    # __iter__ metodu, bir iterator nesnesi oluşturur ve döndürür
    def __iter__(self):
        # İterator başlatılırken kullanılabilecek başlangıç değerleri burada tanımlanabilir
        self.a = 1
        # Iterator nesnesi döndürülür
        return self
    
    # __next__ metodu, bir sonraki öğeyi döndürür
    def __next__(self):
        # Her __next__() çağrısında, bir sonraki öğe hesaplanır
        x = self.a
        # Her __next__() çağrısında, öğe sayacı artırılır
        self.a += 1
        # Önceki öğe döndürülür
        return x

# MyClass sınıfından bir örnek oluşturulur
atak = MyClass()
# MyClass örneği üzerinde bir iterator oluşturulur
myiter = iter(atak)

# Iterator üzerinde next() fonksiyonu kullanılarak sıradaki öğe alınır ve yazdırılır
print(next(myiter))  # 1
# Bir sonraki öğe alınır ve yazdırılır
print(next(myiter))  # 2
# Bir sonraki öğe alınır ve yazdırılır
print(next(myiter))  # 3
# Artık koleksiyonun sonuna ulaşıldığı için StopIteration hatası alınır
# print(next(myiter))  # StopIteration hatası fırlatılır
