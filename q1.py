# dict={1:['a','b','c'],2:['d','e','f'],3:['g','h','i']}
# for k in dict:
#     print(k,':',dict[k][2])


# dict={1:['swati'],2:['poonam']}
# for keys in dict:
#     print(keys,':',dict[keys][0][4])


i=0
n=int(input('enter the no. of data you want in your dict:'))
dict={}
while i<n:
    name=input('enter name:')
    work=input('enter your work:')
    dict[name]=work
    i+=1
print(dict)

