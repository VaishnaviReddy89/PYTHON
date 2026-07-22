x=str(2)
y=int(2)
z=float(2)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

#GLOBAL VARIABLES
a="high level"
def myfunc():
    a="not low level"
    print("python is " + a)
myfunc()
print("PYHTON IS "+ a)