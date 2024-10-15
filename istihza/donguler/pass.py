while True:
    sayı = int(input("Bir sayı girin: "))

    if sayı == 0:
        break

    elif sayı < 0:
        pass

    else:
        print(sayı)
# pass ifadesi bir bloğun hiçbir işlem yapmadan sona ermesini sağlar.
# pass deyimini kodlarınız henüz taslak aşamasında olduğu zaman da kullanabilirsiniz.
# Örneğin, diyelim ki bir kod yazıyorsunuz. Programın gidişatına göre, bir noktada
# yapmanız gereken bir işlem var, ama henüz ne yapacağınıza karar vermediniz.
# Böyle bir durumda pass deyiminden yararlanabilirsiniz. 
