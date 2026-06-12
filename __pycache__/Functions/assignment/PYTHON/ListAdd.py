print("PYTHON ADD ITEMS")
fruits=["ORANGE","MANGO","KIWI","APPLE"]
fruits.append("PINEAPPLE")
print(fruits)
fruits=["ORANGE","MANGO","KIWI","APPLE"]
fruits.insert(0,"PINEAPPLE")
print(fruits)
print("EXTEND")
fruits=["ORANGE","MANGO","KIWI","APPLE"]
FRUIT=["GRAPES","BLUEBERRY","STRAWBERRY"]
fruits.extend(FRUIT)
print(fruits)
#Add Any Iterable
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)