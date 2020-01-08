import sqlite3 #SQLLITE IS THE LIBRARY FOR SQL
con=sqlite3.connect('mydb.sqlite3') #If file is notfound it will create one

#For other db
#MYSQL
#import pymsql
#con=pymsql.connect(user='', password='',port='',database='')

#For other db
#ORACLE
#import cxoracle
#con=pymsql.connect(user='', password='',port='',database='')


cur=con.cursor() #Cursor is to commmunicate with db
query='''CREATE TABLE IF NOT EXISTS LOGDATA(
IP VARCHAR(100),
DATE VARCHAR(100),
PICS VARCHAR(100),
URL VARCHAR(100))'''
cur.execute(query)

#Download db browser for sqlite to see the table

import urllib.request as u #URLLIB IS LIBRARY WHICH IS USED TO READ DATA FROM A WEBSITE
myurl='https://www.jafsoft.com/searchengines/log_sample.html'
f=u.urlopen(myurl)
import re
for line in f:
    #print(type(line))
    line=line.decode()
    #print(line)
    m=re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*',line)
    if m!=None:
        ip=m.group(1)
        print(ip)


#[.] . only
# . any character
#\d any digit
#\D non digit
# * represent 0 or more
# + represent 1 or more
# ? represent 0 or 1
# r[ea]d matches red and rad [] means either of both