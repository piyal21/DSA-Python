class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = float("-inf")
        total = 0
        
        for i in range(0,n):
            total = total + nums[i]
            max_val = max(max_val,total)
            
            if total < 0:
                total = 0
                
        return max_val