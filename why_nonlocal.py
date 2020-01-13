count=0
def create_acc():
    global count
    count+=1
def delete_acc():
    global count
    count-=1
create_acc()
create_acc()
count=100
delete_acc()
print('Total Accounts=',count)
#Once u use a global varaible anywhere it changes the value thus we need nonlocal variable

def acc():
    c=0
    def ca():
        nonlocal c
        c=c+1
    def da():
        nonlocal c
        c=c-1
    def ta():
        print('Total=',c)
    return ca,da,ta
x=(10,20)
x,y=(10,20)#not a tuple
f1,f2,f3=acc()
f1()
f1()
c=100
f2()
f3()