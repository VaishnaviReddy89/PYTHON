for i in range(0,100):
    if i%2==0:
        continue
    print(i)
    '''
    1. range(1, 21)
range(1, 21)

This generates numbers from 1 to 20.

Numbers are:

1, 2, 3, 4, 5, 6, ..., 20
2. for i in range(1, 21)
for i in range(1, 21):

The loop takes one number at a time and stores it in i.

Example:

First i = 1
Then i = 2
Then i = 3
… until 20
3. if i % 2 == 0
if i % 2 == 0:

% means modulus operator (remainder).

Example:

4 % 2 = 0
5 % 2 = 1

If remainder is 0, the number is even.

So:

2 % 2 = 0 → even
4 % 2 = 0 → even
4. continue
continue

If number is even, continue skips that number and goes to the next loop.

5. print(i)
print(i)

This prints only the numbers that are not skipped (odd numbers).
'''