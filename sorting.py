dict1={'Ankush':500,'Prant':398,'Suhani':700,'Anmol':678}
dict1['Ankush']

# sorting A Dictionary In Python By Key:-
# Method-1:

# for stu in sorted(dict):
    # print(stu)
    # print(stu,dict[stu])

# Method-2:-
for stu,val in sorted(dict1.items()):
    print(stu,val)
print(sorted(dict1))

print(sorted(dict1.items()))

# to get sorted dict:
# M-1
print(dict(sorted(dict1.items())))

# M-2:
# sorted_dict=dict(sorted(dict1.items()))
# print(sorted_dict)


#--------------------------------------------------------------------------------#

# sorting A Dictionary In Python By Value:-

        