""" x = int(input("Notunuz: "))
if x > 100 or x < 0:
    print("Böyle bir not yok")

elif not (x >= 50):
        print("Kaldınız")
else:
        print("Geçtiniz")
    
 """

parola = input("Parola: ")
if not parola:
    print("Parola boş olamaz")

""" parola = ""

bool(parola) #parola boş bırakılmamış, değil mi?

False #Hayır, parola boş bırakılmış.

bool(not parola) #parola boş bırakılmış, değil mi?

True #Evet, parola boş bırakılmış """