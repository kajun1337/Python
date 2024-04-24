
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))


print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class testclass():
    def __len__(self):
        return 0

print("///////////////////////////////////")
ehli = testclass()
print(bool(ehli))