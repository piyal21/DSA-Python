nums = [4,6,9,12,15,33,50,59,76,88,90,93,98,100]


def binary_search(nums,low,high,target):
    
    if low > high:
        print(target,' is not found in the list')
        
    mid = (low+high)//2
    
    if nums[mid]== target:
        print(target,'found at index:',mid)
        
    elif target < nums[mid]:
        binary_search(nums,low,mid-1,target)
    else:
        binary_search(nums,mid+1,high,target)
        
        
binary_search(nums,0,len(nums)-1,88)
    
    
    
