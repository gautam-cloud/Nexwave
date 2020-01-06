#dict class

#In dict its not indexed, we need to provide index

#Index can be any immutable objecty like no,string

l=['python',10,'Blr']
print(l[0])

d={'course':'python','dur':10, 'loc':'Blr'}
print(d['course'])

#Unordered 
#Add or Update
d['course']=['c++','java']
print(d['course'])
#In add dont put the key it will add it

e=d.copy()

#remove it will return the deleted item as well as return the dictionary
r1=d.pop('course')
print('pop=',r1,d)

del d['dur']
print('After del=',d)

r2=d.popitem()
print('r2 is',r2,d)

#other methods
k=e.keys()
v=e.values()
i=e.items()
print(k,v,i,sep='\n')


