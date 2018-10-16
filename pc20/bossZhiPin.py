import requests
import json
import re
from bs4 import BeautifulSoup as bs
from mongoSitting import *
from multiprocessing import Pool
keyWord = ["C++","python","java"]

def open_sittintg_file(i):
    with open('sitting.json','r') as f:
        res=json.load(f)
        return res['user-agent'][i];

def string_handle(res,keyWord):
    soup = bs(res,'lxml')
    classname = soup.find(attrs={'class':'job-list'})
    lis = classname.find_all('li')
    for li in lis:
        position = {
            'keyWord':keyWord,
            'companyName':li.find_all('h3')[1].find('a').text,
            'positionName':li.find(attrs={'class':'job-title'}).text,
            'jobNature':'全职',
            'workYear':(li.find(attrs={'class':'info-primary'}).find('p').text).split(' ')[2][:-2],     #使用beautiSoup对其选择后，使用字符串拼接
            'education':(li.find(attrs={'class':'info-primary'}).find('p').text).split(' ')[2][-2:],
            'city':(li.find(attrs={'class':'info-primary'}).find('p').text).split(' ')[0],
            'salary':(float(li.find('span').text.split('-')[0][:-1])+float(li.find('span').text.split('-')[1][:-1]))/2
        }
        print(position)
        sava_to_mongo(position)

def main(i):
    headers = {
        'user-agent':open_sittintg_file(i%7)
    }
    url = 'https://www.zhipin.com/c100010000/h_100010000/?query='+keyWord[i%3]+'&page='+str(i)+'&ka=page-'+str(i)

    res = requests.get(url,headers=headers).text
    print(res)
    string_handle(res,keyWord[i%3])

if __name__=='__main__':
    pool = Pool()
    pool.map(main,[i*1 for i in range(1,30)])