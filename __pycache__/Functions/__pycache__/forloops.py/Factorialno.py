print("Factorial of a  number")
n=int(input("enter a number:"))
fact=1
for i in range(1, n+1):#This line is used to create a loop (repetition).
#It makes Python run the same code again and again.
    fact*=i
    print(fact)