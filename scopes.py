#LOCAL ENCLOSED GLOBAL BUILTINS
x=10
def f1(): #f1 and f2 are objects too
    x=20 #Enclosed scope
    def f2():
        x=30 #LOCAL SCOPE
        print('F2=',x)
    f2()
    print('F1=',x)
f1()
print('Global=',x)
#f2() #Cannot call this as f2 is an object defined in f1
#we can access by return f2 in f1()
#Function is also object too


x=10
def f1(): #f1 and f2 are objects too
    x=20 #Enclosed scope
    def f2():
        nonlocal x #Non local will refer to the envclosed scope variable instead of creating another variable
        x=200
        print('F2=',x)
    f2()
    print('F1=',x)
f1()
print('Global=',x)

#NONLOCAL X REFERS TO THE IMMEDIATE X IF WE DONT HAVE IN IMMEDIATE THEN IT WILLL SEE NEXT IMMEDIATE X
#LIKE f1() x f2() y f3() nonlocal x here it refers f1 vala x


x=10
def f1(): #f1 and f2 are objects too

    def f2():
        global y #Since y is not there in the global scope thus it will create a y wioth a global scope
        y=200
        print('F2=',x)
    f2()
    print('F1=',x)
f1()
print('Global=',x,y)

print(dir(__builtins__)) #Return builtin classes and functions



