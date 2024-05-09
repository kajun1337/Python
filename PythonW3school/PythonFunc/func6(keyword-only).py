def benim_fonksiyonum(*, x):
    print(x)

benim_fonksiyonum(x = 3)

def calculate(*, x, y):
    result = x * y
    print("Sonuç:", result)

calculate(y=5, x=3)


def pozisyonel(x,y,/):
    print(x-y)
pozisyonel(12,3)

def test1(arguman1,arguman2,opsiyonelarguman= None):
    if opsiyonelarguman is not None:
          print(arguman1,arguman2,opsiyonelarguman)
    else:
        print(arguman1,arguman2)
    

test1("gez","goz","tamirci")