import platform
import datetime

# print(platform.processor())
x = datetime.datetime.now()
print(x)

y = datetime.datetime.now()

print(y.year)
print(y.strftime("%A"))
