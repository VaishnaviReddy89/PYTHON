print("Change a Range of Item Values")
phones=["iphone","oneplus","samsung","redmi","poco","vivo"]
phones[1:3]=["nothing","realme","moto"]
print(phones)
#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
phone=["iphone","oneplus","samsung","redmi","poco","vivo"]
phone[1:3]=["nothing"]
print(phone)
#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
print("Insert items")
#To insert a new list item, without replacing any of the existing values, we can use the insert() method
list=[1,2,3]
list.insert(2,4)
print(list)
print("strings")
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 
