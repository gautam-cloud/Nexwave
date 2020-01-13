import addmodule #once this is imported it will execute every line
#Its giving an error
#WE HAVE TWO WAYS TO DO THAT 1)ENV VARIABLE IE TO SET PYTHON PATH SO THAT IT CAN READ IT FROM LIB 2)Programaticaaly
#This import will Search for file execute it and set an object
print(addmodule.msg)
print(addmodule.add(10,20))
line='-'*40
print(line)

#2nd way using sys
#import sys
#print(sys.path)
#sys.path.append(r'C:\Python Training\lib') #import addmodule

#2nd way to import module
import addmodule as a
print(a.msg)
print(a.add(10,20))
print(line)

#we can import many modules in a single line as import module1,module2,module3
#3rd way to import module
from addmodule import msg,add
print(msg)
print(add(10,20))
print(line)

# 4th way Aliasing
from addmodule import msg as a, add as b
print(a)
print(b(10,20))
print(line)

#5th way
from addmodule import *
print(msg)
print(add(10,20))

#Access module when in directory
import project.net.addmodule
print(project.net.addmodule.msg)
print(project.net.addmodule.add(10,2))
print(line)

import project.net.addmodule as a
print(a.msg)
print(line)


from project.net.addmodule import msg,add
print(msg)
print(line)


#INIT FILE
#IF INIT IS FINDING WHEATHER IF ANY MODULE IS ALRAEDY OPEN OR PORT IS OPEN  AS INIT WILL GET EXECUTED FOR EVERY DIRECTORY IT IS IN STARTING FROM PROJECT,NET,MODULE
#THUS WE MADE A __INIT__.PY FILE IN NET

#IF WE WANT TO USE 3RD PARTY LIBRARY MANUALLY WE CAN SEARCH FOR IT, DOWNLOAD IT ANSD INSTALL IT OR ELSE USE PIP FOLDER OR THROUGH PYCHARM
# 1st way
# Download from python.org and give the path and in terminal of pycharm type
# pip install C:\Users\lab365\Downloads\bottle-0.12.18-py3-none-any.whl

#2nd way
#Write directly in terminal
#pip install flask

#3rd way
#Go to file then seetings search for selinium and install pacakage



