F=open('SSH_log_Sample.txt')

count=0
for line in F:
    if 'Failed password' in line:
        count=count+1

    if 'sshd version' in line:
        s = line.split()
        position= s.index('version')
        ver=s[position+1]

    if 'private host key' in line:
        l=line.split()
        # print(l)
        #en=l[2].split()
        en=l.index('key')
        en1=l[en+3]
        en2=en1[:en1.index(':')]

    if 'Accepted password' in line:
        u=line.split()
        # print(u)
        us=u.index('for')
        use=u[us+1]

        ip=u[us+3]

        port=u[us+5]


print('No. of failed login attempts:', count)
print('SSHD version:', ver)
print('Encryption:', en2)
print('Successful login user:', use)
print('ip:', ip)
print('port:',port)