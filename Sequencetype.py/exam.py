def frequency(nums):
    d={}
    for nums in nums:
        d[nums]=d.get(nums,0)+1
    return d
print(frequency([1,2,2,3,3,1]))