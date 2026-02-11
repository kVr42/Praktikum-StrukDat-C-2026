#pyton tuples

#access tuple items
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1])

#change tuple items
thistuple = ("apple", "banana", "cherry")

#thistuple[1] = "blackcurrant" #error
print(thistuple)

#add tuple items
thistuple = ("apple", "banana", "cherry")

#thistuple.append("orange") #error
print(thistuple)

#remove tuple items
thistuple = ("apple", "banana", "cherry")
#thistuple.remove("banana") #error
print(thistuple)

#loop tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
for i in range(len(thistuple)):
  print(thistuple[i])
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  
#join tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)


