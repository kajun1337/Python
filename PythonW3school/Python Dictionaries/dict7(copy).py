elite = {
"brand": "cevher",
"zoma": "koma",
"hespe": "toni"
}

myOld = elite.copy()
for key,value in elite.items():
        print(f"{key}: {value}")
#second way 

mySon = dict(elite)
print(mySon)