d={'ROM':'d1 info','HDD':'d2 info', 'FDD':'d3 info', 'RAM':'d4 info', 'CPU':'d5 info'}
k=input("Enter thE device for which you wish to search")
result=[]
for i in d.keys():
        if i.startswith(k):
            result.append(i)
    print(set(result))
if len(result) == 0:
        print("Device Not Found")
else:
    info = d.get(k)
    if info is not None:
        print(info)
    else:
        print("Device Not Found")

