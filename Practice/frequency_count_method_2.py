numbers = [ 1,2,3,1,2,2,3,4,7,5,4,4,5,6,19,33,40,29]


dict_map = {}

for i in range ( 0, len(numbers)):
    dict_map[numbers[i]]=dict_map.get(numbers[i],0)+1
    
    
print(dict_map)
        
