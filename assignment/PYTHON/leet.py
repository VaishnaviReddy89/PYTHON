prices=[7,1,5,3,6,4]
max=0
for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        profit=prices[j]-prices[i]
       
        if profit>max:
           max=profit
print(max)
 