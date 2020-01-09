l=[]
print(dir(l))#with any collection we can see dir wghich shows all methods
print(help(l.pop))
import sys
print(help(sys))#Description about library
#For files we create we need to give the ffirst multyiline comment of it and that will be displayed while using help same is the case with function

def add():
    '''
    Desc about add
    called doc string
    '''
    #Some Comment
    """
    Some other comment
    """
print(help(add)) #1st muntiline comment

