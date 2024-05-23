import platform
import random
import modules3variables
from modeules4 import kisi2
# from modeules4 import greeting -->  bu da olabiliirdi
import pandas



x = platform.system()
print(x)

y = dir(platform)
print("\n*********", y)
print("\n*********")
print("\n*********")
print("\n*********")


print(modules3variables.kisi1["ad"])


print("\n*********")
print("\n*********")
print("\n*********")


print(kisi2["ad"])
sayi = 0
array = [12,10,3,59] 
print("\n*********")
print("\n*********")
print("\n*********")

# print(sayi.random())

print(dir(random))
print("\n*********")
print("\n*********")
print("\n*********")

random.shuffle(array)
print(array)

print("\n*********")
print("\n*********")
print("\n*********")

print(dir(pandas))

print("\n*********")
print("\n*********")
print("\n*********")

print(random.randrange(12,100))

print("\n*********")
print("\n*********")
print("\n*********")





