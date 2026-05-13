print("FIND SUM OF NUMBERS FROM 1 TO N")
n=int(input("Enter Number:"))
sum=0#to store the total
for i in range(1,n+1):
    #Why n + 1?
    #Because range() does not include the ending number.
    sum+=i#sum = sum + i
    print(sum)
#calculate the total of consecutive numbers.