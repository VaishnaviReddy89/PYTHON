data=[1,2,2,3,3,3,4]
result={}
for i in data:
    result[i]=result.get(i,0)+1 #get(i, 0) returns the current count of i if it exists, otherwise 0, then we add 1.
print(result)
    