print("******GLOBALKEYWORD******")
#TO CREATE VARIABLE INSIDEBA FUNCTION ,YOU CAN USE THE GLOBAL KEYWORD

def python():
    global x
    x="INTERPRETED LANGUAGE"
    print("python is " + x)
python()

#A global variable is created outside a function.
#To change its value inside a function, we must use the global keyword.
#This tells Python: “This variable already exists globally; do not create a new local variable.”

#EXAMPLE
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)
