from reboot import reboot as r
from DS3231 import DS3231
import json
import os,inspect   
def is_reboot(path):  
       with open(path, mode='rb') as reboot:
            data = reboot.read()
            data = json.loads(data.decode())
            return(data['reboot'])
def set_reboot(path,value):
       with open(path, "wb") as reboot:
            data = json.dumps({"reboot":value})
            print(data)
            reboot.write(data.encode())
       
def reboot():
        dt = DS3231(0)
#    dt.setNow()
        hr = str(dt.readTime().strftime("%H"))
        mi = str(dt.readTime().strftime("%M"))
        print(hr)
        path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  +  '/system.json'
        isreboot = is_reboot(path)
        if hr == "5":
            if isreboot:
                print("reboot")
                set_reboot(path,0)
                r()        
        if hr != "5":
            if isreboot != 1:
                set_reboot(path,1)
                print("set 1")
        isreboot = is_reboot(path)
        print(isreboot)
        
print(reboot())

