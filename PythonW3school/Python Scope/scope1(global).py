""" Kapsam (scope): Bir değişkenin erişilebilir olduğu alanı ifade eder. Bir değişkenin kapsamı, 
onun tanımlandığı bölgeye bağlıdır.

Lokal Kapsam (Local Scope): Bir değişkenin sadece tanımlandığı işlevin içinde erişilebilir olduğu kapsamı ifade eder. Yani, bir işlevin içinde tanımlanan
bir değişkenin kapsamı, sadece o işlevin içinde geçerlidir ve bu değişken sadece o işlevin içinde kullanılabilir. """

def myfunc():
    x = 100
    print(x)

myfunc()

print("##############################################################################################")

def ruvo():
    x = 300
    def ic():
        print(x)
    ic()

ruvo()
print("##############################################################################################")

#Global Scope


y = 400 
def mytesti():
    print(y)

mytesti()
print(y)

print("##############################################################################################")

#Naming Variables

def totaliter():
    global x
    x = 300

totaliter()
print(x)

print("##############################################################################################")
global berkay
berkay = 888
ferit = 300
def tazmanya():
    global ferit
    ferit = 200
    berkay = 19
    return berkay
tazmanya()
# print(ferit)
print(tazmanya())

print("##############################################################################################")



