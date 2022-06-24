# from xmlrpc.server import _DispatchArity2

# TYPE I:-

dict={2:'sapna',1:'pragati',5:'tanuja',4:'kranti',2:'jija'}
# dict2={1:'bhavna',2:'teena',3:'shruti',4:'mansa',5:'bhavna',6:'teena'}
# dict3={3:'swati',5:'pushpa',7:'tanu',4:'prit',5:'pushpa'}
# these are possiblities:

my_dict={}
# here keys and item both are keys of the same dict.
for keys in dict:
    # my_dict[keys]=dict[keys]
    for item in dict:
        if keys!=item:
            my_dict[keys]=dict[keys]
            
        else:
            pass
print(my_dict)

# # TYPE II :-

# dict2={1:'bhavna',2:'teena',3:'shruti',4:'mansa',5:'bhavna',6:'teena'}
# my_dict={}
# for keys in dict2:
#     for item in dict2:
#         if dict2[keys]!=dict2[item]:
#             my_dict[keys]=dict2[keys]
#         else:
#             pass
# print(my_dict,'*')
# # it's not working ,why?

# # TYPE III:-
# dict3={3:'swati',5:'pushpa',7:'tanu',4:'prit',5:'pushpa'}


# improve these codes?