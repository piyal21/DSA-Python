# check if an array is sorted or not 
# Return True / False depending on it. 

def check_sorted_array(nums):
  n= len(nums)

  for i in range(0,n-1):
    if nums[i] > nums[i+1]:
      return False
    
  return True

# taking user input for array 

size = int(input('Enter the size of your array :'))
array = []
for i in range(0,size):
  k = int(input(f'Enter element {i+1}:'))
  array.append(k)

print('Your array is: ',array)
print()
p =check_sorted_array(array)

if p == True:
  print('Your array is sorted')
else :
  print('Your array is not sortedd.')

