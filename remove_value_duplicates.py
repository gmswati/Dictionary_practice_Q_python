# code for removing duplicate values:
dict_1={1:200,3:100,2:200,5:100,6:300,4:200}
req_dict={}
for i,j in dict_1.items():
    if j not in req_dict.values():
        req_dict[i]=j
print(req_dict)
print(type(dict_1.values()))