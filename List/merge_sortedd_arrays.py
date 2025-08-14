# merge 2 sortedd arrays 


nums1 =[ 1,1,1,2,4,6,7]
nums2 = [ 1,2,3,6,7,8,9,10]



#merging sorted arrays 

nums3 = nums1 + nums2
nums3.sort()
print('Before sorting :',nums3)
nums3 = list(set(nums3))
print('After sorting ',nums3)