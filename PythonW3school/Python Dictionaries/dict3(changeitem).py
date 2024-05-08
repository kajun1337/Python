ehlibeyt = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
ehlibeyt["year"] = 2018
zoma = "\n".join([f"{key}: {value}" for key, value in ehlibeyt.items()])
print(zoma)
ehlibeyt.update({"year": 2020})
zoma2 = "\n".join([f"{key}: {value}" for key, value in ehlibeyt.items()])
print(zoma2)