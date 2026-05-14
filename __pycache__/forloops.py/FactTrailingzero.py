n=int(input("enter a number:"))
count=0#This will store number of trailing zeros.
while n>=5: #suppose n =10
    
    '''
    In factorial:
2 is ALWAYS more
5 is LESS
👉 So we only count 5’s
'''

    n//=5 #10//5=2 #again 2//5=0
    count+=n#count = count + n (#count +=2)
    print(count) #print count =2
    