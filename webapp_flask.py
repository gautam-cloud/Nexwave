#bottle- html file extention=.tpl ; directory path-TEMPLATE_PATH ; execution taken care by-Simple Template Engine(STE) ; to write python statement- begin with '%' followed by statement ; to implement indentation- start with %for and end with '% end'. to print -> {{ var }}
#flask-  html file extention=.html ; directory-templates folder needs to be created ; Jinja2 template Engine ; to write python statement- begin with '{%' followed by statement and enclosed by '%} ; to implement indentation {%for ...%} ; same as above
#django- html file extentiion=.html ; directory-template folder needs to be created :Django Template Engine ;  same as above ; same as above ;  same as above

import flask
#How to create website
app=flask.Flask('MyApp')#name of app is to be given as arg
#app.run()
@app.errorhandler(404)#predefined decorator #error becomes errorhandler
def errorpage(err):
    return 'Mind your own business'
@app.route('/')
def indexpage():
    return 'Welcome'
@app.route('/about')
def aboutpage():
    return '<b>This is about</b>'
@app.route('/login')
def loginpage():
    return '''<html>
    <form action='/verify' method='post'>
    USER NAME :<input type='text' name='uname'/><br/>
    PASSWORD  :<input type= 'password' name='pw' /><br/>
               <input type= 'Submit' value='LOGIN'/><br/>
    </form>
    </html>'''
#http methods
    #get- to display data (eg. Gmail/about / contact)
    #post- to take confidential data(eg. user name, password, create account)
    #put- to update data(eg. to add data)
    #delete- to delete data(eg. to delete data/account)

@app.route('/verify',methods=['POST'])#method to methods ahnd post in list
def verifypage():
    u=flask.request.form.get('uname') #bottle.request.forms will create a dictionary

    #for eg. if forms={'uname':'xyz'}, so if we call by the command-> forms['uname'] and no data is found so it will throw an error
    #but if we use command--> forms.get('uname') and no data is found it will return None.

    p=flask.request.form.get('pw')
    if not(u=='abc' and p=='xyz'):
        return 'Login Failed'
    else:
        #return 'Login Success'
        import _sqlite3
        con=_sqlite3.connect('mydb.sqlite3')
        cur=con.cursor()
        cur.execute('Select * from LOGDATA')
        result=cur.fetchall()
        return flask.render_template('report.html', res=result)#res is any name, res will be accessible in tpl

@app.route('/download/<filename>')# we are giving var as filename becoz for different file we need that filename to come as multiple files are there
def downloadfile(filename):
    return flask.send_from_directory(directory=r'C:\Python Training\bin', filename=filename)#Like if we have a download link in the webpage and once we click on it the file will get downloaded
#This filename can accept anything like string , no etc
#If we wish to restrict it to numbers then

@app.route('/empid/<int:eid>')
def empid(eid):
    d={'name':'abc', 'EMPID':eid}
    return d #It will take int float as eid only

@app.route('/logdata')
def logdata():
    return flask.redirect('/login')

@app.route('/passwords')
def passwords():
    return flask.abort(201,'Access Denied')





app.run(host='192.168.3.224',port=8080)