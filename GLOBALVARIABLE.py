print("*****GLOBALVARIABLE*******")
#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

x="vaishu"
def myfunc():
    print("HER NAME IS " + x)
    
myfunc()    
#Global variables can be used by everyone, both inside of functions and outside.

print("******LOCALVARIABLE*******")  
#A variable declared inside a function and used only within that function.

x="beautiful"
def vaishu():
    x="NICE GIRL"
    print("vaishu is very " + x) 

vaishu()
print("vaishu is very " + x) 

 