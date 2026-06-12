print("ITEMS()")
#it is important for loops.
d={"a":1,"b":2}
print(d.items())
for k,v in d.items():
    print(k,v)
c={"m1":34,"m2":40,"m3":45}
for sub,marks in c.items():
    if marks>=35:
        print(sub,marks)