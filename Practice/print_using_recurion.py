# --> Printing 1-N using recursion 

def print1toN(i,n):
    
    if i>n:
        return
    print(i)
    print1toN(i+1,n)
    


k = int(input('Enter N th value : '))
print1toN(1,k)