# right rotate an array by one place 

nums = [ 5,-2,3,9,0,6,10,7]

def right_rotate_array(nums):
  n = len(nums)
  nums[:]= [nums[n-1]] + nums[0:n-1]
  return nums


print('Array before right rotation : ',nums)
print()
k = right_rotate_array(nums)
print('Array after right rotation : ',k)
