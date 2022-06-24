a={1:500,2:300,3:400}
# print(a.get(1))
b={4:700,5:700,7:300}
c={8:200,9:234}

dict={}
for key in a:
    dict[key]=a[key]
for key in b:
    dict[key]=b[key]
for key in c:
    dict[key]=c[key]
print(dict)

# Q.2
# n=int(input('enter the no. of elements do you want in your dict:\n'))
# dict={}
# i=0
# while i<n:
#     key=input('enter the desired key:')
#     value=input('enter the desired value:')
#     dict[key]=value
#     i+=1
# print(dict)

# a={"1":["a","b"],"2":["c","d"]}
# for i in a["1"]:
#     for j in a["2"]:
#         print(i+j)


# from operator import le


# from itertools import count


# d=[{'a':100},{'b':200},{'c':300},{'e':200}]

# a=list(d.values())
# b=list(d.keys())

# dict={}
# for i in b:
#     for j in a:
#         dict[j]=i
# print(dict)

# Q.2

# dict={}
# i=0
# l=len(d)
# while i<l-1:
#     j=i+1
#     while j<l:
#         for item_1 in d[i]:
#             for item_2 in d[j]:
#                 if d[i][item_1]!=d[j][item_2]:
#                     dict[item_1]=d[i][item_1]
#                 else:
#                     pass
#         j+=1
#     i+=1
# print(dict)

# dict_1={'a':100,'b':200,'c':700}
# count_1=0
# for key in dict_1:
#     count_1+=1
#     # print(key,' ',value,' ',count_1)
#     print(key,end=' ')
#     print(dict_1[key],end=' ')
#     print(count_1)
    

# a={'1':['a','b'],'2':['c','d']}
# list_values=list(a.values())
# for i in list_values[0]:
#     for j in list_values[1]:
#         print(i,end='')
#         print(j)


a={'s   001':['M','S'],'s    002':['M','s','e'],'s003':['M','S']}
dict={}
for key in a:
    k=''
    for l in key:
        # print(l)
        if l==' ':
            pass
        else:
            k+=l
    dict[k]=a[key]
print(dict)