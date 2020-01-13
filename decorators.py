
def add1(a,b):
    print('Result is')
    print(a+b+a)
    print('End of RES')

def sub1(a,b):
    print('Result is')
    print(a - b)
    print('End of RES')

add1(10,20)
sub1(10,20)
#Decorator is used to write the common part in functions as a common function only
#Mydecorator
def mydec(func):
    #def decorated_func(x,y):
    def decorated_func(*x,** y):
        print('Result is')
        #func(x,y)
        func(*x, **y)#x=(10,20,30 y=()
        print('End of RES')
    return decorated_func

@mydec
def add2(a,b):
    print(a+b+b)

add2(10,20)

#How @mydec works?
def add3(a,b):
    print(a+b)

f=mydec(add3)     #f pointing to decorated_func
f(100,200)
#In func add3 goes and will return to f the decorated_func and the values we pass in f goes a x and y
#Thus @ performs these all operations

@mydec
def add4(a,b,c): #WE do *x and **y in decorator to run this
    print(a+b+c)

add4(10,20,30)

