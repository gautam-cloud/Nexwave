l1=[i for i in range(10)]
l2=[i*i for i in l1 if i%2==0]
f=open('out1.txt')
l3=[line.strip() for line in f]
print(l3)

f2=open('C:\Python Training\log\Server Log.txt')
ip=[line.split()[0] for line in f2 if line[:3].isdigit()]
print(ip)

f2.seek(0)
ip2=(line.split()[0] for line in f2 if line[:3].isdigit())
print(tuple(ip2))

f2.seek(0)
images=[line.split()[6].lstrip('/pics') if 'pics' in line.split()[6] else 'No image' for line in f2 if line[:3].isdigit()]
print(images ) #FLOW STARTS WITH FOR THEN RIGHT SIDE IF THEN LEFT SIDE IF, IF TRUE EXECUTE IF NOT THEN ELSE

hosts=['h1','h2']
ips=['ip1','ip2']
d={k:v for k,v in zip(hosts,ips)}
print(d)