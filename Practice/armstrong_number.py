from math import *

user_input = int(input('Enter number : '))

num = user_input

# digit count 
digits = int(log10(num)+1)
sum = 0 

while num > 0:
    
    last_digit = num % 10 
    sum  = sum + pow(last_digit,digits)
    num = num // 10 
    sum = int(sum)

print(sum)
if user_input == sum:
    print('Armstrong Number')
else:
    print('Not armstrong number')