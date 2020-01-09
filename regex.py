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
    m=re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[a-zA-Z]{3}/\d{4}).*(?:GET|POST)\s+/(?:pics/(\w+\.\w+))?.*(http://\S+)</A>.*',line) #.*? we have put as .* is greedy operator takes min of the next
    # We dont need to capture GET POST in a group so we write?: before it
    # [.] . only
    # . any character
    # \d any digit
    # \D non digit
    # * represent 0 or more
    # + represent 1 or more
    # ? represent 0 or 1
    # r[ea]d matches red and rad [] means either of both
    # \s space
    # \w word character [a-zA-Z0-9_]
    # \W non word [^a-zA-Z0-9_] (not of)
    # \S non space
    if m!=None:
        ip=m.group(1)
        #print(ip)
        dt=m.group(2)
        pics=m.group(3)
        if pics==None:
            pics='No image'
        url=m.group(4)
        #print(ip,dt,pics,url)
        query=f"INSERT INTO LOGDATA VALUES('{ip}','{dt}','{pics}','{url}')" # f here is formatted string ie {name} is replaced with value
        print(query)
        cur.execute(query)
    con.commit()
cur.execute('SELECT * FROM LOGDATA')
result=cur.fetchall() #We can also use fetch1() to get ek ke karka result but we have to use loop for all then
print(result)

#NOW WE WANT TO WRITE THE RESULT TO CSV FILE
#THERE ARE 2 WAYS OF IT ONE WITH PRINT AND OTHER WITH STANDARY LIBRARY CALLED CSV which has two methods Reader Writer
#WRITING RESULT TO CSV FILE
import csv
f=open('dbdump.csv','w',newline='') #writerow method itself puts a newline so we made it not to get a extra line break
wt=csv.writer(f)
wt.writerow(['IP','DATE','PICS','URL'])
for eachrow in result:
    wt.writerow(eachrow)
f.close()
#READING FROM CSV FILE
f=open('dbdump.csv')
rdr=csv.reader(f)
csv_out=list(rdr)
print('csv_out=',csv_out)

#THERE ARE LESS OPTION WITH CSV LIBRARY LIKE READ AND WRITE
#WE HAVE N NO OF METHODS IN DATAFRAMES Class IF WE MAKE A DATFRAME OBJ WE CAN MAKE USE OF ALL METHODS
#pandas is 3rd party library so install it

import pandas as pd #We use dataframe here instead of list as list has min functions and in 2d data we have to do many operations and dataframe as it has more features prints in a indexed ways
df1=pd.DataFrame([[10,20,30],[40,50,60]],index=['r1','r2'],columns=['c1','c2','c3']) #df1 is the dataframe object
l1=list([[10,20,30],[40,50,60]])
print(df1)
print(l1)

#data frame method to_csv (does without for )
df2=pd.DataFrame(result)
print(df2)
df2.to_csv('out3.csv',index=None, header=['IP','DATE','PICS','URL'])

#Directly writing in csv with cursor
cur.execute('Select * from LOGDATA')
df3=pd.DataFrame(cur)
df3.to_csv('out4.csv')

#DATA FRAME USAGE WITH EXCEL AND JSON FILE
df3.to_excel('out5.xlsx') #Install openpyxl
df4=df3.T #We did a transpose of it as in JSON VIEWER WE WANT IT IN KEY VALUE PAIR PERFECTLY
df4.to_json('out6.json') #See this file with ONLINE JSON VIEWER ON GOOGLE BY COPING THE CONTENT OF FILE out6.json










