
# list that contain values 

n = [ 5,3,2,2,1,5,5,6,7,9,3,3,4,2,10,10,4,7,7,6,8]
m = [ 10,111,1, 9,5,67,2]


hash_list = [ 0]*11 

for i in n:
    hash_list[i] +=1
    
for i in m:
    if i < 10 or i > 10:
        print(0)
    else:
        print(hash_list[i])
    
for i in hash_list:
    print('value :',hash_list[i],'--- Frequency : ',i)
    
    