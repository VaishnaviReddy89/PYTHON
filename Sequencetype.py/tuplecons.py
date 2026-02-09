print("%%%%TUPLECONSTRUCTOR%%%%")
#The tuple() constructor is a built-in function used to convert other iterable data types into a tuple.
print("LIST TO TUPLE")
l=[10,20,30]
t=tuple(l)
print(t)
print("/////////////////////")
print("STRING TO TUPLE")
S="python"
t=tuple(S)
print(t)
print("//////////////////////")
print("SET TO TUPLE")
s={1,2,4}
t=tuple(s)
print(t)
print("/////////////////")
print("RANGE TO TUPLE")
r=range(6)
t=tuple(r)
print(t)
print("////////////////////")
print("DICTIONARY TO TUPLE")
d={1:'a',2:'b'}
t = tuple(d)
print(t)
