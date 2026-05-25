print("LIST COMPREHENSION")
#List comprehension is a short and simple way to create lists in Python using a single line of code.
print("WITHOUT LIST COMPREHENSION")
numbers=[1,2,3,4]
squares=[]
for i in numbers:
    squares.append(i+i)
print(squares)
print("WITH LIST C0MPREHENSION")
#SYNTAX:[expression for item in iterable if condition]
NUMBERS=[1,2,3,4]
add=[i+i for i in NUMBERS]
print(add)