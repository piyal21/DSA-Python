
# -> Time Complexity O(N log N)



nums = [ 3,2,6,7,9,9,4,5,10,1,4,15,30,5,8,8,2]
 
def merge_sort(arr):
    
    if len(arr) <=1 :
        return arr
    
    mid = len(arr)//2
    left_arr = arr[:mid] # 0--> mid
    right_arr = arr[mid:] # mid --> end 
    
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    
    return merge_array(left,right)
    
# merging two sorted arrays  
def merge_array(left, right):
     
    n,m = len(left),len(right)
    i,j=0,0
    result_array =[]
     
    while i < n and j < m:
        if left[i] <= right[j]:
            result_array.append(left[i])
            i +=1 
        else:
            result_array.append(right[j])
            j +=1      
    if i<n:
        while i < n:
            result_array.append(left[i])
            i+=1      
    if j<m:
        while j<m:
            result_array.append(right[j])
            j+=1     
    return result_array


sorted_nums = merge_sort(nums)
print(sorted_nums)
