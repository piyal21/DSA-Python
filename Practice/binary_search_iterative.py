nums = [4,6,9,12,15,33,50,59,76,88,90,93,98,100]


def binary_search(nums,target):
    
    n = len(nums)
    low = 0 
    high= n-1 
    
    while low <=high:
        mid = (low+high)//2
        
        if nums[mid]== target:
            return mid # --> index of the target value in the list
        elif target < nums[mid]:
            high = mid -1
        else:
            low = mid + 1
        
        
value_index =binary_search(nums,88)
print(value_index)
    
    
    
