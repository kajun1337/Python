import re

txt = "The rain in Spain"
x = re.findall("ai",txt)
print(x)
print("******************\n")
y = re.findall("Portugal",txt)
print(y)
print("******************\n")

