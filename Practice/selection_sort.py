
nums = [ 5,7,8,4,1,6,9,2]

def selection_sort(l):
    
    n=len(l)
    
    for i in range(0,n):
        for j in range(i+1,n):
            if l[j] < l[i]:
                #swap values using indexes 
                l[i],l[j]=l[j],l[i]
    
    print(l)
    
    
selection_sort(nums)