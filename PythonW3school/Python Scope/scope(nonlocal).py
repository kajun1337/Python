#The nonlocal keyword is used to work with variables inside nested functions.
#nonlocal değişkenin dış fonksiyona ait olmasını sağlar.
#aslında globalle hemen ahemen aynı goreı goruyor 

def ilkfonksiyon():
    x = "Ismail"
    def ikincifonksiyon():
        nonlocal x
        x = "Okul"
    ikincifonksiyon()
    return x

print(ilkfonksiyon())

