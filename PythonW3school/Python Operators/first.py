import ctypes

print(10+5)


print(20 % 3)
print(2 ** 3)
print (50 // 3)
print (50 / 3)

x = 5
# x += 3
# x -= 3
# x *= 3
x /= 3
print(x)

""" def gelensayi(parametre):
    if parametre > 0 and parametre <= 5:
        return(True)
    
    
    else :
        return(False)
     """

def gelensayi(parametre):
    if not(parametre > 0):
        return(True)
    
    
    else :
        return(False)
    

print(gelensayi(6))



memory_First = [1,"sss",4]
memory_Second= [1,"sss",4]

print(memory_First is memory_Second)
print("\n ********" ,bool(memory_Second == memory_First))

print(id(memory_First))
print(id(memory_Second))



