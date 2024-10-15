ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

# for i in ikinci_metin:
#     if not i in ilk_metin:
#         print(i)
    
# Gördüğünüz gibi, döngüleri (for), bool işleçlerini (not) ve aitlik işleçlerini (in) kullanarak,
# istediğimiz şeyi rahatlıkla yapabiliyoruz.
#aynı metinleri karşılaştırarak farklı olan karakterleri bulduk tek bir kere yazdırcaz

# fark = ""
# for i in ikinci_metin:
#     if not i in ilk_metin:
#         if not i in fark:
#          fark += i
# print(fark)

# birleştirme işlemlerinin bir değiştirme işlemi olmamasıdır.

a = "Python"
print(id(a))

a = a + "Test"
print(a)
print(id(a))

""" for s in ikinci_metin:
    if not s in ilk_metin and not s in fark:
        fark += s """
#DAHA KISA 
#Burada iki farklı if deyimini iki farklı satırda yazmak yerine, bu deyimleri and işleci ile birbirine bağladık.
