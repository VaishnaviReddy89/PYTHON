lst=[10,20,30,40,40]
new_lst=[] #create empty list to store unique values
for x in lst:
    if x  not in new_lst:
        new_lst.append(x) #We add the element only if it is not already there.  
print(new_lst)
        