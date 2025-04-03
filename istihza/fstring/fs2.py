# fstring
isim = "Halit"
soyIsım = "Falyalı"

print(f"Merhaba {isim} {soyIsım}!")

# Uzun yollu format kullanımı
test = 'Buğra'
yas = 18
"Onun adı {} ve o {} yaşında.".format(test, yas)

birinci_sayi = int(input('Birinci sayıyı girin: '))
ikinci_sayi = int(input('İkinci sayıyı girin: '))

print(f'Sayıların toplamı {birinci_sayi + ikinci_sayi} eder.')

# f-string ifadelerinde süslü parantezler ({}) yazılan ifadenin 
# bir operatörüdür. f-string içerisinde süslü parantez yazabilmek 
# için genel kaçış karakteri olan ters eğik çizgi (\) yerine { 
# veya } parantezi 2 defa eklenir:

fstring = "f-string"

f"{{ {fstring}: f'{{ifade}}' şeklinde kullanılır. }}"

