# check for palindrome using recursion 


user_input=str(input('Enter a string to check for palindrome: '))
x = user_input 

def check(a,l,r):
    if l>= r :
        return True
    if a[l] != a[r]:
        return False
    
    return check(a,l+1,r-1)

k=check(x,0,len(x)-1)
print(k)
        
    
    
 