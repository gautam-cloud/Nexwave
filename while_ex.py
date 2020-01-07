a=0
while a<10:
    print('a=',a)
    a+=1

s='python'
b=0
while b<len(s):
    print('b=',s[b])
    b+=1

l=['fn','ln','adr','a1','fn','adr','a2']
i=0
while i<len(l):
    if(l[i]=='adr'):
        i=i+1
        print(l[i])
        i=i+1
    else:
        i=i+1

j=0
while j<len(l):
    if l[j].startswith('a'):
        print('Found')
        break
    else:
        j=j+1
else:
    print("NOT FOUND")

k=0
while k<len(l):
    if not l[k].startswith('a'):
        k=k+1
        continue
    print(l[k])
    k=k+1
    print('Last statement of while')
# we dont have qa direct do-while loop we can use while true and if for that work

cart=[]
while True:
    i=input('Enter item')
    cart.append(i)
    ch=input('Quit(y/n)?')
    if ch=='y':
        print('Cart=',cart)
        break