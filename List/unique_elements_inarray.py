# remove duplicate element from an sorted array 

nums = [ 1,1,1,2,2,3,4,4,5,7,9,9,10]

def remove_duplicates(nums):
  n = len(nums)
  if n == 1 :
    return 1 

  i = 0 
  j = i+1
  
  while j < n :
    if nums[j] != nums[ i]:
      i+=1 
      nums[i], nums[j] = nums[j],nums[i]
    
    j+=1

  return i+1

k = remove_duplicates(nums)
print(k) # --> Here k is the number of unique elements in the array. 

