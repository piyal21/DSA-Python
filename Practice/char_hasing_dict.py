char_list = "azyxyzaaadcdcdkhdfeinsdfdkeuiiii"

find_freq_char = ['d','a','c','i','k']


hash_dict = {}

for i in char_list:
    if i in hash_dict:
        hash_dict[i] += 1 
    else:
        hash_dict[i]=1
        
        
for j in find_freq_char:
    if j in hash_dict:
        print(j, 'has freq --- ',hash_dict.get(j,0))
    else:
        print(j,'No Freq.')