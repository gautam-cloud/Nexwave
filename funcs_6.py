#Keyword only Arguments #user frindly aas order of passing can be changed and if default value is there then we can skip passing value
def add(a,b=10,*c,d,e):
    r=a+b+sum(c)+d+e #D and E are keyword only argument no value will go to these unless we explicitly write the argument name
    return r #After star argument its keyword argument
res=add(10,20,30,40,50,d=3,e=5) #we need to pass d and e mandatory or else give a default value
print('Res=',res)

def telnet(*cmds,h=None,p=None):
    return 'Hello'
res2=telnet()
res3=telnet('dir')
print(res2,res3)
res4=telnet('dir',p=1,h=2)
print(res4)

#If we only want keyword only argument then use as telnet(*,h,p) thus no order is mneacassary while calling
