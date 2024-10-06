izinli_karakterler = "0123456789+-/*= "

print("HOS GELDINIZ")

while True:
    veri = input("İşlem yapmak istediğiniz veriyi giriniz: ")
    if veri == "q":
        print("Çıkılıyor...")       
        break
    for i in veri:
        if i not in izinli_karakterler:
            print("İzin verilmeyen karakter girdiniz")
            quit()
    print(eval(veri))
    


