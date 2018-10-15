import requests
import json
import time
from multiprocessing import Pool
from mongoSitting import *

keyword = '嵌入式'
def open_sitting_file(i):
    with open('sitting.json',encoding='utf-8') as f:
        sitting = json.load(f)
        return sitting['user-agent'][i];

def processing_result(res):
    items=res['content']['positionResult']['result']
    for item in items:
        position = {
            'keyWord': keyword,
            'companyName':item['companyShortName'],
            'positionName':item['positionName'],
            'jobNature':item['jobNature'],
            'workYear':item['workYear'],
            'education':item['education'],
            'city':item['city'],
            'salary':(float(item['salary'].split('-')[0][:-1])+float(item['salary'].split('-')[1][:-1]))/2
        }
        sava_to_mongo(position)
        print(position)

def main(i):

    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    data = {
        'first':'true',
        'pn':i,
        'kd':keyword
    }
    headers = {
     'User-Agent': open_sitting_file(i),
     'Host': 'www.lagou.com',
     'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
     'Upgrade-Insecure-Requests': '1',
     'X-Anit-Forge-Code': '0',
     'X-Requested-With': 'XMLHttpRequest'
    }
    res = requests.post(url,data=data,headers=headers)
    json_result=res.json()
    processing_result(json_result)
    time.sleep(5)

if __name__=='__main__':
    pool = Pool()
    pool.map(main,[i*1 for i in range(0,20)])
