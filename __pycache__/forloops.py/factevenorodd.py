n=int(input("enter a number"))
fact=1
for i in range(1,n+1):
    fact*=i
    if fact %2==0:
       print("Even Factorial")
else:
    print("Odd Factorial")