#!/usr/bin/env python
# coding: utf-8

# In[23]:


#multiple objects can be created in a class as compared to functions
#inheritance
#operator overloading
#just to differentiate between functions inside and outside the class; they are known as methods(inside) and function(outside)
#types of variables: local, enclosed, global, instance, class variables 

class Account1:
    def adduser(self,n): #self-> is like this(java); to identify the current object
        self.name=n
        
    def viewuser(self):
        return self.name
    bank='ICICI' #class variable; if you try to modify it will affect all the instances->like a static variable
    
    @classmethod #decorator
    def bankrules(cls,area):
        return 'Bank Rules: '+area
    
    @staticmethod
    def bankinfo(): #static method since don't want to pass any arguments
        return 'Bank_Info'
    
    def __init__(self): #like a constructor; only one __init_ in a class
        print('SB LOGIC HERE')
        
    
cust1=Account1() #simply call the class; it will create object. 1) creating the object-> __new__ 2) initializing the object-> __init__
cust2=Account1()
cust1.adduser('c1') #calling of the method-> adduser(cust1,'c1')
cust2.adduser('c2')
print(cust1.viewuser())
print(cust2.viewuser())

#adduser, viewuser written with self to identify the current object; since it needs to work with multiple objects, it is known as instance methods
#name-> instance variable; to store the data for multiple objects

#2 types of objects:
#1. instance object
#cust1,cust2-> instance objects
#2. class object is only one, with the class name
#Account1-> class object

print(Account1.bank) #to access
print(cust1.name)
print(Account1.bankrules('Blr'))
print(Account1.bankinfo())
print(Account1.viewuser(cust2))

class Account2(Account1):#Inheritence
    def addadhar(self,a):
        self.adhar=a
    def viewadhar(self):
        return self.adhar
    #If we want to mak changes in some existingh method creting method with new name is not a good idea thus we follow polymnorphism
    def viewuser(self):
        return 'Welcome'+self.name
    def __init__(self): #Here init of sub class will run , ignoring the superclass init 
        super().__init__()#There are two ways to run both 
        print('CA LOGIC HERE')
        #2nd way 
        Account1.__init__(self)
    

cust3=Account2()
cust3.adduser('C3')
print(cust3.viewuser())
print(Account2.bank)
print(Account2.bankrules('BLR'))
print(Account2.bankinfo())
cust3.addadhar('a1')
print(cust3.viewadhar())



class RBI:
    def viewrules(self):
        return 'RBI rules'
#Multiple Inheritence 
class Account3(Account2,RBI): #Here Diamond problem doesnot come as it search for method 1st in current class then see for mentioned class in Left to Right oreder
    pass

cust4=Account3()
print(cust4.viewrules())#Will serach current class,not found then Account2 ,not found hen Account1 ,not found hen RBI
cust4.adduser('c4') 


class Govt:
    def viewrules(self):
        return 'Govt rules'
    
class Account4(Account3,Govt):
    pass
cust5=Account4()
print(cust5.viewrules())#it shows RBI Rules bt we want Govt rules too
print(Govt.viewrules(cust5))
#OR
class Account5(Account3):
    def __init__(self):
        self.gov=Govt()
cust6=Account5()
print(cust6.viewrules())
print(cust6.gov.viewrules()) 


class Account6:
    def __init__(self,n):
        self.name=n
    def __add__(self,x):
        return self.name+x.name
    def __str__(self):
        return self.name
    def __len__(self):
        return len(self.name)
    def __iter__(self):
        self.count=0
        return self
    def __next__(self):
        c=self.count
        if c<len(self.name):
            self.count+=1
            return self.name[c]
        else:
            raise StopIteration
            
    
        
        

cust7=Account6('abc')
cust8=Account6('xyz')
result=cust7+cust8#it works as cust7__add__cust8
print('result=',result)
print('cust7=',cust7)#it gives object refernce but we want name thus we use __str__ 
print('cust7=',cust7)
print('Length=',len(cust7))# we get error on this use __len__

for i in cust7: #For the first time it executes iter then for every iteration it executes next, return c means it will return to the same object
    print('i=',i) #This give error so we need to call two method for any object to make itirable

#ABSTRACT CLASS
from abc import ABC,abstractmethod#to create abstract class there are two steps  
class Account(ABC):#1.Make this class as subclass of ABC
    def adduser(self,a):
        self.name=a
    @abstractmethod#2.make abstract method #abstract class has one or more abstract method
    def viewuser(self):
        pass
        #return self.name #we cannot provide a implementation to this method as this depends on person to person what they want to print
        
    
#a=Account()#It allows to create the obj even if implementation of all function is not provided so to put rtestrictions we use abstract class

class MyAccount(Account):
    def viewuser(self):
        return 'Hello'+self.name
    
b=MyAccount()
b.adduser('B')
print(b.viewuser())


# In[ ]:





# In[ ]:




