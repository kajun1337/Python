import random

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

print("--------------------")
hakan = 8
p = float(hakan)
print((p))

print ("%%")

name = 'Mustafa'
yas = 2
tost = 'Sever %s' % name

marul = ('Kesin mi {} yasin {}'.format(name,yas))
marul = ('Kesin mi {} yasin {}'.format(name,yas))

print(marul)

#print("Random sayi üretici\n {}" ,format(random.randrange(1,4)))

print("Random sayi üretici\n" , format(random.randrange(1,4)))

print("Random sayi üretici\n" , (random.randrange(1,4)))









