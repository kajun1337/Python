#starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(4):
    print(x)
print("\n **********")
for y in range (2,6): # its mean -> 2,3,4,5
    print(y)


print("\n **********")
for z in range (1,8,2): # 1-den 7 ye kadar 2 şer artarak 
    print(z)
print("\n **********")

for muti in range(6):
  print(muti)
else:
  print("Finally finished!")

print("\n **********")
#The else block will NOT be executed if the loop is stopped by a break statement.
for her in range(6):
  if her == 3: break
  print(her)
else:
  print("Finally finished!")
  


