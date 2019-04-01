import requests
import json
import time
from downloadfile import download_file
from reboot import reboot
from zip import extractall


def update(path):
    url = 'http://solardata2.tk/api/version/get/2'
    headers = {
        'content-type': "application/json",
    }
    try:
        r = requests.get(url=url, headers=headers, timeout=5)
        data = json.loads(r.content.decode())
        # {'app_build': '1', 'app_version': '1.0'}
        print(data)
        if data['build'] == '1':
            print('no updates')
        else:
            print("downloadling ....")
            url = "https://solardata2.tk/builds/{}/{}/program.zip".format(2,data['build'])
            print(url)
            download_file(url,path+'update.zip')
            extractall(path+'update.zip',path)
            reboot()
    except:
        print("no networkconnection")
# update("")
