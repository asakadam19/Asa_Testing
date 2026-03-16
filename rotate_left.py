def rotoneleft(nums):
    
    first = nums[0]
    
    for i in range(len(nums)-1):
        nums[i] = nums[i+1]
    nums[-1] = first
    
    return nums

def fullrotleft(nums,k):
    
    l = len(nums)
    
    for i in range(k):
        rotoneleft(nums)
    
    return nums

nums = [1,2,3,4,5,6,7]
k = 2 
print(fullrotleft(nums,k))