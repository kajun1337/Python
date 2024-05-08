i = 0
while i < 6:
    print(i)
    
    if i == 4:
        print("dongu kirildi")
        break
    i = i + 1

i = 0


""" İlk kod parçasında sonsuz döngüye girmenin nedeni continue ifadesinin, 
i değişkeninin artırılmasını
(increment) atlayarak döngünün başına dönmesine sebep olmasıdır. """

while i < 5:
    print("*" + str(i))
    if i == 3:
        continue # # i += 1 atlanıyor ve sonsuz döngüye giriyor
    i += 1

    


