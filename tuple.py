print("%%%%TUPLE%%%%%%")
T=("VAISHU","REDDY")
print(type(T))

t=("vaishu","reddy")
print(t[1])

#slicing
tu=(1,62,3,46,5,66,"kiran")
print(tu[0:4:2])

#minmax
tup=(1,62,3,46,5,66)
print(min(tup))
print(max(tup))
print(sum(tup))
print(len(tup))

#operations
print("concatenation")
t1=(1,2,3)
t2=(3,4,5)
print(t1+t2)


print("repetation")
tupl=(1,62,3,46,5,66)
print(tupl*11)


print("Loop")
c=(1,2,3,4,5)
for x in c:
    print(x)
    
    
print("membership")
print(10 in c)
print(t1 is t2)
