print("Enter x input")
x=int(input())
print("Enter y input")
y=int(input())
print("Enter operator")
op=input()
if op=='+':
    print(x+y)
elif op=='-':
    print(x-y)
elif op=='*':
    print(x*y)
elif op=='/':
    print(x/y)
else:
    print("Invalid operator")