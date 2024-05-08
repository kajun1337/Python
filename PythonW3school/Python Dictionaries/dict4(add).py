# 1 way directly
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red" #1.yontem
zoma = "\n".join([f"{key}: {value}" for key,value in thisdict.items()])
print(zoma)
thisdict.update({"model": "toyata"})
zoma = "\n".join([f"{key}: {value}" for key,value in thisdict.items()])
print(zoma)
