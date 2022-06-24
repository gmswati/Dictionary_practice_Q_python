dict={'Adarsh':65,'Aman':45,'Gopal':85,'Gajodhar':75}
# Method - 1:
rev={}
for key in dict:
    rev[dict[key]]=key
print(rev)

# Method - 2:
dict={'Adarsh':65,'Aman':45,'Gopal':85,'Gajodhar':75}
rev={v:k for k,v in dict.items()}

# print(dict.items())
# O.p:dict_items([('Adarsh', 65), ('Aman', 45), ('Gopal', 85), ('Gajodhar', 75)])


print(dict)
print(rev)

