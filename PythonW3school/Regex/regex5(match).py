import re 
txt = "The rain in Spain"
a = re.search("ai",txt)
print(a)
print("*****************")
b = re.search("ai",txt)
c = re.search(r"\bS\w+", txt)
test = re.search(r"ai\w+",txt) #ai den sonra gelen n yide alıyor bu sekılde
print(c.string)
print("*****************")
print(b.span())
print("*****************")
print(test.group())
print("*****************")
