d={"a":1,"b":2}
#get access
print("GET")
print(d.get("a"))
print(d.get("b"))
print(d.get("c",0))
#update
print("UPDATE")
d.update({"a":100})
print(d)
#loop
print("LOOP")
for k,v in d.items():
    print(k,v)
#pop
print("POP")
d.pop("a")
print(d)