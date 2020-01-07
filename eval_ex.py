a='10'
b=int(a)
c=eval(a)
print(a,b,c)

d='[10,20,30]'
e='hello'
f=list(e)
print(f)
g=list(d)
h=eval(d)
print(g)
print(h) #eval takles as string only and evaluates what it has inside (expression) and returns the result
)
i=10
j=20
k=eval('i+j')
print('k=',k)


