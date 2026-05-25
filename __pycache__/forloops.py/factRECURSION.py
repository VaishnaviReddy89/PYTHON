def fact(n):#we creating function fact
    if n==0 or n==1: #Base condition 
        return 1#This stops recursion
    return n *fact(n-1)
n=int(input("Enter a Number"))
print(fact(n))
#Stops at base condition (0 or 1)
'''
fact(5)
= 5 * fact(4)
= 5 * (4 * fact(3))
= 5 * (4 * (3 * fact(2)))
= 5 * (4 * (3 * (2 * fact(1))))
= 5 * 4 * 3 * 2 * 1 ← STOP POINT
= 120
'''

    