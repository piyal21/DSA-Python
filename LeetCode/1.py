class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict={}
    
        for index,values in enumerate(nums):
            complement = target-values
            if complement in new_dict:
                return [new_dict[complement],index]
            new_dict[values]=index