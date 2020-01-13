#We dont call apis in broswer 5tyhis is the way book my show will call the api to reterrive data from pvr
#Calling apis 1,2,3 created in file rest_api_bottle
api1='http://127.0.0.1:5000/ip'#5050 for flask 8080 for bottle
api2='http://127.0.0.1:5000/emp'
import requests
api1_res=requests.get(api1)
api1_res=api1_res.json()
print('api1_res=',api1_res)

api2_res=requests.post(api2,params={'user':'abc', 'passwd':'xyz'})
api2_res=api2_res.json()
print('api2_res=',api2_res)

api3='http://127.0.0.1:5000/json'
api3_res=requests.get(api3)
api3_res=api3_res.json()
print('api3_res=',api3_res)
