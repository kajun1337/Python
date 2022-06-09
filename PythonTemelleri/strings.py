name = 'Sadık'
surname = 'Turan'
age = 36
zozo = 'My name is ' + name + ' ' + surname + '\nand I am' + str(age) + 'Yo'

lenghy = len(zozo)

print(zozo[0])
print(len(zozo))
print(zozo[lenghy -1]) # bu ifade zozo[-1] ile aynı 
print(zozo[2:7]) # 2.indexten basla 5.indexr kadar git
print(zozo[3:]) #3ten basla sonun kadar gitsin
print(zozo[:15]) #sondan basa
print(zozo[2:40:2]) #2den 40 a kadar 2 şerli atlayarak git

