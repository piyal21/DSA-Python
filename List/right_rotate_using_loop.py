# Rotation using loop 

nums = [ 1,2,3,4,5]

def rotate(nums):
  n = len (nums)
  temp = nums[-1]

  for i in range(n-2,-1,-1):
    nums[i+1]=nums[i]

  nums[0]= temp
  print(nums)

print('Before : ')
print(nums)
print()
print('After :')
rotate(nums)
