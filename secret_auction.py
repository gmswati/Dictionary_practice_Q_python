i=0
n=int(input('enter the no. of participents'))
dict={}
while i<n:
    name=input('enter the name of the participant:\n')
    bid_amount=float(input('enter the bidding amount:\n'))
    dict[name]=bid_amount
    i+=1
print(dict)
max=0
winner_name=''
for key in dict:
    if max < dict[key]:
        max=dict[key]
        winner_name=key
print('winner of the secret auction is',winner_name)



