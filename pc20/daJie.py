import requests
from mongoSitting import sava_to_mongo
from multiprocessing import Pool
from sitting import *

keyWordLen = get_keyWordLen()

def sava_result(resjson):
    print(resjson)
    for item in resjson["list"]:
        try:
            dic = {}
            dic["keyWord"]=resjson["keyword"]
            dic["companyName"]=item["compName"]
            dic["positionName"]=item["jobName"]
            dic["workYear"]=item["pubEx"]
            dic["education"]=item["pubEdu"]
            dic["city"]=item["pubCity"]
            dic["salary"]=(int(item["salary"].split('-')[0].split('K')[0])+int(item["salary"].split('-')[1].split('K')[0]))/2
            sava_to_mongo(dic)
        except:
            continue
def main(i):
    for j in range(0,keyWordLen):
        keyWord= get_keyWord(j)
        firstUrl = 'https://so.dajie.com/job/search'
        url = 'https://so.dajie.com/job/ajax/search/filter?keyword='+keyWord+'&order=0&city=&recruitType=&salary=&experience=&page='+str(i+1)+'&positionFunction=&_CSRFToken=ZHc07e-ibW9qugRFMAllwA6MvdUiieGIdXGM4w1h&ajax=1'
        session = requests.session()
        session.get(firstUrl)
        session.headers['referer'] = firstUrl
        response = session.get(url)
        sava_result(response.json()["data"])

if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i*1 for i in range(10)])