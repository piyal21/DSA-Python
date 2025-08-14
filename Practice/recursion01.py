

count = 0 

def greet():
    global count
    if count == 5:
        return
    
    print('Hello Piyal')
    count +=1
    greet()
    
greet()


    
    

