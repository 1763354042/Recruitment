import requests
import json
import re
from bs4 import BeautifulSoup as bs
from mongoSitting import *
from multiprocessing import Pool
from sitting import *

def string_handle(res,keyWord):
    soup = bs(res,'lxml')
    classname = soup.find(attrs={'class':'job-list'})
    lis = classname.find_all('li')
    for li in lis:
        position = {
            'keyWord':keyWord,
            'companyName':li.find_all('h3')[1].find('a').text,
            'positionName':li.find(attrs={'class':'job-title'}).text,
            'workYear':(li.find(attrs={'class':'info-primary'}).find('p').text).split(' ')[2][:-2],     #使用beautiSoup对其选择后，使用字符串拼接
            'education':(li.find(attrs={'class':'info-primary'}).find('p').text).split(' ')[2][-2:],
            'city':(li.find(attrs={'class':'info-primary'}).find('p').text).split(' ')[0],
            'salary':(float(li.find('span').text.split('-')[0][:-1])+float(li.find('span').text.split('-')[1][:-1]))/2
        }
        print(position)
        sava_to_mongo(position)

def main(i):
    keyWord = get_keyWord(i)
    url = 'https://www.zhipin.com/c100010000/h_100010000/?query='+keyWord+'&page='+str(i)+'&ka=page-'+str(i)
    proxy = get_proxy()
    # proxies = {
    #     'https':'https://'+proxy,
    #     'http':'http://'+proxy,
    # }
    headers = {
        'user-agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/70.0.3538.67Safari/537.36',
        'proxies':'https://'+proxy

    }
    res = requests.get(url,headers=headers).text
    print(res)
    string_handle(res,keyWord)

if __name__=='__main__':
    pool = Pool()
    pool.map(main,[i*1 for i in range(0,2)])