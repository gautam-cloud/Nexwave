#Positional Argument
#WITH DEFAULT VALUES
def add(a,b=10):
    return a+b
r=add(10) #If we miss passing the argument then it will take the default else it will take the passed one
print('Sum=',r)

def get_ips(filepath,mode='r'):
    f=open(filepath)
    if filepath.endswith('.csv'):
        ips=[line.split(',')[0] for line in f]
        return ips
    else:
        ips=[line.split()[0] for line in f]
        return ips
r=get_ips('log_report.txt','r')
print('r=',r)