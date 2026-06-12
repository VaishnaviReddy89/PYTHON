start=int(input("enter a starting  number"))
end =int(input("enter a ending number"))
for i in range(start ,end + 1):
    print(" " * (4 - i) + "*" * (2 * i - 1))
    #Spaces: " " * (4 - 1)
    #Stars:"*" * (2 * 1 - 1)