import requests
import json
import time
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
webhook = "https://oapi.dingtalk.com/robot/send?access_token=c62c51bff3b38ead62968bd2fb22f6b0c8f346c635ccd4e782fa40ef0adc19a8"
headers = {'content-type':"application/json"}
dat['text']['content'] = 'a'
print(time.localtime(time.time()))
a = time.localtime(time.time())
c = time.strftime("%H:%M:%S",time.localtime(time.time()))
print(dat)
print(c)
print(type(c))
if c == '16:53:00':
    print(c)
#try:
#    res = requests.post(webhook,data = json.dumps(dat),headers = headers)
#except requests.exceptions.RequestException as e:
#    print(e)
    