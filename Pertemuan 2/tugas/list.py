#python list
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[1:3])
print(thislist[-3:-1])
print(thislist[:2])
print(type(thislist))

#change list item
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#add list item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist.insert(1, "orange")
print(thislist)

#remove list item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist.pop(1)
print(thislist)
del thislist[0]
print(thislist)
thislist.clear()
print(thislist)

#loop list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
for i in range(len(thislist)):
  print(thislist[i])
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#list comprehension
thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in thislist if "a" in x]
print(newlist)
newlist = [x for x in thislist if x != "apple"]
print(newlist)
newlist = [x.upper() for x in thislist]
print(newlist)
newlist = [x for x in thislist if x != "apple"]
print(newlist)
newlist = [x if x != "banana" else "orange" for x in thislist]
print(newlist)

#sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
mylist = list(thislist)
print(mylist)

#join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
for x in list2:
  list1.append(x)
print(list1)
list1.extend(list2)
print(list1)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
