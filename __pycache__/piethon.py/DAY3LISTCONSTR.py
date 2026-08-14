print("LIST CONSTRUCTOR")
"""
python provides a built-in function called list(). It is called the list constructor because it can create a new list from another iterable (such as a tuple, string, set, etc.)
"""
fruits=list(("vaishu","reddy"))
print(fruits)

print("covert a string into list")
name="VAISHU"
n=list(name)
print(n)

print("CREATE EMPTY LIST ")
n=list()
print(n)

print("convert range to list")
ra=list((range(1,6)))
print(ra)

print("convert set to list")
se=list({"vaishu","reddy"})
print(se)