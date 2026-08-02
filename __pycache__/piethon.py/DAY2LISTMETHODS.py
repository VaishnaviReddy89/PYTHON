print("list have built in methods")

#APPEND IS ADDS AN ELEMENT AT END OF LIST
CG=["B1","B2","B3"]
CG1=["B5","B6"]
CG.append("B4")
print(CG)
CG.append(CG1)
print(CG)


#it print the copy of list
CG=["b1","b2"]
c=CG.copy()
print(c)

#it return the no.of elements with specified integer values.
CG=["b1","b2"]
g=CG.count("b1")
print(g)

#add elments of a list to the end of the current list.
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

#return thr index number of value
fruits = ['apple', 'banana', 'cherry']
x=fruits.index("apple")
print(x)

#adds element at specified element.
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1,"avacado")
print(fruits)

#removes the element at specified position
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

#remove the specified value
fruits = ['apple', 'banana', 'cherry']
fruits.remove("apple")
print(fruits)

#reverse the order list.
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

#sort the list.
fruits = ['mango', 'banana', 'cherry']
fruits.sort()
print(fruits)