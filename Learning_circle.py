from unicodedata import name


my_list=[]
n=int(input('enter the no:'))
i=0
while i<n:
    nam=input('enter the name:')
    sur_name=input('enter the sur_name:')
    age=int(input('enter the age:'))
    dict={}
    dict['name']=nam
    dict['sur_name']=sur_name
    dict['age']=age
    my_list.append(dict)
    i+=1
print(my_list)