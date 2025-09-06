# --> Search in rotated sorted array


nums=[17,18,20,1,3,4,5,7,8,10,11,14,15,16]
indx=[0,  1, 2,3,4,5,6,7,8, 9,10,11,12,13]



def SearchRotated(nums,target):
    n = len(nums)
    low , high = 0, n-1

    while low <= high:
        mid = (low+high)//2
        
        if nums[mid] == target:
            return mid
        
        if nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid +1
            
            else:
                high = mid -1 
        else:
            if nums[low] <= target <=nums[mid]:
                high = mid -1
            else:
                low = mid +1 

    return -1

k=SearchRotated(nums,20)
print(k)