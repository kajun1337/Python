a = 300
print(id(a))
lale = "Azerbeycan"
print(id(lale))
b = 300 # a ile b nin kimlik adresi aynı olur çünkü aynı değeri taşırlar
print(id(b))

print(a is 300)

# is ve == işleçleri birbirleriyle aynı işlevi görmez
#is işleci nesnelerin kimliklerine bakıp o nesnelerin aynı nesneler olup olmadığını kontrol ederken
# == işleci ise nesnelerin değerlerine bakarak aynı olup olmadıklarını kontrol eder.

ezber  = "python güçlü ve kolay bir programlama dilidir"

print(ezber is "python güçlü ve kolay bir programlama dilidir")