a= 25
""""
a = a + 5
print(a) """


a += 5
print(a) #10
a -= 23
print(a)
a *= 3 
print(a)
a /= 2
print(a)
a **= 2
print(a) #100

print("\n------------------------------------------" )

#:= işleci Walrus operatörü

""" giriş = len(input("Adın ne? "))

if giriş < 4:
    print("Adın kısaymış.")
elif giriş < 6:
    print("Adın biraz uzunmuş.")
else:
    print("Çok uzun bir adın var.")
 """

if ( giriş := len(input("Adın ne? ")) ) < 4:
    print("Adın kısaymış.")
elif giriş < 6:
    print("Adın biraz uzunmuş.")
else:
    print("Çok uzun bir adın var.")

#Normalde bir değişkene değer atamak için önce bir satırda atama yapar, sonra başka bir satırda bu değeri kullanırdık.
#Walrus operatörü := ise bu iki adımı tek satırda yapmanıza olanak tanır:
