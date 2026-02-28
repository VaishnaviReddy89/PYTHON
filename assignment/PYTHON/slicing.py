#You can return a range of characters by using the slice syntax.

#Specify the start index and the end index, separated by a colon, to return a part of the string.
a="VAISHU REDDY"
print(a[0:2])#index 2 is not printing.
#SLICE FROM START
b="VAISHU REDDY"
print(b[:6])#index 6 is not printing
#SLICE TO THE END
c="VAISHU REDDY"
print(c[4:])#from index 4 the alphabets are printing
#-VE INDEX
d="VAISHUREDDY"
print(d[-4:-1])#here "E" is position -4 and "Y" is position -1 so -1 is not included