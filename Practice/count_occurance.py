nums = [1,2,2,3,3,3,3,3,3,5,7,8,9,10,12,12,12,12,14]

def LowerBound(nums, target):
    n = len(nums)
    lb = -1
    low, high = 0, n-1
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    return lb

def UpperBound(nums, target):
    n = len(nums)
    ub = n
    low, high = 0, n-1
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
    return ub

class Solution:
    def countOccurrence(self, nums, target):
        lb = LowerBound(nums, target)
        
        if lb == -1 or nums[lb] != target:
            return 0   # target not found
        
        ub = UpperBound(nums, target)
        return ub - lb   # count of occurrences


# Example usage
sol = Solution()
print(sol.countOccurrence(nums, 3))   #ans-> 6
  
