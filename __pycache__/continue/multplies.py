print("NOT MULTIPLIES  5")
for i in range(1,31):
    if i % 5==0:
        continue#continue says: “Don’t print 5, 10, 15, 20, 25, 30 — skip them.”
    print(i)
    
print("MULTIPILES 5")
for x in range(1,100):
    if x%5!=0:
        continue#print 5,10,15.....
    print(x) 
    