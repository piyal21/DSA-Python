# --> Finding frequency of numbers in a list : 

# list 
numbers = [ 1,2,3,1,2,2,3,4,7,5,4,4,5,6,19,33,40,29]


dict_map = {}

for i in range ( 0, len(numbers)):
    if numbers[i] in dict_map:
        dict_map[numbers[i]] += 1
    else:
        dict_map[numbers[i]]=1
        
print(dict_map)