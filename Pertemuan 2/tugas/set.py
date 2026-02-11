#pyton set

#access set items
thisset = {"apple", "banana", "cherry"}
print(thisset)
for x in thisset:
  print(x)
print("banana" in thisset)

#add set items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
thisset.update(["orange", "mango", "grape"])
print(thisset)

#remove set items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
thisset.discard("cherry")
print(thisset)
x = thisset.pop()
print(x)
print(thisset)
thisset.clear()
print(thisset)

del thisset
#print(thisset) #error

#loop set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
for i in thisset:
  print(i)
i = 0
for x in thisset:
  print(x)
  i = i + 1

#join set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#frozen set
thisset = frozenset({"apple", "banana", "cherry"})
print(thisset)

#thisset.add("orange") #error
#thisset.remove("banana") #error