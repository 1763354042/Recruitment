import requests
import json
import time
from multiprocessing import Pool
from mongoSitting import *
from sitting import *


def processing_result(res,keyWord):
    try:
        items=res['content']['positionResult']['result']
        for item in items:
                position = {
                    'keyWord': keyWord,
                    'companyName':item['companyShortName'],
                    'positionName':item['positionName'],
                    'workYear':item['workYear'],
                    'education':item['education'],
                    'city':item['city'],
                    'salary':(float(item['salary'].split('-')[0][:-1])+float(item['salary'].split('-')[1][:-1]))/2
                }
        sava_to_mongo(position)
        print(position)
    except:
        return None


def main(i):
    keyWord = get_keyWord(i)
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    data = {
        'first':'true',
        'pn':i,
        'kd':keyWord
    }

    headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
         'Host': 'www.lagou.com',
         'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
         'Upgrade-Insecure-Requests': '1',
         'X-Anit-Forge-Code': '0',
         'X-Requested-With': 'XMLHttpRequest',
         'proxies':'https://'+get_proxy()
    }
    print(headers["proxies"])
    res = requests.post(url,data=data,headers=headers)
    print(res.read().decode('utf-8'))
    json_result=res.json()
    processing_result(json_result,keyWord)
    time.sleep(1)

if __name__=='__main__':
    pool = Pool()
    pool.map(main,[i*1 for i in range(0,20)])
