print("DICTIONARY METHODS")

print("GET")
d = {"name": "Vaishnavi", "age": 21}
print(d.get("name"))     
print(d.get("city"))     
print(d.get("city", "India")) 

print("KEY")
print(d.keys())  

print("Values")
print(d.values())

print("ITEMS")
print(d.items())  
 
for k, v in d.items():
    print(k, v)
    
print("UPDATE")
d.update({"age": 22, "city": "Hyderabad"})
print(d)

print("POP")
d.pop("age")
print(d)

print("POPITEMS")
d.popitem()

print("COPY")
d2 = d.copy()

print("SET DEFAULT")
d = {"name": "Vaishnavi"}

d.setdefault("age", 21)
print(d)

print("CLEAR")
d.clear()