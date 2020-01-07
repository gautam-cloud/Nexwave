#Writing to file
f1=open('out1.txt','w') #In w mode if file is not available it will make one and if existing file is there with data it will erase that
x=10
s='python\n'
x=str(x)+'\n' #The function with which we want to write data takes only string value
f1.write(x)
f1.write(s) #data get copied from buffer to file  when we close connection by without even closing we can see the output in file as interpretor does close the connection itself
f1.flush() #transfer data from buffer to file without closing the connection


#2nd way
l=[x,s]
f1.writelines(l)
f1.close()

#Reading from file
f2=open('out1.txt','r') #If the file is not avail;able it wont read, it will show error
r1=f2.read()  #'10\npy\n10\npy'
print('r1=',r1)  #In print all \n get converted

f2.seek(0)
r2=f2.read()
print('r2=',r2) #we have a seek pointer in reading and writing. In write the seek is at start as empty file but once it is read seeik pointer comes to end and second time we get no read
#thus we use seek(0)


f2.seek(0)
r3=f2.readline()
print('r3=',r3)

#2nd way
while True:
    line=f2.readline()
    if line=='': #EOF
        break
    else:
        print('line=',line)

#3rd way
f2.seek(0)
r4=f2.readlines() #In case of read and readlines it will read the whole file but in read it returns as string but in readlines it shows as readlines
print('r4=',r4)



r5=[]
for l in r4:
    l=l.strip()
    r5.append(l)
print('r5=',r5)


f2.seek(0)
for x in f2:
    print('line=',x)


f2.seek(0)
r6=list(f2)

f2.seek(0)
r7=tuple(f2)

l1=['h1','h2']
l2=['ip1','ip2']
d1=dict(zip(l1,l2))
print('D1=',d1)


e=enumerate(l1,start=1)
print(list(e)) #Make  a collection of tuple with an index no , value

f2.seek(0)
d2=dict(enumerate(f2))
print('d2=',d2)
f2.close


f3=open('out1.txt','a')#a means append
f4=open('out2.csv','a')#if file is available it will make use of the file but if it is not availbale then it will make a new one
print(20,'java',sep='\n',file=f3,flush=True)
print(20,'java',sep=',',file=f4)
f3.close()
f4.close()


#write,writelines,print
# w means write only
#r means read only
#a means append only
# w+ means WR
#r+ means RW
#a+ means AR
# last 3 provide Read write but diff in filer creation and all

#Binary file
# wb means write only
#rb means read only
#ab means append only
# w+b means WR
#r+b means RW
#a+b means AR
