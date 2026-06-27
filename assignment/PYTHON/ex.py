nums=[10,4,8,3]
leftside=[]
leftsum=0
right=sum(nums)
for i in nums:
    right-=i
    v= abs(leftsum-right)
    leftside.append(v)
    leftsum+=i
print(leftside)