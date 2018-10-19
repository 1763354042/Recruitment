import requests
from multiprocessing import Pool
from mongoSitting import *
from sitting import *


def string_2_json(res,keyWord):
    json_result = res.json()['data']['results']
    for pos in json_result:
        if pos['salary'] =='薪资面议':
            continue
        position = {
            'keyWord': keyWord,
            'companyName':pos['company']['name'],
            'positionName':pos['jobName'],
            'workYear':pos['workingExp']['name'],
            'education':pos['eduLevel']['name'],
            'city':pos['city']['items'][0]['name'],
            'salary':(float(pos['salary'].split('-')[0][:-1])+float(pos['salary'].split('-')[1][:-1]))/2
        }
        print(position)
        sava_to_mongo(position)


def main(i):
    keyWord = get_keyWord(i)
    url = 'https://fe-api.zhaopin.com/c/i/sou?start='+str(i*60)+'pageSize=60&cityId=489&salary=4001,6000&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw='+keyWord+'&kt=3'

    headers = {
        'proxies' :'https://' + get_proxy(),
    }
    res=requests.get(url,headers=headers)
    string_2_json(res,keyWord)

if __name__ == '__main__':
    pool = Pool()
    pool.map(main,[i*1 for i in range(0,30)])