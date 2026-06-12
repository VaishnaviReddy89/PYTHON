#convert one numeric datatype to another datatype
print("$$$$$$$$ NUMBER COVERTER SYSTEM $$$$$$$$$$")

num=input("enter a number: ")#takes a number from the user
print("choose conversion type")
print("1.convert to integer")
print("2.convert to float")
print("3.convert to complex")

choose=int(input("enter your choice(1/2/3): "))#user enters 1 2 or 3

if choose == 1:
 print(int(float(num)))
 print("integer value:" ,num)
elif choose ==2:
    print(float(num))
    print("float value:" ,num)
elif choose ==3:
    print(complex(float(num)))
    print("complex value:" , num)
else:
    print("invalid choice")