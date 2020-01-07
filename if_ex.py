a=0
if a==10:
    print('a equal 10')
if a>10:
    print('a greater than 10')
if a<10:
    print('a less than 10')

a=10
if a==10:
    print('a equal 10')
elif a>10:
    print('a greater than 10')
elif a<10:
    print('a less than 10')

a=0
if a==10:
    print('a equal 10')
elif a>10:
    print('a greater than 10')
else:
    print('a less than 10')

s='python'
if 'th' in s:
    print('Substring found')
if not s.startswith('java'):
    print('Not Java')
if s!='c++':
    print('not c++')
if s[1:3]=='yt':
    print('yt found')

l1=[10,20]
l2=l1
l3=l1.copy()
if 20 in l1:
    print('20 found')

if l1 is l2: #Checks id only
    print ('both refers same obj')

if id(l1)==id(l2):
    print('Both refers same obj')

if l1==l3: #Checks content
    print('Content are same')

d={'A':10, 'B':20}
if 'B' in d: #Default it search in key only
    print('Key B found')
if 'B' in d.keys():
    print('key b found')
if 20 in d.values():
    print('20 found')
if ('A',10) in d.items():
    print('item found')

if a==10: #If we want Empty block use pass it does not do anything
    pass