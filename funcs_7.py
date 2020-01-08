# Variable Keyword only argument
def add(a,b=10,*c,d,e,**f): #*c(variable position argument) captures extra position argument and **f(variable keyword only argument) captures extra keyword argument in form of dictionary
    print('EXTRA KEYWORD ONLY ARGUMENTS=',f)
    r=a+b+sum(c)+d+e+sum(f.values()) #as dictionary
    return r
r1=add(10,d=20,e=30)
print('r1=',r1)
print('-'*40)
r2=add(10,20,30,40,50,d=60,e=70,x=80,y=90)
print('r2=',r2)

D={'d':50,'e':60,'x':70} #30,40 goes to c
res3=add(10,20,30,40,**D)
print('res3=',res3)




