nums = [ 1,2,4,0,3,0,0,3,5,1]



def move_zeros(nums):
    n= len(nums)
    i=0

    while i<n:
        if nums[i]==0:
            break 
        i+=1
    if i == n:
        return
    j= i+1 
    while j<n:
        if nums[j] != 0:
            nums[i],nums[j]= nums[j],nums[i]
            i+=1
        j+=1
    
move_zeros(nums)
print(nums)