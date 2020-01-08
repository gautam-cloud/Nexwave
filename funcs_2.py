def add():
    a=10
    b=20
    c=a+b
    return c #sending value and from this point program execution ends, after this no code in function executes
    print('AFTER RETURN')
r1=add()
print('r1=',r1)

def add():
    a=10
    b=20
    c=a+b
r1=add()
print('r1=',r1)

def add():
    a=10
    b=20
    c=a+b
    return
r1=add()
print('r1=',r1)

def add():
    a=10
    b=20
    c=a+b
    return a,b,c
r1=add()[2] #SENDING a,b,c as a tuple
print('r1=',r1)

def add():
    a=10
    b=20
    c=a+b
    return [a,b,c] #Return as a list
r1=add()
print('r1=',r1)


def add():
    a=10
    b=20
    c=a+b
    return (a+b)/(a-b) #Can write on line expression in return
r1=add()
print('r1=',r1)



