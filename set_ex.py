#Unordered Collection
#No Index
#No key
#Mutable
#Hold only immutable objects
#Unique Values
s={10,10,20,'py'}
print(s)

#add
s.add(30)
s.add(30)
print('add=',s)

#remove
r1=s.remove(10)
print('remove=',s,r1)
r2=s.pop()
print('pop=',r2,s)

#Set operation
s1={10,20,30,40}
s2={30,40,50,60}
s3=s1.union(s2)
s4=s1.intersection(s2)
print('Intersection:',s4)
s5=s1.difference(s2)
print('Diff:',s5)
s6=s1-s2
print(s6)  
      
