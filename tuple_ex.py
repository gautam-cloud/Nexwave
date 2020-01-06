#tuple class
t1=tuple([10,20,30])
t2=(10,12.56,'python',['a','b'],(10,20))
print(t2)
print(t2[1])
print(t2[-4:4:2])
i=t2.index('python')
c=t2.count(12.56)
print(i,c)

#tuple to list
t=(10,20)
l=list(t)
print('l=',l)

#list to tuple
l=[30,40]
t=tuple(l)
print('t=',t)


