import requests
import json
import time
dat = {
    "msgtype": "text", 
    "text": {
        "content": "MC_2.0"
    }, 
    "at": {
        "atMobiles": [
            "156xxxx8827", 
            "189xxxx8325"
        ], 
        "isAtAll": "false"
    }

}
mc_status = {}
charge = False
ever = True
Emergency = False
webhook = "https://oapi.dingtalk.com/robot/send?access_token=dd9960d5296c666b9e4a97330424946609e1d189a53a40c3a5b9faa14fe35cbc"
url_mc = "http://192.168.1.51:8080/status.cgi"
headers = {'content-type':"application/json"}
def SendDataToDing(status):
    dat["text"]["content"] = 'MC_2.0' + str(status)
    try:
        print(dat["text"]["content"])
        res = requests.post(webhook,data=json.dumps(dat),headers=headers)        
    except requests.exceptions.RequestException as e:
        print(e)
    return res.status_code
def GetStatus():
    try:
        res = requests.get(url_mc)
    except requests.exceptions.RequestException as e:
        print(e)
    if res.status_code == 200:
        return res.json()
    else:
        return

while True:
    mc_status = GetStatus()
    c = time.strftime("%H:%M:%S",time.localtime(time.time()))
    t = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    if mc_status['port'] == 1:
        str3 = '已连接\r\n'
    else:
        str3 = '未连接\r\n'
    str2 = str(t) + '\r\n' + str(c) + '\r\n' + '行驶里程:' + str((mc_status['milages'])/1000000) + 'km' + '\r\n' + '当前电压' + str(mc_status['Bv']) +'v'+ '\r\n' + '电容电流:' + str(mc_status['C1']) +'A'+ '网络状态'+str3+'\r\n'
    if (mc_status['Bv'] < 40000):
        if charge == False:
            strin = '###电压低于' + str(mc_status['Bv'])+'\r\n'
            charge = True
            SendDataToDing(strin + str2)
    if (mc_status['Bv'] > 50000):
        if charge == True:
            charge = False
    if (c == '08:30:00'):
        if ever == True:
            ever = False
            SendDataToDing(str2)
    else:
        ever = True
    if (mc_status['sp'] == 0):
        if Emergency == False:
            m = time.time()
            Emergency = True
        if (time.time() - m ) > 60:
            strin = "###小车超过1min未行走\r\n"
            SendDataToDing(strin + str2)
            #Emergency = False
    else:
        Emergency = False
    
    SendDataToDing(str2)    
    time.sleep(3)


    




        
    



