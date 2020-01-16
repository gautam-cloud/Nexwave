a=10
#b=0
try:
    r=a/b
    print('r=',r)
except:
    print('Some Error')

#There can be many error like fiv by 0 or B not found so to know which error has occured write class name in except
#All classes(ZerDivsionError, Index Error) are inherited from the class Exception

try:
    r2=a/b
    print('r2=',r2)
except ZeroDivisionError:
    print('IN ZDE')
except NameError as n:
    print('NE=',n,type(n))
except (KeyError,IndexError):
    print('KE or IE')

#superclass can accept sub class exceptions
#sub class will not accept superclass exception ie opposite of inheritence
#IT WILLHANDLE ALL TYPE OF EXCEPTIONS

l=[]
try:
    print(l[1])
except Exception as e:
    print('e=',e,type(e))
#if there is no error then else and if error found then except
c=10
#d=10
try:
    r=c/d
except:
    print('In Except')
else:
    r=c/c
    print('In else',r)

#Use of else is that whatever try block is there that is for that line only, if we write all else in try then it will execute except for that code also if it finds error

#Nested try except can be written

#finally block major used for closing the connection
try:
    r=c/d
except:
    print('In except')
    #print(xyz)
finally:
    print('In finally')

#try finally
#try except finally
#try except else finally

e=10
f=0
try:
    if f==0:
        raise ZeroDivisionError#Manually raising the user defined exception
    print('stmt-100')#it will execute the 100 print statements and then raise and exception if we wish it not to happpen then we can use user defined exception
    r=e/f
except ZeroDivisionError:
    print('From Raise')

line='-' * 40
print(line)


result='Test case failed'
try:
    assert 'success' in result,'some test failed' #if assert is true then it do nothing if it is false then raise an assertion error. Some testcase fail is the message which we pass
    print('Test case Success')
except AssertionError as ae:
    print('ae=',ae)


#User defined Exception
class MyError(Exception):
    def __init__(self,m):
        self.msg=m
    def __str__(self):#if we dont write this then it will search in exception class. here we wrote it thus it will override that
        return 'Error Details:'+self.msg
try:
    if 'success' not in result:
        raise MyError('Test failed')
    else:
        print('Execution Success')
except MyError as me:
    print('me=',me)

