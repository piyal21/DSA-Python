from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # -> upper bound function 
        def upper_bound(nums, target):
            n = len(nums)
            ub = n   
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target:
                    ub = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ub

        # -> lower bound function 
        def lower_bound(nums, target):
            n = len(nums)
            lb = n  
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= target:
                    lb = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return lb

        lb = lower_bound(nums, target)
        ub = upper_bound(nums, target)

        
        if lb == len(nums):
            return [-1, -1]
        if nums[lb] != target:
            return [-1, -1]

        return [lb, ub - 1]
