# --> Recursion with parameters 


#function 

def printing(x,n):
    if n == 0:
        return
    
    print(x)
    n -=1
    printing(x,n)
    
    # or we can also do this 
    # print(x)
    # printing(x,n-1)
    
    
printing('piyal',4)