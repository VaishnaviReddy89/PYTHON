#Unpacking is used to easily extract values from a collection into separate variables.
t=(1,2,3)
a,b,c=t
print(a,b,c)
#Packing → many values into one variable
#Unpacking → one collection into many variables

def calc(x,y):
    return x+y,x-y
add,sub=calc(1,3)
