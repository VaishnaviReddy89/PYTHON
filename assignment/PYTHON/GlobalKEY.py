#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

#To create a global variable inside a function, you can use the global keyword.
def var():
 global x;
 x="AWESOME"
var()
print("VAISHU IS "+ x)

y="beautiful"

def func():
    global y;
    y="classy"
  
func()
print("BMW IS "+y)
  