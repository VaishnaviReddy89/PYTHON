data=[1,2,2,3,3,3,4]
result={}
for i in data:
    result[i]=result.get(i,0)+1
    print(result)
    