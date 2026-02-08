print("create tuple with one item")
tup=("vaishu",)
print(type(tup))

print("CONSTRUCTOR")
#The use of the tuple() constructor in Python is to create or convert data like iterable into a tuple.
print("creating tuple from a list")
lst=[2,3,4]
t=tuple(lst)
print(t)
print("creating tuple from a string")
t=tuple("vaishu")
print(t)
print("creating tuple from a range")
t=tuple(range(5))
print(t)
print("creating tuple from a set")
s={1,3,4}
t=tuple(s)
print(t)
t=tuple([2])
print(t)

