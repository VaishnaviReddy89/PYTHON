print("****TEXTDATATYPE******")
#It is used to store a sequence of characters such as letters, numbers, and symbols.
x= "HI PYTHON"
print(x)
print(type(x))

#Strings are immutable, meaning their characters cannot be changed after creation.

#s = "Python"
#s[0] = "J"
print("///////////////")
s = "Python"
s = "J" + s[1:]
print(s)
print("//////////////")
print("REPLACE")
s= "banana"
s.replace("b","c")
print(s)