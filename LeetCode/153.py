
nums = [ 4,5,6,7,0,1,2]


def find_min_sorted_array(nums):
    
    n = len(nums)
    low , high = 0, n-1
    min_val = float('inf')
    
    while low <= high :
        mid = (low+high)//2
        
        if nums[mid] <= nums[high]:
            min_val = min(min_val,nums[mid])
            high = mid -1
        else:
            min_val=min(min_val,nums[low])
            low = mid +1
            
    return min_val

k=find_min_sorted_array(nums)
print(k)