print("Loop through a list")
name=["vaishu","Reddy"]
for i in name:
    print(i)

print("FROM 0 TO 100")
for i in range(100):
  print(i)

print("from start to stop")#stops before stop value.
for z in range(0,55):
    print(z)
    
print("from start to stop and step")
for l in range(0,55,3):
    print(l)
    
'''
start = 1
stop = 11
step = 2 (jump by 2
'''
print("loop through a string")
name = "Python"
for ch in name:
    print(ch)
    
print("Even Numbers")
for e in range(2,11,2):
    print(e)

print("Odd Numbers")
for o in range(1,11,2):
    print(o)
    
print("for loop with if")
for p in range(1, 6):
    if p == 3:
        print("Found")
print("break in for loop")
for b in range(1, 6):
    if b == 3:
        break
    print(b)
    
print("break in for loop")
for q in range(1, 6):
    if q == 3:
        continue
    print(q)
print("continue in for loop")
for k in range(1, 6):
    if k == 3:
        continue
    print(k)