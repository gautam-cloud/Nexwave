#List class
l1=list([10,20,30])
l2=[10,12.5,'python',['a','b']]
print(l2)
print(l2[1])
print(l2[2][1])
print(l2[-1:1:-1])

#add
l2.append(200)
print('append=',l2)
l2.insert(2,300)
print('Insert is',l2) #2nd position insert

l3=[10,20]
l4=['a','b']
l5=l3+l4
l6=l3*10
print(l5,l6,sep='\n')
l3.extend(l4)
print('extend=',l3)

#Remove

r1=l5.pop()
print('r1=',r1,l5)
r2=l5.pop(2)
print('r2=',r2,l5)
r3=l5.remove(20)
print('remove=',r3,l5)
del l5[0]
print('After del=',l5)

#update
print('l3 is',l3)
l3[1]='java'
print('After update=',l3)



#some other methods
l6=[10,30,20]
l6.sort() #aSC
print('sORT ASC=',l6)
l7=['Z','A','B']
l7.sort(reverse=True) #Desc
print('sort desc=',l7)
l8=[10,'a',20,'b']
l8.reverse()
print('reverse is',l8)


l8.clear()
print('l8 is',l8)


#Copy
l=[10,['a','b']]
m=l #reference copy
n=l.copy() #shallow copy

#Copy module
import copy
p=copy.deepcopy(l)
print(id(l[0]),id(p[0]))
print(id(l[1]),id(p[1]))      

cp=copy.deepcopy
q=cp(l)



   
