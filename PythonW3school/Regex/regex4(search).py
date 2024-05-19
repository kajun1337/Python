import re
txt = "The rain in Spain"
x = re.search("\s",txt)
print(x.start())

""" re.search() fonksiyonu, verilen deseni dizede arar ve eşleşme bulunursa bir Match nesnesi döndürür. Bu örnekte, "\s" deseni boşluk karakterlerini arar. x değişkenine atanan Match nesnesi, boşluk karakteri ile eşleştiği için değer alır.

start() yöntemi, eşleşmenin başlangıç konumunu döndürür. Yani, eşleşen desenin dizede nereden başladığını verir.

Bu örnekte print(x.start()), ilk boşluk karakterinin dizedeki konumunu (indeksini) yazdıracaktır. Örneğin, "The rain in Spain" dizesindeki ilk boşluk karakteri, "3" konumunda bulunmaktadır (sayma 0'dan başlar). Bu nedenle, çıktı "3" olacaktır. """

y = re.search("Portakal" ,txt)
print(y)

print("*****************")

z = re.split("\s" ,txt)
print(z)

#You can control the number of occurrences by specifying the maxsplit parameter:
a = re.split("\s",txt,maxsplit=1)
print(a)

print("*****************")
#SUB re.sub()

b = re.sub("\s","33",txt)
print(b)
#The33rain33in33Spain bosluklara 33 at dedik 
c = re.sub("\s","9",txt,2)  # 4.parametre de kac tane koyulacagını seciyorsun bir nevi
print(c)

print("*****************")
