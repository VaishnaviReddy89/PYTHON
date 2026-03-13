tuples=("apple","cherry","banana")
y=list(tuples)
y[2]="orange"
tuples=tuple(y)
print(y)