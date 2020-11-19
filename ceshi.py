import requests
import time
import math
import json
AutoRun = False
charing = False
AutoCharge = False
uptime = False
charge_time = 0
motion_time = 0
webhook = "https://oapi.dingtalk.com/robot/send?access_token=c62c51bff3b38ead62968bd2fb22f6b0c8f346c635ccd4e782fa40ef0adc19a8"
headers = {'content-type':"application/json"}
s = []
data = {}
dat = {
    "msgtype": "text", 
    "text": {
        "content": "fdtest"
    }, 
    "at": {
        "atMobiles": [
            "156xxxx8827", 
            "189xxxx8325"
        ], 
        "isAtAll": "false"
    }

}
while True:
    try:
        res = requests.get("http://192.168.1.51:8080/status.cgi") 
    except requests.exceptions.RequestException as e:
        print(e)
        continue
    data = res.json()
    if charing == False:
        if uptime == False:
            t = time.time()
            uptime = True  
        AutoRun = False
        if AutoCharge == False:
            try:
                ret = requests.post("http://192.168.1.97:5004/setposxy.cgi",data={'posX':0,'posy':0})
            except requests.exceptions.RequestException as e:
                print(e)
                continue
            #time.sleep(10)
            if math.fabs(data['posx']) < 10:
                if data['st'] == 'idle':
                    try:
                        res = requests.post("http://192.168.1.97:5004/charge.cgi",data={'posX':1})
                    except requests.exceptions.RequestException as e:
                        print(e)
                        continue    
                    s = res.status_code
                    print(s)
                    AutoCharge = True
                else:
                    time.sleep(1)
            else:
                time.sleep(1)
            
        if math.fabs(time.time() - t) > 1200:
            print("end charge")
            try:
                res = requests.post("http://192.168.1.97:5004/charge.cgi",data={'posX':2})
            except requests.exceptions.RequestException as e:
                print(e)
                continue
            charing = True
            AutoRun = True
                #AutoCharge = False
    if  AutoRun == True:
        if uptime == True:
            t = time.time()
            uptime = False
        if math.fabs(data['posx']) < 10:
            if data['st'] == 'idle':
                now = time.strftime("%Y-%m-%d",time.localtime(time.time()))
                c = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
                
                filename = "D:/logs/"+now+".log"
                print(data['posx'])
                a = str(data['posx'])
                b = str(data['adc[1]'])
                d = str(c)
                print(type(a))
                milages = str(data['mil'])
                try:
                    f = open(filename,'a+')
                    f.write(d+':'+' '+'milages:'+milages+' '+'pos:'+a+' '+'adc:'+b+'\n')
                finally:
                    if f:
                        f.close()
                #posx = str(data['posx'])
                #adc = str(data['adc[1]'])
                #print(posx)
                #print(adc)

                #try:
                #    f = open(filename,'a+')
                #    f.write(posx + ' '+adc+'\n')
                #finally:
                #    if f:
                #        f.close()
                try:
                    rep = requests.post("http://192.168.1.97:5004/setposxy.cgi",data={'posX':4000,'posy':0})
                except requests.exceptions.RequestException as e:
                    print(e)
                    continue
            #if rep == 200:
            #print(rep)
        if math.fabs(data['posx'] - 4000) < 10:
            if data['st'] == 'idle':
                try:
                    ret = requests.post("http://192.168.1.97:5004/setposxy.cgi",data={'posX':0,'posy':0})            
                except requests.exceptions.RequestException as e:
                    print(e)
                    continue
        if (time.time() - t) > 7200:
            print("start charge")
            AutoRun = False
            charing = False
            AutoCharge = False
    sh = time.strftime("%H:%M:%S",time.localtime(time.time()))
    if sh == "17:00:00":
        dat['text']['content'] = 'fd' + '\n' + 'milages:' + str(data['mil']) + '\n' 
    dat['text']
        try:
            res = requests.get(webhook,data = json.dumps(dat),headers = headers) 
        except requests.exceptions.RequestException as e:
            print(e)
            continue
    print(int(time.time()))

    
    time.sleep(1)