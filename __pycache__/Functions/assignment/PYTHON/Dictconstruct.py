print("DICT CONSTRUCTOR")
#dict() is useful when you need to create a dictionary dynamically or convert other data into a dictionary.
#zip(pairs)
keys=["name","age"]
values=["Vaishu",20]
d=dict(zip(keys,values))
print(d)
#INPUT
key=input("ENTER KEYS: \n").split()
value=input("ENTER VALUES \n").split()
c=dict(zip(key,value))
print(c)