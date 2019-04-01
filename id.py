import random
import requests
import json

uid = ''


def getrandint():
    return(random.randint(0, 9))


while True:
    fisrt = str(getrandint())
    if fisrt == '0':
        print(fisrt)
        continue
    else:
        uid += fisrt
        print(fisrt)
        break


for i in range(0, 15):
    uid += str(getrandint())
print(uid)



API_ENDPOINT = 'https://solardata2.tk/api/datalogger/check'
print(len(uid))
headers = {
    'content-type': "application/json",
}
data= {"uvid": uid}

print(json.dumps(data))
r = requests.post(url=API_ENDPOINT,data= json.dumps(data), headers=headers)
print(r)
data = r.content.decode('utf-8')
print(data)

if data == '0':
    print(data)
    uid = {"uvid": uid}
    print(uid)
    r = requests.post(url=API_ENDPOINT, data=json.dumps(uid), headers=headers)
    print(r.content)

# extracting response text

