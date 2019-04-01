import requests


def internet_on():
    try:
	
        request = requests.get(url='https://solardata2.tk/', timeout=1)
	#print("in try")
        return True
    except:
	#print("in wxce")
        return False


print(internet_on())
