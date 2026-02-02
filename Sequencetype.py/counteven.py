lst=[1,2,3,4,5,6] #creating a list
count=0 #initialize a list
for x in lst: #Take one element at a time from the list and store it in x.
    if x%2==0: #x % 2 means remainder when divided by 2.
        #If remainder is 0 → even
        #If remainder is 1 → odd
        #2 % 2 = 0 → even
        #4 % 2 = 0 → even
        #6 % 2 = 0 → even
     count+=1 #Each time we find an even number, we increase count by 1.
    print(count)
    