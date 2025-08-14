# -> Optimal solution for prime numbers 
from math import *
ui = int(input('Enter a number : '))

num = ui
prime_list = []

for i in range(1, int(sqrt(num))+1 ):
    if num % i == 0 :
        prime_list.append(i)
        
        if num//i != i:
            prime_list.append(num//i)
        
prime_list.sort()                       # --> O ( N log (N))
print(prime_list)