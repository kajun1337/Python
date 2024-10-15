# Python’da break özel bir deyimdir. Bu deyim yardımıyla, devam eden bir süreci 
# kesintiye uğratabiliriz. Bu deyimin kullanıldığı basit bir örnek verelim:
while True:

    parola = input("Lütfen bir parola belirleyiniz:")

    if len(parola) < 5:

        print("Parola 5 karakterden az olmamalı!")

    else:

        print("Parolanız belirlendi!")

        break   

 