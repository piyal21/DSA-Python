
# list that contain values 

n = [ 5,3,2,2,1,5,5,6,7,9,3,3,6,1,3,4,4,2,10,10,4,7,7,6,8]
m = [ 10,111,1, 9,5,67,2]

hash_dict = {}


# storing frequency in the dictionary 

for i in range(0,len(n)):
    if n[i] in hash_dict:
        hash_dict[n[i]] += 1
    else:
        hash_dict[n[i]]=1

# checking the 2nd list   
for i in range(0,len(m)):
    if m[i] in hash_dict.keys():
        print('Value : ',m[i], 'Freq--',hash_dict[m[i]])
    else:
        print('Value :',m[i], ' No frequency')