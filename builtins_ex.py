#map
l=[100,200,300,400]
def sub(i): #we want each element to be reduced by 10
    return i-10

r1=map(sub,l) # we can use it with any collection
print(list(r1))

#Filter
def filt(j):
    return j>100
r2=filter(filt,l)
print(list(r2))
#if return value is true it will return the elementb i9f condition false then ignore

#reduce
import functools as fc
def red(p,q):#it will take first two arg from the list then take one element from list and add it eith previous sum
    return p+q
r3=fc.reduce(red,l)
m=['W','E','L']
r4=fc.reduce(red,m)
print(r3,r4)

#lambda functions
#Function without name
#Single liner
#we can embedd it in function arguments/list/tuple/dictionary only without defining it first earlier
r5=map(lambda i: i-10,l)
r6=filter(lambda j: j>100,l)
r7=fc.reduce(lambda p,q: p+q,m)
print(list(r5),list(r6),r7,sep='\n')

#LAMBDA FUNCTION WE CAN ASSIGN TO VARIABLE ALSO
f=lambda a,b:a+b
r8=f(10,20)
print('R8 IS',r8)

l=[(lambda i:i*i) (a) for a in range(10)]
print('L IS',l)
#This a will go to i


keys=['A','B']
values=[10,20]
d={k:(lambda i:i*i)(v) for k,v in zip(keys,values)}
print('D=',d)
#Frameworks are used to create websites
#Frameowrk(bottle, flask, django, pyramid, web2py, faLcon are all frameworks
    #Bottle,Falcon and Flask are micro frameworks.
    #Django and Web2py are for highly scalable applications
    #MVC(MODEL VIEW CONTROLLER)
    #Pyramid and web2py implement MVC
    #MVC (MODEL VIEW TEMPLATE) , Django is MVT
    #Pyramid is for middle level applications
    #Falcon is for creating API's only.
  #Generally three things required to develop a web application- webserver, database and browser ; in frameworks its not required.
  #Simple Object Access Protocol(SOAP, an architecture)-secure way of sharing data by creating a separate program to ensure access of only relevant details instead of details of entire server(for eg bookmyshow accessing db of pvr)
    #drawbacks of SOAP-needs to follow separate rules in order to implement this, leading to difficulties.
    #Representational State Transfer(REST)-To overcome difficulties encountered while implementing SOAP, it doesnt implement its own protocol,makes use of http only to send and receive requests.





