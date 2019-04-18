import requests
import json
domain = "https://api.solardata2.tk"
url = domain + "/api/inverter/stats/add"

data = {
        "uvid": "3350338465239810",
        "slave": 1,
        "pv1_voltage": 0,
        "pv2_voltage": 0,
        "pv3_voltage": 0,
        "pv1_current": 0,
        "pv2_current": 0,
        "pv3_current": 0,
        "pv1_power": 0,
        "pv2_power": 0,
        "pv3_power":  0,
        "annual_energy": 0,
        "total_energy": 0,
        "daily_energy": 0,
        "other": str({
            "month_0": 0,
            "month_1": 0,
            "month_2": 0,
            "month_3": 0,
            "month_4": 0,
            "month_5": 0,
            "month_6": 0,
            "month_7": 0,
            "month_8": 0,
            "month_9": 0,
            "month_10": 0,
            "month_11": 0,
            "month_12": 0,
            "apparent_power":  0,
            "vers": 1}),

        "offline": 0,
        "recordedAt": "2019-04-18 23:08:55"
    }
print(data)
headers = {'Content-type': 'application/json'}
r=  requests.post(
url, data=json.dumps(data),headers=headers
)

print(r.content)