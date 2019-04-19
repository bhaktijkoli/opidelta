import restart
import datetime
import requests
import csv
import json
from usim800 import sim800
import os
import inspect
import time
from update import *
from data import writecsv, setData, setCsvData
from save import sentsavedata, createfile
from var import registers
from uvid import getuvid
from findslave import find_slave_id
import minimalmodbus as mb
from networkconnection import internet_on

from pyA20.gpio import gpio
from pyA20.gpio import port
from DS3231 import DS3231
from onoff import *
dt = DS3231(0)
dt.readTime()
led = port.PA14
led1 = port.PA19
led2 = port.PA18

gpio.init()
gpio.setcfg(led, gpio.OUTPUT)
gpio.setcfg(led1, gpio.OUTPUT)
gpio.setcfg(led2, gpio.OUTPUT)
vers = 1
GSM = False

if GSM:
    gsm = sim800(baudrate=9600, path="/dev/ttys1")
    gsm.requests.APN = "www"
#slave_ids = find_slave_id()
slave_ids = [1,2]
uid = str(getuvid())
print(uid)
path = '/root/orangepizerodelta/'
path = ''
file_name = path + uid + '.csv'
temp_file = path + 'temp.csv'

file_name = path + uid + '.csv'
temp_file = path + 'temp.csv'
print(file_name)


if not os.path.exists(path + uid+".csv"):
    createfile(path + uid+".csv")
    print("file created")


def initmodbusandread(i):
    try:
        if (registers.get(i)[4]["send"]) is True:
            print(i)
            instrument = mb.Instrument('/dev/ttyS1', slave_id)
            instrument.serial.baudrate = 9600  # Baud
            instrument.serial.bytesize = 8
            instrument.serial.stopbits = 1
            instrument.serial.timeout = 2  # seconds
            instrument.address = slave_id   # this is the slave address number
            instrument.mode = mb.MODE_RTU   # rtu or ascii mode
            read(i, instrument)
    except IOError:
        registers.get(i)[5]["value"] = '0'
        print("Failed to read from instrument")


def read(i, instrument):
    try:
        value = instrument.read_register(
            i,
            registers.get(i)[2]["decimal"], 4)
        gpio.output(led, 1)
        time.sleep(0.1)
        print(i)
        print(value)
        gpio.output(led, 0)
        time.sleep(0.1)

        registers.get(i)[5]["value"] = value
        print(i)
        print(value)
        time.sleep(0.2)
    except:
        registers.get(i)[5]["value"] = '0'
        print("can't read {} rig".format(i))


def senddata(file_name, url, sdata, headers, data, vers):
    try:
        if internet_on():
            sentsavedata(file_name, temp_file="temp.csv", url=url, vers=vers)
            gpio.output(led1, 1)
            time.sleep(0.1)

        print("near r")
        print(data)
        if not GSM:
            r = requests.post(url, data=json.dumps(data), headers=headers,
                              timeout=2)
        else:
            r = gsm.requests.post(url=url, data=json.dump(data))
        print(r)
        print(r.content)

    except:
        print('no net')
        writecsv(file_name, sdata)
        gpio.output(led1, 0)
        time.sleep(0.1)


domain = "https://api.solardata2.tk"
url = domain + "/api/inverter/stats/add"
print(url)
while True:

    try:
        base_path = os.path.dirname(os.path.abspath(
            inspect.getfile(inspect.currentframe()))) + "/"
        print(base_path)
        restart.reboot()
        update(base_path)
        print(slave_ids)
        for slave_id in slave_ids:
            for i in registers.keys():
                initmodbusandread(i)
            timesend = str(dt.readTime().strftime("%Y-%m-%d %H:%M:%S"))
            # timesend = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(timesend)
  
            # onoff()
            print(uid + "{0:0=2d}".format(slave_id))
            data = setData(uid, slave_id, registers, timesend, vers)
            sdata = setCsvData(uid, slave_id, registers, timesend, vers)
            headers = {'Content-type': 'application/json'}
            senddata(file_name, url, sdata, headers, data, vers)
        time.sleep(10*20)
    except Exception as e:
        print(e)
        restart.reboot()
        time.sleep(10)
