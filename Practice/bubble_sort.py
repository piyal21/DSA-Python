# -> Bubble sort / Adjacent sort[swap]
# ->Time complexity : O((n*(n+1))/2) or |  O(n^2) -> Avg/ Worst case
# -> Best case : O(n^2)


nums = [ 5,8,1,6,9,2,4,10]
print(len(nums))

def bubble_sort(nums):
    
    n =len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]= nums[j+1],nums[j]
    print(nums)
    
bubble_sort(nums)