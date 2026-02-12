phone={
    "brand":"iphone",
    "model":17,
    "year":2025
    
}
x=phone.values()
print(x)#before change
phone["year"]=2026
print(x)#after change
#The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.