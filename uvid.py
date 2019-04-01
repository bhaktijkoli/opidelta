import os,inspect
import json
path =  os.getcwd() +  '/conf.json'
#path = 'conf.json'

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  + '/conf.json'
print(path)
def getuvid():
    with open(path, mode='rb') as conf:
        data = conf.read()
        data = json.loads(data.decode())
        return(data['udi'])
