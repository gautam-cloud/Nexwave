import pandas as pd
df=pd.read_csv('dbdump.csv')
print(df['IP'])
df2=df['ID'].describe()
print(df2)
line='-'*40
print(line)

df3=df['IP'].describe()
print(df3)
print(line)

df4=df.describe() # WE are calling on all file but but default it takes on no column. if we have multiple column no then it will give summary of all number columns
print(df4)
print(line)

df5=df['ID'].mean()
print('df5=',df5)
print(line)

df6=df.head(5) # 5 rows from top
df7=df.tail(5) # 5 rows from bottom
print(df6)
print(df7)
print(line)

#To print count of a column
df8=df['PICS'].value_counts()
print(df8)
print(line)

#GRAPH REPRESENTATION
import matplotlib.pyplot as plt
df8.plot()
plt.show()

#Bar Graph and Save
df8.plot.bar()
plt.savefig('mygraph.png',bbox_inches='tight')

writer=pd.ExcelWriter('Report.xlsx',engine='xlsxwriter') #Install xlsxwriter #ExcelWriter is a class
df8.to_excel(writer,sheet_name='DATA') #Pandas has many writer so we need to write in which writer we want to use in engine
wb=writer.book #If we need more sheet so we need the workbook reference here
ws=wb.add_worksheet('GRAPH') #this is to add a new sheet
ws.insert_image('B2','mygraph.png')#Insert the image
writer.close()

df9=df[df['ID']>10]
print('df9=',df9)
df10=df[df['PICS'].str.endswith('jpg')]
print('df10=',df10)
df11=df.groupby(['PICS']).count()
print('df11=',df11)
line='-'*40
#SLICING
df12=df.iloc[1,1] #Value at Row 1 Column 1
print('df12=',df12)
print(line)
df13=df.iloc[1] #Value at Row 1
print('df13=',df13)
print(line)
df14=df.iloc[:,1] #1st column
print('df14=',df14)
print(line)
df15=df.iloc[1:10:2]#1 to 9th row step by 2
print('df15=',df15)
print(line)
df16=df.iloc[:,0:5:2]# 0 to 5th column step by 2
print('df16=',df16)
print(line)
df17=df.iloc[5:10,1:4]#in between data
print('df17=',df17)
print(line)
df18=df.iloc[[1,4]]#row 1,4,7
print('df18=',df18)
print(line)
df19=df.iloc[[1,4],[1,3]]#row 1,4,7 column 1,3
print('df19=',df19)
print(line)





