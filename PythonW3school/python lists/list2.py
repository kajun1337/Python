def hakan(avo):
    if "cherrX" in avo:
        return True
    else:
        return False


thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

secondarylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(secondarylist[2:5])
print("\n ***********",secondarylist[4:])
print("\n ***********",secondarylist[:5])

print("\n ***********",secondarylist[-3:-1])

if "banana" in secondarylist:
    print("OK!")
else:
    print("NO")

print(hakan(secondarylist))
