myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

""" Create three dictionaries, then create one 
dictionary that will contain the other three dictionaries: """

myfamily2 = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  },
}


print(myfamily2["child1"]["name"],myfamily["child2"]["year"])

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])