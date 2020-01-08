#Variable Argument
def add(a,b=10,*c): #*c captures extra arguments in form of tuple
    print('Extra arguments passed=',c)
    r=a+b+sum(c)
    return r
res1=add(10)
print('result1=',res1)
print('-'*40)
res2=add(10,20,30,40,50)
print('res2=',res2)

def telnet(host=None,port=None,*cmds): #*CMDS Packing
    import subprocess
    result=[]
    for each_cmd in cmds:
        r=subprocess.check_output(each_cmd,shell=True)#SUBPROCESS TO EXECUTE SYSTEM COMMAND. CHECK OUTPUT IS WRITTEN IN FILE SUBPROCESS SO WE NEED TO IMPORT IT
        result.append(r)
    return result

r=telnet(0,0,'dir','type log_report.csv')
print('R=',r)
f=open('cmd_out.txt','w')
r=[line.decode() for line in r] #Bytes to string
f.writelines(r)
f.close()


#iF COMMANDS ARE IN FILE THEN WE CAN TAKE IT FROM FILE IN A LIST AS
c=['dir','type log_report.csv']
r2=telnet(0,0,*c) #UNPACKING






