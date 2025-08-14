# finding 2nd largest element in an array [effective approach]
nums = [ 55,23,12,99,45,67,34,0,-34,-45]

def finding_2nd_largest(nums):
  n= len(nums)
  largest = float("-inf")
  s_largest= float("-inf")

  for i in range(0,n):
    if nums[i] > largest :
      s_largest = largest
      largest = nums[i]

    elif nums[i] > s_largest and s_largest != largest:
      s_largest = nums[i]


  return s_largest

second_largest = finding_2nd_largest(nums)
print(second_largest)