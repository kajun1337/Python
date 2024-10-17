H#atırlarsanız döngüleri anlatırken şöyle bir örnek vermiştik:

tr_harfler = "şçöğüİı"
a = 0

while a < len(tr_harfler):
    print(tr_harfler[a], sep="\n")
    a += 1

#Bu kodların for döngüsü ile yazılabilecek olan şu kodlara alternatif olduğundan söz etmiştik:

tr_harfler = "şçöğüİı"

for tr_harf in tr_harfler:
    print(tr_harf)

