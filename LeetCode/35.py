# --> leetcode 35 . 
# --> Search Insert Position



nums = [1,3,5,6]



def lowerBound(nums,target):
    n = len(nums)
    lb = n 
    low = 0 
    high = n-1
    
    while low <= high:
        mid = (low+high)//2
        
        if nums[mid] >= target:
            lb = mid
            high = mid -1 
            
        else:
            low = mid +1
            
    return lb

k = lowerBound(nums,5)
print(k)