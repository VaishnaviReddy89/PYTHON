#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
print("convert tuple into list")
t=("apple","orange","cherry")
l=list(t)
l[1]="berry"
t=tuple(l)
print(t)

print("add item")
t=("apple","orange","cherry")
l=list(t)
l.append("berry")
t=tuple(l)
print(t)

print("tuple to tuple")
t=("apple","orange","cherry")
y=("orange",)
t +=y
print(t)


print("remove")
t=("apple","orange","cherry")
l=list(t)
l.remove("cherry")
t=tuple(l)
print(t)


