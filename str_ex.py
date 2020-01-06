a='Person'
print(a)
b="Person's"
print(b)
c="""Person"""
print(c)
d='''Person's Height XYZ'' '''
print(d)
s1='hello'
s2='py'
s3=s1+s2
s4=s1*10
print(s3,s4)
line='-'*10
print(line)
e='person\'s'
print(e)
f=r'C:\Python Training\test.py' #raw string
print(f)
g='WEL COME'
print(g)
print(len(g)) #length of any collection
print(g[7]) #print char at defined no
#SLICING
print(g[1:6]) #slicing or substring
print(g[1:]) 
print(g[:6])
print(g[:]) #print full string
h=g[:]
print(id(h),id(g))
#Step
print(g[1:6:1]) #STEP DEFAULR IS 1 ONLY
print(g[1:6:2])
#reverse
print(g[::-1])
print(g[6:1:-2])
#-VE INDEX
print(g[-7:-2])
#Reterive last 4 char using +ve index
print(g[len(g)-4:])
#Reterive last 4 char using -ve index
print(g[-4:])
#Str class
i=10
j=str(i)
k=str('python')
print(i,j,k,sep='\n')

r1=g.startswith('Wel')
print('R1=',r1)
r2=g.endswith('ME')
print('R2=',r2)

r3=g.isupper()
r4=g.upper()
print(r3,r4)
r5=g.islower()
r6=g.lower()
print(r5,r6)

l='abc'
r7=l.isalpha()
m='123'
r8=m.isdigit()
n='abc123'
r9=n.isalnum()
print(r7,r8,r9)

r10=n[-3:].isdigit()
print(r10)

r11=g.count('E')
print('No of occurance of E =',r11)

r12=g.index('E')
r13=g.find('E')
print(r12,r13)
r14=g.index('E',3)
r15=g.index('E',3,8) #8 is exclusive
print(r14,r15)
r16=g.rindex('E')
print('r16=',r16)
p='   WEL COME    '

r17=p.strip()
r18=p.lstrip()
r19=p.rstrip()
print(r17,r18,r19,sep='\n')

q='[wel[come][]'
r20=q.strip(']w[e')
print(r20)
r21=q.lstrip('w[')
r22=q.rstrip('][e')
print(r21,r22)

r23=g.replace('E','e')
print(r23)

r24=g.split()
print(r24)
r25=g.split('E')
print(r25)

x=10
y=20
z=x+y
r26='add of x and y is z'
r27='add of {} and {} is {}'.format(x,y,z)
print(r26,r27)
r28='add of {1} and {0} is {2}'.format(x,y,z)
print(r28)


r29=f'add of {x} and {y} is {z}'
print(r29)

r30='-'.join(g)
r31='xyz'.join(r24)
print(r30,r31)
