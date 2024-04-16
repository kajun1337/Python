#value types --> string, int, float, verinin kendisiyle ilgilenilir.

x=5
y=25

x=y

y=10 #çıktı alınırsa x=25, y=10

#reference types --> list, verinin adresiyle ilgilenilir.

a = ["apple","banana"]
b = ["apple","banana"]

a=b # adresler eşitlendi. o yüzden çıktı aynı olacak.

b[0]="grape"

print(a,b) #çıktı alınırsa grape,banana ve grape,banana olur.

