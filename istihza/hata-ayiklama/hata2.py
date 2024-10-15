try:
    ilk_sayı    = input("ilk sayı: ")
    ikinci_sayı = input("ikinci sayı: ")
    # Kullanıcıdan alınan verileri tamsayıya dönüştürmeye çalışıyoruz
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)

except(ValueError, ZeroDivisionError):
        print("Bir hata oluştu!")
        print("Lütfen tekrar deneyin!")

        """ except ValueError:
    print("INTEGER DEGER KONTROL")
except ZeroDivisionError:
    print("Bir sayıyı 0'a bölemezsiniz!") """