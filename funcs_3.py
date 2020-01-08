#Positional Argument
def add(a,b):
    return a+b
r=add(10,20)
print('Sum=',r)

def get_ips(filepath,mode):
    f=open(filepath)
    if filepath.endswith('.csv'):
        ips=[line.split(',')[0] for line in f]
        return ips
    else:
        ips=[line.split()[0] for line in f]
        return ips
r=get_ips('log_report.txt','r')
print('r=',r)