# Biz Python’da range() fonksiyonunu belli bir aralıkta bulunan sayıları göstermek için kullanıyoruz.

""" for i in range(0,10):
    print(i) """
#ilk parameterre sıfır ise yazmana gerek yok direkt range(10) yazabilirsin
""" sayac = 0
while sayac in range(3):
    parola = input("Parolanızı belirleyin: ")
    if sayac == 2:
        print("2 kere denediniz. Lütfen daha sonra tekrar deneyin!")
        break
    elif not parola:
        print("Parola bölümü boş geçilemez!")
        sayac += 1
    elif len(parola) in range(3,9):
        print("Parolanız başarıyla belirlendi: ", parola)
        break
    else:
        print("Parola 3 ile 8 karakter arasında olmalıdır!")
        continue 
 """
#Bu fonksiyonu kullanarak bir döngünün kaç kez çalışacağını da belirleyebilirsiniz

""" for i in range(3):
    parola = input("parola belirleyin: ")
    if not parola:
        print("parola bölümü boş geçilemez!")

    elif len(parola) in range(3, 8):
        print("Yeni parolanız", parola)
        break

    elif i == 2:
        print("parolayı 3 kez yanlış girdiniz.",
        "Lütfen 30 dakika sonra tekrar deneyin!")

    else:
        print("parola 8 karakterden uzun 3 karakterden kısa olmamalı") """

    #range(ilk_sayı, son_sayı, atlama_değeri)
# for i in range(0, 10, 2):
#     print(i)

for i in range(10, 0, -1): #10'dan 0'a kadar 1'er 1'er azalarak
    print(i)