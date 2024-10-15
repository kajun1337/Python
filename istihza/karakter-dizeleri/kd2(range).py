isim = input("isim gir:")
for i in range(0, len(isim)):
    print(isim[i])

    # Aslında bu sorunun cevabı çok basit. Uzunluğunu bilmediğiniz karakter dizileri
    # için range() fonksiyonuyla birlikte len() fonksiyonundan yararlanabilirsiniz.
    # Nasıl mı? Hemen bir örnek verelim:
    #
    # for karakter in range(len(kardiz)):
    #     print(kardiz[karakter])



while True:
    txt = input("cıkmak ıcın q")
    if txt.upper() == "q":
        exit()
    else:
        site = "www.istihza.com"
        print(site[4:11])





