print("........Ternary operator...........")
#The ternary operator is used to write a conditional statement in a single line.
#value_if_true if condition else value_if_false
a=10
b=20
c=a if a>b else b       #Condition: a > b → False So it returns b
print(c)

print("****even or odd*****")
n=7
result ="Even" if n%2==0 else "odd"
print(result)