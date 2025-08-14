


# --> Tail Recursion 

count = 1

def greet():
    global count

    if count == 5:
        return

    count += 1
    greet()
    print(count)

greet()
