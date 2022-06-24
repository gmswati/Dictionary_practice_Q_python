
list1=[2,0,4,0,7,0,0,9,1]
i=0
list=[]
my_list=[]
while i<len(list1):
    
    if list1[i]!=0:
        my_list.append(list1[i])
    else:
        list.append(list1[i])
    i+=1
print(my_list.extend(list))
