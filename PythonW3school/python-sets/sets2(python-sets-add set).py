network = {"apple", "banana", "cherry"}
for i in network:
    print(i)

print("banana" in network) #True döner
print("banana" not in network) # False döner
#add method

network.add("matlab")
print(network)

#update method through
tropik = {"apple", "banana", "cherry"}
tropik2 = {"pineapple", "mango", "papaya"}
tropik.update(tropik2)
print(tropik)

#Farklı türleri tercih ettik

mebbis = {"apple", "banana", "cherry"}
nasreddin = ["kiwi", "orange"]

mebbis.update(nasreddin)

print(mebbis)