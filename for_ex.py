s='python'
for a in s:
    print('a=',a)

b='java'
l=[10,20,30]
for b in l:
    print ('b=',b)
print('now a and b=',a,b)

d={'A':10, 'B':20}
for k in d:
    print('k=',k)
line='-'*40
print(line)
for k in d.keys():
    print('Keys=',k,'value=',d[k])
print(line)

for v in d.values():
    print('v=',v)
print(line)

for i in d.items():
    print('i=',i,i[0],i[1])
print(line)

for i,j in d.items():
    print(i,j)
print(line)

hosts=['h1','h2','h3']
ips=['ip1','ip2']
z=zip(hosts,ips) #Generator object
print(z) #For zip they didnot create printing in its class like list etc so we use list to print it
print(list(z)) #Single time generator
for h,p in zip(hosts,ips): #In one iteration give me one element
    print(h,p)
print(line)

r1=range(10)
r2=range(1,10)
r3=range(1,10,2)
print(list(r1),list(r2),list(r3),sep='\n')
r4=range(10,1,-1)
print(list(r4))
print(line)

for i in range(2,10,2):
    print('i=',i)
print(line)

for h in range(0,len(hosts),2):
    print(hosts[h])
#or
for h in hosts[::2]:
    print('h=',h)
print(line)

comp=['ibm','del1','sap','del2']
f=0
for i in comp:
    if i.startswith('del'):
        print('Found')
        break
if f==0:
    print('Not Found')

comp=['ibm','del1','sap','del2']
for i in comp:
    if i.startswith('del'):
        print('Found')
        break
else:                #This is for-else, if break happens it will come out of even else tooo as else is of for loop
    print('Not Found')
print(line)

for i in comp:
    if i.startswith('del'):
        print('Some Logic')
    print('Last statement of for')
print(line)

for i in comp:
    if not i.startswith('del'):
        continue
    if i.startswith('del'):
        print('Some Logic')
    print('Last statement of for')









