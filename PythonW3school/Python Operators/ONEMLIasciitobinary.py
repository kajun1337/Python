def asci_to_binary(arg):
    y = ord(arg)
    x = bin(y)
    return x

print(asci_to_binary('a'))


def integerfunc(parametre):
    print("gelen:{}".format(parametre))
    print("gelen:{}",format(parametre))
    print(f"gelen:{parametre}")

    
integerfunc(2)