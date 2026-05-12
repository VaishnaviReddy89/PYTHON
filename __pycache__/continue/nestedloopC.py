#A nested loop means loop inside another loop.
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue
        print(i, j)
'''
i = 1
j = 1 → print (1,1)
j = 2 → continue → skip
j = 3 → print (1,3)

i = 2
j = 1 → print (2,1)
j = 2 → skip
j = 3 → print (2,3)

i = 3
j = 1 → print (3,1)
j = 2 → skip
j = 3 → print (3,3)
'''