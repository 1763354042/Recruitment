import requests
from multiprocessing import Pool
from mongoSitting import *
keyword = '嵌入式'

def string_2_json(res):
    json_result = res.json()['data']['results']
    for pos in json_result:
        if pos['salary'] =='薪资面议':
            continue
        position = {

            'keyWord': keyword,
            'companyName':pos['company']['name'],
            'positionName':pos['jobName'],
            'jobNature':pos['emplType'],
            'workYear':pos['workingExp']['name'],
            'education':pos['eduLevel']['name'],
            'city':pos['city']['items'][0]['name'],
            'salary':(float(pos['salary'].split('-')[0][:-1])+float(pos['salary'].split('-')[1][:-1]))/2
        }
        print(position)
        sava_to_mongo(position)


def main(i):
    url = 'https://fe-api.zhaopin.com/c/i/sou?start='+str(i*60)+'pageSize=60&cityId=489&salary=4001,6000&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw='+keyword+'&kt=3'
    res=requests.get(url)
    string_2_json(res)

if __name__ == '__main__':
    pool = Pool()
    pool.map(main,[i*1 for i in range(0,30)])