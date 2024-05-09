def recursive(sayi):
    if(sayi != 0):
        sonuc = sayi + recursive(sayi - 1)
        print(sonuc)
    else:
        return 0
    return sonuc
print("\n recursive test")
recursive(4)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Faktöriyel hesaplama fonksiyonunu kullanarak çeşitli değerleri hesaplayabiliriz
print("\n",factorial(5))  # 5! = 5 * 4 * 3 * 2 * 1 = 120