a = 33
b = 200
if b>a:
    print("b buyuktur a")

#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
c = 33

if b>c:
    print ("graether than")
elif a == b:

    print("equal")
else: 
    print("a is graether")

#Short Hand If
if a > b: print("tek satir test")
#ıbe statement if & else
print("A") if a > b else print("B")
#The and keyword is a logical operator, and is used to combine conditional statements:

x = 200
y = 33
z = 500
if x > y and z> y:
    print("Both conditions are True")


if x > y or x > z:
    print("At lears one of the conditions is True")

if not x > y:
    print("x is NOT greaterher than y")

#Ternary Operators

e = 330
f = 330
print("A") if e > f else print("=") if e == f else print("B")