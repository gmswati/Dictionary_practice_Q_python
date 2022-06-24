# sort python Dictionaries by keys or values:
d={'Adarsh':65,'Aman':45,'Gopal':85,'Gajodhar':75}
print(d.keys())
# O/p: dict_keys(['Adarsh', 'Aman', 'Gopal', 'Gajodhar'])

print(d.values())
# O/P: dict_values([25, 45, 85, 75])

#sort by keys:
#list=sorted(kise, kis tarah se)
list1=sorted(d.items(),key=lambda x:x[0])

# here key is not dictionary's key this key is telling that kise key bna kar short krni h.
#means main attention kise deni h.
#sort by values:
list2=sorted(d.items(),key=lambda x:x[1])

print('Original Dictionary=',d)
print('sort by keys=',list1)
print('sort by values=',list2)
