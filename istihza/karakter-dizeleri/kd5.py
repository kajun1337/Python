print(dir(str))
# . Bu metot bize Python’daki bir nesnenin özellikleri hakkında bilgi edinme imkanı verecek.
# dir() fonksiyonuna parametre olarak bu ‘str’ kelimesini verdiğimizde, Python bize karakter dizilerinin bütün metotlarını listeliyor.

print("\n**************************************************")


x = dir(str)
sayac = 0
for i in x:
    if "_" not in i[0]:
        sayac += 1
        print('{}-'.format(sayac),i)

print("Toplam {} adet metot var.".format(sayac))
