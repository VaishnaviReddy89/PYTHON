print("APPEND")
list=[1,2,3]
list.append(3)
print(list)


print("insert items")
fruits=["vaishu","reddy"]
fruits.insert(1,"ANNADI")
print(fruits)

print("extend list")
list=["apple","mango"]
lists=["kiwi","cherry"]
list.extend(lists)
print(list)

print("Add Any Iterable")
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)