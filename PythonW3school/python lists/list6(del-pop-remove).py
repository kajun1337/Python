# The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# thislist.pop(0)

# del thislist
# thislist.clear()
thislist.pop(0)
thislist.remove("banana")
print(thislist)
# print(bool(thislist))

""" return ifadesi, yalnızca
fonksiyonlar içinde kullanılabilir. 
Eğer bu kodu bir fonksiyon dışında çalıştırmaya 
çalışırsanız, SyntaxError alırsınız çünkü return ifadesi geçerli 
bir bağlamda (fonksiyon içinde) kullanılmamış olur. """




def check_list(thislist):
    if thislist:  # Bu kontrol, liste boş ise False, dolu ise True döner.
        return True
    else:
        return False

# Örnek liste
liste = ["elma", "muz"]
print(check_list(liste))  # True çıktısı verir, çünkü liste dolu.

bos_liste = []
print(check_list(bos_liste))  # False çıktısı verir, çünkü liste boş.

