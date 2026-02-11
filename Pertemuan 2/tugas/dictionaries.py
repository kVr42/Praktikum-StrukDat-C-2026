#pyton dictionaries

#access dictionary items
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)
print(thisdict["brand"])
print(thisdict.get("model"))

#change dictionary items
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["year"] = 2018
print(thisdict)
thisdict.update({"model": "Fiesta"})
print(thisdict)

#add dictionary items
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["color"] = "red"
print(thisdict)
thisdict.update({"price": 20000})
print(thisdict)

#remove dictionary items
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)
thisdict.clear()
print(thisdict)
del thisdict
  #print(thisdict) #error

#loop dictionary
thisdict = {"brand": "Ford", "model": "Mustang", "year":  1964}
for x in thisdict:
  print(x)
for x in thisdict.keys():
  print(x)
for x in thisdict.values():
  print(x)
for x, y in thisdict.items():
  print(x, y)
for x in thisdict:
  print(thisdict[x])
for i in range(len(thisdict)):
  key = list(thisdict.keys())[i]
  print(thisdict[key])
i = 0
keys = list(thisdict.keys())
while i < len(thisdict):
  key = keys[i]
  print(thisdict[key])
  i = i + 1

#copy dictionary  
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
mydict = thisdict.copy()
print(mydict)
mydict = dict(thisdict)
print(mydict)

#join dictionary
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)
dict1.update(dict2)
print(dict1)

#nested dictionary
myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}
print(myfamily)
child1 = myfamily["child1"]
print(child1)
child1_name = myfamily["child1"]["name"]
print(child1_name)
child2_year = myfamily["child2"]["year"]
print(child2_year)
child3 = myfamily["child3"]
print(child3)
child3_name = myfamily["child3"]["name"]
print(child3_name)
child3_year = myfamily["child3"]["year"]
print(child3_year)
child2 = myfamily["child2"]
print(child2)
child2_name = myfamily["child2"]["name"]
print(child2_name)
child1_year = myfamily["child1"]["year"]
print(child1_year)