d={"a":1,"b":3}
d2=d.copy()
print(d2)
d1 = {"a": 1, "b": 2}
#d2=d1.copy()
d2 = d1

d2.update({"a":100})

print(d1)   # original
print(d2)   # copy