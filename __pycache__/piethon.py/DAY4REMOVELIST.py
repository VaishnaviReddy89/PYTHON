print("REMOVE METHOD")
#The remove() method removes the specified item.
list=["apple","orange","kiwi"]
list.remove("apple")
print(list)
print("POP METHOD")
#The pop() method removes the specified index.
list=["apple","orange","kiwi"]
list.pop(2)
print(list)
#If you do not specify the index, the pop() method removes the last item.
phones=["iphone","realme","apple"]
phones.pop()
print(phones)
print("DELETE KEYWORD")
#The del keyword also removes the specified index:
LIST=["FRUITS","KIWI"]
del LIST[0]
#The del keyword can also delete the list completely.
print(LIST)         
#The clear() method empties the list.
LIST=["FRUITS","KIWI"]
LIST.clear()
print(LIST)