s='abc123xyz456ABC'
r1=s.split('123')
print('r1=',r1)

import re
r2=re.split('\d{3}',s)#SPLIT AT EVERY NO
print('r2=',r2)

r3=s.find('123')
if r3!=-1:
    print('Substring found')

r4=re.search('\d{2}',s)#Search two digit are there or got
if r4!=None:
    print('Digit found')

#Get all ips by shortcut
f=open(r'C:\Python Training\log\Server Log.txt' )
data=f.read()
ips=re.findall('\d{3}.\d{3}.\d{3}.\d{3}',data)
print('ips=',ips)


