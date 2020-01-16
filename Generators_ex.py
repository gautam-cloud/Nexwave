t1=(10,20,30)
t2=(i for i in range(10))
print('T1=',t1)
print('T2=',t2)
print('LIST(T2)=',list(t2))

l=[1,2,3,4]
def squares(m):
    res=[]
    for j in m:
        r=j*j
        res.append(r)
    return res
r1=squares(l)
for a in r1:
    print('a=',a)
#if we have 100 elements in list let 100mb data thus is for loop it takes one one element but before that we create 100 object twice so we use generator so that we can crraete objects on the fly
line='-'*40
print(line)

#Generator
def gen_squares(n):
    for k in n:
         yield k*k
    for l in n:
        yield l*l
r2=gen_squares(l)
for b in r2:
    print('b=',b)
print('r1=',r1)
print('r2=',list(r2))
#yield will not create the obj but only will keep a track of all execution when u ask for the value it will generate
#we saved the space here
#It empties ALSO THUS LIST OF R2=NONE







