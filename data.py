import csv


def int_to_hex(num):
    return(hex(int(num)))


def return_int_value(a, b):
    a = hex(int(a))
    b = hex(int(b))
    hex_a = a + b[2:]
    return (int(hex_a, 0))


def setData(uid, slave_id, registers, timesend,vers):

    b = registers.get(1073)[5]["value"]
    a = registers.get(1074)[5]["value"]
    runtime_energy = return_int_value(a, b)

    b = registers.get(2111)[5]["value"]
    a = registers.get(2112)[5]["value"]
    month_0 = return_int_value(a, b)

    b = registers.get(2113)[5]["value"]
    a = registers.get(2114)[5]["value"]
    month_1 = return_int_value(a, b)

    b = registers.get(2115)[5]["value"]
    a = registers.get(2116)[5]["value"]
    month_2 = return_int_value(a, b)

    b = registers.get(2117)[5]["value"]
    a = registers.get(2118)[5]["value"]
    month_3 = return_int_value(a, b)

    b = registers.get(2119)[5]["value"]
    a = registers.get(2120)[5]["value"]
    month_4 = return_int_value(a, b)

    b = registers.get(2121)[5]["value"]
    a = registers.get(2122)[5]["value"]
    month_5 = return_int_value(a, b)

    b = registers.get(2123)[5]["value"]
    a = registers.get(2124)[5]["value"]
    month_6 = return_int_value(a, b)

    b = registers.get(2125)[5]["value"]
    a = registers.get(2126)[5]["value"]
    month_7 = return_int_value(a, b)

    b = registers.get(2127)[5]["value"]
    a = registers.get(2128)[5]["value"]
    month_8 = return_int_value(a, b)

    b = registers.get(2129)[5]["value"]
    a = registers.get(2130)[5]["value"]

    month_9 = return_int_value(a, b)

    b = registers.get(2131)[5]["value"]
    a = registers.get(2132)[5]["value"]
    month_10 = return_int_value(a, b)

    b = registers.get(2133)[5]["value"]
    a = registers.get(2134)[5]["value"]
    month_11 = return_int_value(a, b)

    b = registers.get(2135)[5]["value"]
    a = registers.get(2136)[5]["value"]
    month_12 = return_int_value(a, b)

    data = {
        "uvid": uid,
        "slave": slave_id,
        "pv1_voltage": registers.get(45056)[5]["value"],
        "pv2_voltage": registers.get(45059)[5]["value"],
        "pv3_voltage": registers.get(45062)[5]["value"],
        "pv1_current": registers.get(45057)[5]["value"],
        "pv2_current": registers.get(45060)[5]["value"],
        "pv3_current": registers.get(45063)[5]["value"],
        "pv1_power": registers.get(45058)[5]["value"],
        "pv2_power": registers.get(45061)[5]["value"],
        "pv3_power": registers.get(45064)[5]["value"],
        "daily_energy": registers.get(1071)[5]["value"],
        "other": str({"runtime_energy":  runtime_energy,
                      "month_0": month_0,
                      "month_1": month_1,
                      "month_2": month_2,
                      "month_3": month_3,
                      "month_4": month_4,
                      "month_5": month_5,
                      "month_6": month_6,
                      "month_7": month_7,
                      "month_8": month_8,
                      "month_9": month_9,
                      "month_10": month_10,
                      "month_11": month_11,
                      "month_12": month_12,
                      "apparent_power":  registers.get(49200)[5]["value"],
                      
                      "vers":vers}),
        "offline": 0,
        "recordedAt": timesend
    }
    return data


def writecsv(file_name, data):
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
        "daily_energy",
        "runtime_energy",
        "month_0",
        "month_1",
        "month_2",
        "month_3",
        "month_4",
        "month_5",
        "month_6",
        "month_7",
        "month_8",
        "month_9",
        "month_10",
        "month_11",
        "month_12",
        "apparent_power",
        "vers",
        'recordedAt',
        
    ]
    print(data)

    with open(file_name, 'a') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, fieldnames)
        w.writerow(data)


def setCsvData(uid, slave_id, registers, timesend,vers):
    b = registers.get(1073)[5]["value"]
    a = registers.get(1074)[5]["value"]
    runtime_energy = return_int_value(a, b)

    b = registers.get(2111)[5]["value"]
    a = registers.get(2112)[5]["value"]
    month_0 = return_int_value(a, b)

    b = registers.get(2113)[5]["value"]
    a = registers.get(2114)[5]["value"]
    month_1 = return_int_value(a, b)

    b = registers.get(2115)[5]["value"]
    a = registers.get(2116)[5]["value"]
    month_2 = return_int_value(a, b)

    b = registers.get(2117)[5]["value"]
    a = registers.get(2118)[5]["value"]
    month_3 = return_int_value(a, b)

    b = registers.get(2119)[5]["value"]
    a = registers.get(2120)[5]["value"]
    month_4 = return_int_value(a, b)

    b = registers.get(2121)[5]["value"]
    a = registers.get(2122)[5]["value"]
    month_5 = return_int_value(a, b)

    b = registers.get(2123)[5]["value"]
    a = registers.get(2124)[5]["value"]
    month_6 = return_int_value(a, b)

    b = registers.get(2125)[5]["value"]
    a = registers.get(2126)[5]["value"]
    month_7 = return_int_value(a, b)

    b = registers.get(2127)[5]["value"]
    a = registers.get(2128)[5]["value"]
    month_8 = return_int_value(a, b)

    b = registers.get(2129)[5]["value"]
    a = registers.get(2130)[5]["value"]

    month_9 = return_int_value(a, b)

    b = registers.get(2131)[5]["value"]
    a = registers.get(2132)[5]["value"]
    month_10 = return_int_value(a, b)

    b = registers.get(2133)[5]["value"]
    a = registers.get(2134)[5]["value"]
    month_11 = return_int_value(a, b)

    b = registers.get(2135)[5]["value"]
    a = registers.get(2136)[5]["value"]
    month_12 = return_int_value(a, b)

    sdata = {
        "uvid": uid,
        "slave": slave_id,
        "pv1_voltage": registers.get(45056)[5]["value"],
        "pv2_voltage": registers.get(45059)[5]["value"],
        "pv3_voltage": registers.get(45062)[5]["value"],
        "pv1_current": registers.get(45057)[5]["value"],
        "pv2_current": registers.get(45060)[5]["value"],
        "pv3_current": registers.get(45063)[5]["value"],
        "pv1_power": registers.get(45058)[5]["value"],
        "pv2_power": registers.get(45061)[5]["value"],
        "pv3_power": registers.get(45064)[5]["value"],
        "daily_energy": registers.get(1071)[5]["value"],
        "runtime_energy":  runtime_energy,
        "month_0": month_0,
        "month_1": month_1,
        "month_2": month_2,
        "month_3": month_3,
        "month_4": month_4,
        "month_5": month_5,
        "month_6": month_6,
        "month_7": month_7,
        "month_8": month_8,
        "month_9": month_9,
        "month_10": month_10,
        "month_11": month_11,
        "month_12": month_12,
        "apparent_power":  registers.get(49200)[5]["value"],
        "vers":vers,
        "recordedAt": timesend
    }
    return sdata
