phones=["iphone","Nothing","Realme"]
p=["vivo","samsung"]
g=phones+p
print(g)
phones=["iphone","Nothing","Realme"]
p=["vivo","samsung"]
phones.extend(p)
print(phones)
phones=["iphone","Nothing","Realme"]
p=["vivo","samsung"]
for x in p:
    phones.append(x)
print(phones)
    