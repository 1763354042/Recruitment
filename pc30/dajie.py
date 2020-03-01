import requests
from save import save_to_mysql
def sava_to_result(data):
    keyWord = data['keyword']
    resultListStr = ''
    for item in data["list"]:
        try:  # 如果没有工作年限和学历要求，则将其设为空格
            if "pubEx" not in item.keys():
                item["pubEx"] = ' '
            if "pubEdu" not in item.keys():
                item["pubEdu"] = ' '
            resultListStr += "('" + keyWord + "','" + item['pubCity'] + "','" + item['compName'] + "','" + item[
                'jobName'] + "','" + item['salary'] + "','" + item['pubEx'] + "','" \
                             + item['pubEdu'] + "'),"#将每条数据写到一个括号内，方便后期批处理
        except:
            print(item)
    resultListStr = resultListStr[:-1]              #删除最后一个，在save_to_mysql内为最后一条数据后以";"结尾
    print(resultListStr)
    save_to_mysql(resultListStr)
def main():
    firstUrl = 'https://so.dajie.com/job/search'
    url = 'https://so.dajie.com/job/ajax/search/' \
          'filter?keyword=python&order=0&city=&recruitType=&salary=&experience=&page=1&positionFunction=&' \
          '_CSRFToken=ZHc07e-ibW9qugRFMAllwA6MvdUiieGIdXGM4w1h&ajax=1'
    session = requests.session()
    session.get(firstUrl)
    session.headers['referer'] = firstUrl
    response = session.get(url)
    sava_to_result(response.json()["data"])

if __name__ == '__main__':
    main()