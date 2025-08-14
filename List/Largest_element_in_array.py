
# Largest element in an arrya 

nums = [ 55,23,12,99,45,67,34,0,-34,-45]


def largerst_elements(list1):
    n= len(list1)
    largest = float('-inf')
    for i in range(0,n):
        largest = max(largest,nums[i])
        
    return largest


h = largerst_elements(nums)
print(h)