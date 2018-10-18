import requests
import json
from mongoSitting import sava_to_mongo
from multiprocessing import Pool

def get_keyWord(i):
    with open('sitting.json','r',encoding='utf-8') as load_f:
        keyWord = json.load(load_f)["keyWord"]
        lens = len(keyWord)
        print(lens)
        keyWord = keyWord[i%lens]
    return keyWord

PROXY_POOL_URL = 'http://127.0.0.1:5555/random'
def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None


def main(i):
    keyWord= get_keyWord(i)
    proxy = get_proxy()
    proxies = {
        'http':'http://'+proxy,
        'https':'https://'+proxy
    }
    firstUrl = 'https://so.dajie.com/job/search'
    url = 'https://so.dajie.com/job/ajax/search/filter?keyword='+keyWord+'&order=0&city=&recruitType=&salary=&experience=&page='+str(i+1)+'&positionFunction=&_CSRFToken=ZHc07e-ibW9qugRFMAllwA6MvdUiieGIdXGM4w1h&ajax=1'
    session = requests.session()
    session.get(firstUrl)
    session.headers['referer'] = firstUrl
   # session.headers['proxies'] = proxies
    responose = session.get(url)
    print(responose.text)

if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i*1 for i in range(10)])