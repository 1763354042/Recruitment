import requests
import time
from multiprocessing import Pool
from mongoSitting import *
from sitting import *

keyWordLen = get_keyWordLen()

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
        print("error")
        return None


def main(i):
    for j in range(0,keyWordLen):
        keyWord = get_keyWord(j)
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
            'Content - Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Cookie':'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1540011570; LGUID=20180311181229-b48623f4-2514-11e8-b1ab-5254005c3644; user_trace_token=20180311181228-7716e61a-e833-48d2-b951-de9b16abd94d; _ga=GA1.2.759847673.1521777617; _gat=1; LGSID=20181020125930-ed715314-d424-11e8-bef2-5254005c3644; PRE_UTM=m_cf_cpt_sogou_pc; PRE_HOST=www.sogou.com; PRE_SITE=https%3A%2F%2Fwww.sogou.com%2Ftx%3Fquery%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26hdq%3Dsogou-site-c91e3483cf4f9005-0001%26ekv%3D3%26ie%3Dutf8%26; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_sogou_pc; LGRID=20181020130000-ff855cba-d424-11e8-8b9f-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1540011600; index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.2120929655.1540011601; WEBTJ-ID=%E2%80%8E2018%E2%80%8E%E5%B9%B4%E2%80%8E10%E2%80%8E%E6%9C%88%E2%80%8E20%E2%80%8E%E6%97%A5%E2%80%8E125929-1668fd7b2e24c5-0c8517f27b2798-784a5037-1049088-1668fd7b2e416a9; JSESSIONID=ABAAABAABEEAAJA8CCF7E6F92B685963EDC7114E1F1B4AA; TG-TRACK-CODE=index_search; SEARCH_ID=57902a22b12f47f7a1ce6f82f444d587',
            'proxies':'https://'+get_proxy()
        }

        res = requests.post(url,headers=headers,data=data)
        json_result=res.json()
        processing_result(json_result,keyWord)
        time.sleep(5)

if __name__=='__main__':
    pool = Pool()
    pool.map(main,[i*1 for i in range(0,10)])
