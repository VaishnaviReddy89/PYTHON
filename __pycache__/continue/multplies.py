print("NOT MULTIPLIES  5")
for i in range(1,31):
    if i % 5==0:
        continue#continue says: “Don’t print 5, 10, 15, 20, 25, 30 — skip them.”
    print(i)
    
print("MULTIPILES 5")
for x in range(1,100):
    if x%5!=0:
        continue#print 5,10,15.....
    print(x) 
'''
1. range(1, 31)

Numbers from 1 to 30.

2. i % 5 == 0

Checks whether the number is a multiple of 5.

A multiple of 5 means:

5, 10, 15, 20, 25, 30

Example:

10 % 5 = 0
15 % 5 = 0

If remainder is 0, it is divisible by 5.

3. continue

When the number is a multiple of 5, continue skips it.

4. print(i)

Prints all other numbers.
'''
    