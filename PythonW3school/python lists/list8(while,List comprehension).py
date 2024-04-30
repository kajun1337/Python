listem =  ["apple", "banana", "cherry"]
i  = 0
while i < len(listem):
    print(listem[i])
    i += 1

print("\n*",len(listem))


# Looping Using List Comprehension

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]