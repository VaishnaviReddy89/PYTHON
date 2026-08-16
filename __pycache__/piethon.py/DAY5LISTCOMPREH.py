print("LIST COMPREHENSION")
phones=["apple","banana","kiwi","mango"]
new=[]
for x in phones:
    if "a" in x:
        new.append(x)
print(new)