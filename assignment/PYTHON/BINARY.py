arr=[2,5,9,10,12,14]
t=10
left=0
right=len(arr)-1
while left <= right:
    
    mid=(left+right)//2
    if arr[mid] == t:
      print("Found at index", mid)
      break
  
    elif arr[mid]<t:
        left=mid+1
         
    else:
        right=mid-1