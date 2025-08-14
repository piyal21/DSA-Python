# --> Rotate by kth place


nums = [3,9,5,6,7,2,-10,99]

def rotate_items(nums,rotation):
    len_of_array= len(nums)
    k = rotation % len_of_array # --> Number of elements that needs to move on the right 
    
    nums[:]= nums[-k:] + nums[:-k]


r = int(input('How many rotation you want: '))
print('Before rotation:',nums)
rotate_items(nums,r)
print('After rotation :',nums)
