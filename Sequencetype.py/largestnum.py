list=[10,20,30]
largest=list[0]
for i in list:
    if i % largest ==0:
        largest=i
print(largest)