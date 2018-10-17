import requests
import json
from mongoSitting import *

keyWord = ["C++","python","java"]
def open_sitting_sitting(i):
    with open('sitting.json','r') as f:
        json_result = json.load(f)
        return json_result['user-agent'][i]

def main(i):
    headers = {
        'user-agent':open_sitting_sitting(i),
    }
    url = 'https://so.dajie.com/job/ajax/search/filter?keyword='+keyWord[i%3]+'&order=0&city=&recruitType=&salary=&experience=&page='+str(i)+'&positionFunction=&_CSRFToken=&ajax=1'
    res = requests.get(url,headers=headers)
    print(res.text)

if __name__ == '__main__':
    main(1)