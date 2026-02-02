print("$$$$$$RemoveDuplicates$$$$$$$$$")
lst=[1,1,2,3,3,4,5]
new_lst=[]
for x in lst:
    if x  not in new_lst:
        new_lst.append(x)
        
print(new_lst)
        