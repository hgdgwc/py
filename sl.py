import re
import time
import requests
import json
import datetime
data = []
adc = []
rp = []
dat = {
    "msgtype": "text", 
    "text": {
        "content": "fdtest"
    }

}
webhook = "https://oapi.dingtalk.com/robot/send?access_token=d8e48ba8b2be0485a2e0d3aae1972fa3ccf8f4299ab968eaf886528b686bec61"
headers = {'content-type':"application/json"}
yesterday = str(datetime.date.today() + datetime.timedelta(-1))

try:
    f = open('./logs/'+yesterday+'.log','r+')
    for line in f:
        rp.append(line.split(' ')[1].split('milages')[0])
        data.append(line.split("milages:")[1].split(' ')[0])
        adc.append(float(line.split("adc:")[1].split('\n')[0]))
finally:
    if f:
        f.close()
        mil = (float(data[len(data)-1]) - float(data[0]))/1000
        adc.sort()
        dat['text']['content'] = '菜鸟4.1测试' + '\n' + '日期: ' + yesterday + '\n' + '开始时间: ' + str(rp[0]) + '\n' + '结束时间: ' + str(rp[len(rp)-1]) + '\n' + '行驶里程数: ' + str(mil) + 'm' + '\n' + '停车精度(最小值): '+str(adc[0]) + '\n' + '停车精度(最大值): ' + str(adc[len(adc)-1])
try:
    res = requests.post(webhook,data = json.dumps(dat),headers = headers)
except requests.exceptions.RequestException as e:
    print(e)