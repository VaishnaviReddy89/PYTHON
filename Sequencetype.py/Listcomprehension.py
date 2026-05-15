print("normal method")
numbers=[]
for i in range(5):
    numbers.append(i)
    print(numbers)
    print("LIST COMPREHENSION")
    number = [x for x in range(5)]

print(number)