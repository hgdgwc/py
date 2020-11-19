import requests
import json
import logging
import math
import time
autoRun = True
charge = False
jsonData = {}
headers = {'connection':'close'}
def Get_Status():
    data = {}
    try:
        url = "http://192.168.1.99:8080/status.cgi"
        res = requests.get(url,headers =  headers) 
    except requests.exceptions.RequestException as e:
        print(e)
    data = res.json()
    return data
def setpositionByThingMa(posx,posy,op):
    try:
        res = requests.post("http://192.168.1.99:8080/setposbythingma.cgi",data = {'posX':posx,'posY':posy,'op':op}) 
    except requests.exceptions.RequestException as e:
        print(e)
    return res.status_code
def setNextTo(posx,posy):
    try:
        res = requests.post("http://192.168.1.99:8080/setposXY.cgi",data = {'posX':posx,'posY':posy}) 
    except requests.exceptions.RequestException as e:
        print(e)
    return res.status_code
def chargeon():
    try:
        res = requests.get("http://192.168.1.99:8080/chargeon.cgi")
    except requests.exceptions.RequestException as e:
        print(e)
    return res.status_code
def chargeoff():
    try:
        res = requests.get("http://192.168.1.99:8080/chargeoff.cgi")
    except requests.exceptions.RequestException as e:
        print(e)
    return res.status_code
while True:
    jsonData = Get_Status()
    battery = jsonData['battery']
    batteryfull = jsonData['batteryfull']
    xPosition = jsonData['posX']
    yPosition = jsonData['posY']
    if autoRun == True:
        if jsonData['arrived'] == True:
            if jsonData['fork'] == True:
                if charge == False:
                    if (battery < batteryfull * 0.4):
                        #setNextTo(0,0)
                        #autoRun = False
                        charge = True
                    if (math.fabs(jsonData['posX']) < 10) and (math.fabs(jsonData['posY'] - 2630) < 5):
                        setpositionByThingMa(2,7,4)
                    else:
                        setpositionByThingMa(0,7,2)
                       
                else:
                    if (xPosition == 0) and (yPosition > -70) and (yPosition < -60):
                        chargeon()
                    else:
                        setNextTo(0,0)
                    if (battery > batteryfull * 0.8):
                        chargeoff()
                        charge = False
    time.sleep(1)
            

                




