tuples=("apple","cherry","banana")
y=list(tuples)#convert tuple into list
y[2]="orange"
tuples=tuple(y)#convert back into list
print(y)