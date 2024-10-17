# enumerate()
# Eğer yazdığınız bir programda numaralandırmaya ilişkin
# işlemler yapmanız gerekiyorsa Python’ın size sunduğu çok
# özel bir fonksiyondan yararlanabilirsiniz. Bu fonksiyonun
# adı enumerate().

print(*enumerate("istihza"))
print(*reversed("istihza"))

# 2. Fonksiyon Çağrılarında * Operatörü
# Fonksiyon çağrılarında * operatörü, bir iterable (örneğin bir
# liste veya tuple) içindeki elemanları ayrı ayrı argümanlar
# olarak geçmek için kullanılır.

# 1. Fonksiyon Parametrelerinde * Operatörü
# Fonksiyon tanımında * operatörü, değişken sayıda argüman
# alabilen bir fonksiyon tanımlamak için kullanılır. Bu tür
# parametreler "varargs" olarak adlandırılır.

x = dir(str)
for i in enumerate(x):
    if "_" not in i[1]:
        print(i)


print("*" * 50)
print(help(enumerate))

import sys

print(sys.version_info, sys.version_minor, sys.version_micro)
