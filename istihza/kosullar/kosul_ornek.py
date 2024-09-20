k_Adi = input("Kullanıcı adı" )
P_word = input("Parola" )
if len(k_Adi) > 10 or len(P_word) > 5:
    print("Kullanıcı adı ve parolanız 10 ve 5 karakterden fazla olamaz")
    exit()
elif k_Adi[0] == "*":
    print("Kullanıcı adı * işareti ile başlayamaz")
    exit()
else:
    print("Giriş başarılı")
    mesaj = "Parolanız {}'dır lütfen saklayınız".format(P_word)
    print(mesaj)
    exit()
    