#GLOABL KEYWORD
a="high level"
def myfunc():
    global a
    a="not low level"
    #print("python is " + a)
myfunc()
print("python is " + a)
