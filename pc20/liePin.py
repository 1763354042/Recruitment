import requests
from bs4 import BeautifulSoup as bs
from mongoSitting import *
from sitting import *
from multiprocessing import Pool

keyWordLen = get_keyWordLen()

def string_handle(soup,keyWord):
    ul = soup.find(attrs={'class': 'sojob-list'})
    lis = ul.find_all('li')
    for li in lis:
        try:
            a = li.find_all('a')
            span = li.find_all('span')
            position = {
                'keyWord': keyWord,
                'companyName': a[2].text.lstrip(),
                'positionName': a[0].text.lstrip(),
                'workYear': span[2].text,
                'education': span[1].text,  # test  出错******************************************
                'city': a[1].text.lstrip(),
                'salary': (float((span[0].text[:-1]).split('-')[0]) + float((span[0].text[:-1]).split('-')[1])) / 2
            }
            sava_to_mongo(position)
            print(position)
        except:
            continue




def main(i):
    for j in range(0,keyWordLen):
        keyWord = get_keyWord(j)
        url = 'https://www.liepin.com/zhaopin/?ckid=f85a7e2cdb27186c&fromSearchBtn=2&init=-1&sfrom=click-pc_homepage-centre_searchbox-search_new&degradeFlag=0&key='+keyWord+'&headckid=f85a7e2cdb27186c&d_pageSize=40&siTag=I-7rQ0e90mv8a37po7dV3Q%7EfA9rXquZc5IkJpXC-Ycixw&d_headId=6b34de8295422a575511f372881718fa&d_ckId=6b34de8295422a575511f372881718fa&d_sfrom=search_fp&d_curPage='+str(i+1)+'&curPage='+str(i)
        headers = {
            'proxies' : 'https://' + get_proxy()
        }
        res = requests.get(url,headers=headers).text
        print(res)
        soup = bs(res, 'lxml')
        string_handle(soup,keyWord)


if __name__=="__main__":
    pool=Pool()
    pool.map(main,[i*1 for i in range(0,30)])
