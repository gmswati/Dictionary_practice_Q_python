# #any(): if koi bhi ek key ki value mil jaye to ye boolean value true deta h else false return krta h.
## any function wants at list one key should be exist. 
# #e.g:
# dict={'a': 3,0:5,' ':4}
# print(any(dict))
# # O.P:a
# #if
# dict={'': 3,0:5,'':4}
# print(any(dict))
# # O.P:none
# dict={' ': 3,0:5,'':4}
# # because we added here 1 space:
# print(any(dict))
# # O.P:none

#-----------------------------------------#
## all(): all wants every key should be exist in a dictionary.the it will give true boolean value otherwise it will give u false.
# #e.g:
# print()
dict={'a': 3,7:5,' ':4}
print(all(dict))
# dict={'a': 3,6:5,7:4}
# print(all(dict))
# dict={'a': 3,0:5,0:4}
# print(all(dict))

# print()
#----------------------------------------------#
# sorted():it sorts our dictionary.
# dict={9:3,2:5,7:4}
# print(sorted(dict))

#----------------------------------------------#
# get(): it helps you to access value of that particular key.
# If value is not present in dict, 