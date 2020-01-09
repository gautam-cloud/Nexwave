#Program to connect to other system
#Details of server we want to connect to
#test.rebex.com
#port 22
# username =demo
# password= password
import paramiko as p
client = p.SSHClient()
client.set_missing_host_key_policy(p.AutoAddPolicy) #Here a pop is made to server but if it allows then only connection happens so we write this line
client.connect('test.rebex.net', username='demo', password='password', port=22)
stdin,out,err=client.exec_command('ls')
cmd_out=out.read()
print('cmd_out=',cmd_out)
#We transfered the text file from the server and copied it here 
ftp=client.open_sftp()
ftp_out=ftp.get('readme.txt','ftp_readme.txt')
print('ftp_out=',ftp_out)
ftp.put('out1.txt','out1.txt') #Acess Denied as they dont allow us to do so



