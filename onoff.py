import requests
import json
import time
from uvid import getuvid

uvid = getuvid()

def on_datalogger():
    slave_ids = [1]
    instrument = mb.Instrument('/dev/ttyS1', 1)
    # instrument.serial.port          # this is the serial port name
    instrument.serial.baudrate = 9600  # Baud
    instrument.serial.bytesize = 8

    instrument.serial.stopbits = 1
    instrument.serial.timeout = 2  # seconds
    instrument.address = 0   # this is the slave address number
    instrument.mode = mb.MODE_RTU   # rtu or ascii mode
    # instrument.debug = True
    # print(i, end=" ")
    try:
        print("in try")
        value = instrument.write_register(registeraddress=4002, value=1,
                                          numberOfDecimals=0, functioncode=6, signed=False)
        print(value)
        time.sleep(0.2)
    except IOError:
        print("Failed to read from instrument")
        print("off")

def off_datalogger():
        print("in off")
        slave_ids = [1]
        instrument = mb.Instrument('/dev/ttyS1', 1)
        # instrument.serial.port          # this is the serial port name
        instrument.serial.baudrate = 9600  # Baud
        instrument.serial.bytesize = 8
        instrument.serial.stopbits = 1
        instrument.serial.timeout = 2  # seconds
        instrument.address = 0   # this is the slave address number
        instrument.mode = mb.MODE_RTU   # rtu or ascii mode
        # instrument.debug = True
        # print(i, end=" ")
        try:
            print("in try")
            value = instrument.write_register(registeraddress=4001, value=1,
                                              numberOfDecimals=0, functioncode=6, signed=False)

            print(value)
            time.sleep(0.2)

        except IOError:
            print("off")

def onoff():
    url = 'http://solardata2.tk/api/inverter/status?uvid={}&slave=1'.format(uvid)
    headers = {
        'content-type': "application/json",
    }
    try:
        r = requests.get(url=url, headers=headers, timeout=1)
        print(r)
        data = json.loads(r.content.decode())
        print(data)
        #{'status': 1}
        if data["status"] == 1:
            print("on")
            on_datalogger()
            print(data)
        elif data["status"] == 0:
            off_datalogger()
            print("off")
        elif data["status"] == 2:
            print("do nothing")
    except :
        pass

