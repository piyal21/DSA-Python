char_list = "azyxyzaaadcdcdkhdfeinsdfdkeuiiii"

find_freq_char = ['d','a','c','i','k']


hash_list = [0]*26
for i in char_list:
    ascii_val = ord(i)
    index = ascii_val - 97
    hash_list[index] +=1
    

# to check for the freq. of given list 

for i in find_freq_char:
    ascii_val1= ord(i)
    index = ascii_val1-97
    print(hash_list[index])
    