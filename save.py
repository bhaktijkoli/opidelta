import csv
from networkconnection import internet_on
import json
from usim800 import sim800
from rename import rename
from uvid import getuvid
import requests
import time
import delete
uid = getuvid()
GSM = False
# if GSM:
#     gsm = sim800(baudrate=9600, path="/dev/ttys1")
#     gsm.requests.APN = "www"
def createfile(file_name):

    with open(file_name, mode='w') as csv_file:

        fieldnames = [
            'uvid',
            'slave',
            'pv1_voltage',
            'pv2_voltage',
            'pv3_voltage',
            'pv1_current',
            'pv2_current',
            'pv3_current',
            'pv1_power',
            'pv2_power',
            'pv3_power',
            'rs_grid_voltage',
            'st_grid_voltage',
            'tr_grid_voltage',
            'grid_power',
            'radiator_temperature',
            'module_temperature',
            'total_energy',
            'alarm_code',
            'annual_energy',
            'daily_energy',
            'apparent_power',
            'reactive_power',
            'power_factor',
            "offline",
            'recordedAt'
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()


def sentsavedata(file_name, temp_file, url,vers):
    createfile('temp.csv')
    line = 0
    with open(file_name, 'r') as inp, open(temp_file, 'a') as out:

        writer = csv.writer(out)
        for row in csv.reader(inp):
            print(line)
            if line != 0:
                data = {
                    "uvid": row[0],
                    "slave": row[1],
                    "pv1_voltage": row[2],
                    "pv2_voltage": row[3],
                    "pv3_voltage": row[4],
                    "pv1_current": row[5],
                    "pv2_current": row[6],
                    "pv3_current":row[7],
                    "pv1_power": row[8],
                    "pv2_power": row[9],
                    "pv3_power":row[10],
                    "daily_energy":row[11],
                    "total_energy":  row[12],
                    "annual_energy": 0,
                    "other": str({
                                  "month_0": row[13],
                                  "month_1": row[14],
                                  "month_2": row[15],
                                  "month_3": row[16],
                                  "month_4": row[17],
                                  "month_5":row[18],
                                  "month_6": row[19],
                                  "month_7": row[20],
                                  "month_8": row[21],
                                  "month_9":row[22],
                                  "month_10":row[23],
                                  "month_11": row[24],
                                  "month_12": row[25],
                                  "apparent_power": row[26],
                                  "vers":row[27]}),
                    "offline": 1,
                    "recordedAt": row[28],

                }

                headers = {'Content-type': 'application/json'}

                try:
                    print(data)
                    if not GSM:
                        r = requests.post(url, data=json.dumps(data),
                                      headers=headers, timeout=1)
                    else :
                        r = gsm.requests.post(url=url,data=json.dump(data))
                    print(r)
                    print(r.content)
                    time.sleep(2)
                except requests.ConnectionError:
                    writer.writerow(row)
                    print('no net')
                except requests.exceptions.ReadTimeout:
                    writer.writerow(row)
                    print('timeout')
            line += 1
    delete.delete(file_name)
    rename(temp_file, file_name)
