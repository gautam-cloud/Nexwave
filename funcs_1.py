def add():
    a=10
    b=20
    c=a+b
    print('c=',c)
add()
add()

def get_ips():
    f=open('C:\Python Training\log\Server Log.txt')
    ips=[line.split()[0] for line in f if line[:3].isdigit()]
    print('ips=',ips)
get_ips()
#print('ips=',ips) #Function block variables cannot be accesed outside function block whereas in for while we were able to acccess

