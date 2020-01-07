f1=open('log_report.txt','w')
f2=open('log_report.csv','w')
f1.write('IP\tDATE\tPICS\tURL')
f2.writelines(['IP,','DATE,','PICS,','URL\n'])
f3=open(r'C:\Python Training\log\Server Log.txt')
for line in f3:
    if line[:3].isdigit():
        #print(line)
        sp=line.split()
        #print(sp)
        ip=sp[0]
        date = sp[3]
        dt = date[1:12]

        if 'pics' in sp[6]:
           im=sp[6]
           im1=im[6:]

           #im2=im.lstrip('/pics/') 2nd way
           #print(im2)
        else:
            im1='No Image'
        url = sp[10][1:-1]
        print(ip,dt,im1,url,sep='\t',file=f1)
        print(ip, dt, im1, url, sep=',', file=f2)
f1.close()
f2.close()

