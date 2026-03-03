print("APPEND")
car=["BMW","FORD","FERRARI"]#add element at the end of the list
car.append("THAR")
print(car)
car.copy()#return the list
print(car)
x=car.count("BMW")#return the no.of times the element is there in list.
print(x)
y=car.index("BMW")#return the index value of element
print(y)
cars=["m3","porsche","lamborgini"]
car.extend(cars)
print(car)

car.insert(3,"MAHINDRA")#insert the element at particular location.
print(car)
car.pop(1)#remove the element with specified postion
print(car)
car.remove("THAR")#remove the element with specified value.
print(car)
car.reverse()#Reverse the list
print(car)
car.sort()#sort the list.
print(car)
car.clear()#clear all elements.
print(car)