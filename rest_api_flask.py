#API-1 -->ip
# API1=HTTP://127.0.0.1:8080/ip #Like bookmyshow ask pvr website for list of movies only
#api return in jsop format as we ned the direct data only

import flask
app=flask.Flask('MyApp')
@app.route('/ip',methods=['GET'])
def api_ip():
    import _sqlite3
    con = _sqlite3.connect('mydb.sqlite3')
    cur = con.cursor()
    cur.execute('Select IP from LOGDATA')
    result = cur.fetchall()
    result=[i[0] for i in result]
    d={k:v for k,v in enumerate(result)}
    return d


# API2=HTTP://127.0.0.1:8080/emp
@app.route('/emp', methods=['POST'])#through browser
def empdetails():
    details=flask.request.args
    details=dict(details)
    return details

@app.route('/json')#create a json file, how to read a json file and how to send data through json
def fromjson():
    f=open('mydata.json','w')
    d={'course':'python','loc':'blr'}
    import json
    json.dump(d,f)
    f.close()
    f=open('mydata.json')
    r=json.load(f)
    f.close()
    return r

app.run()