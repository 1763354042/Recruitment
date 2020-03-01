from bs4 import BeautifulSoup as bs
import requests
from save import save_to_mysql
def save_request(request):
    soup = bs(request,'lxml')
    ul = soup.find(attrs={'class': 'sojob-list'})
    jobList = ul.find_all('li')
    resStr = ''
    keyWord = 'python'
    for li in jobList:
        try:
            a = li.find_all('a')
            span = li.find_all('span')  # 数据库顺序keyword,address,company,position,salary,workYear,education
            resStr += "('" + keyWord + "','" + a[1].text + "','" + a[2].text + "','" + a[0].text.lstrip() + "','" + span[
            0].text + "','" + span[2].text + "'," \
            "'" + span[1].text + "'),"
        except:
            a = li.find_all('a')
            span = li.find_all('span')
            print(len(a),len(span))
    resStr = resStr[:-1]  # 删除最后一个，在save_to_mysql内为最后一条数据后以";"结尾
    save_to_mysql(resStr)


def main():
    url = 'https://www.liepin.com/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new&d_sfrom=search_fp&key=python'
    res = requests.get(url).text
    save_request(res)


if __name__ == '__main__':
    main()