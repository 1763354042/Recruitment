import requests
from bs4 import BeautifulSoup as bs
from save import save_to_mysql

def save_request(res):
    soup = bs(res,'lxml')
    jobUlList = soup.find(attrs={'class':'job-list'})
    ul = jobUlList.find('ul')
    jobList = ul.find_all('li')
    resStr = ''
    keyWord = 'python'
    for li in jobList:
        try:
            jobName = li.find(attrs={'class':'job-name'}).text
            jobArea = li.find(attrs={'class': 'job-area'}).text
            jobLimit = li.find(attrs = {'class':'job-limit clearfix'})
            jobSalay = jobLimit.find(attrs={'class':'red'}).text
            jobWorkYear = str(jobLimit.find('p')).split('<em class="vline"></em>')[0][3:]#原页面在<p>里面内嵌了一个<em>
            jobEducation = str(jobLimit.find('p')).split('<em class="vline"></em>')[1][:-4]
            jobCom = li.find(attrs={'class':'company-text'}).find_all('a')[0].text
            resStr += "('"+keyWord+"','"+jobArea+"','"+jobCom +"','"+ jobName +"'," \
                    "'"+ jobSalay +"','"+ jobWorkYear +"','"+ jobEducation + "'),"
            # 数据库顺序keyword,address,company,position,salary,workYear,education
        except:
            print(resStr)
    resStr = resStr[:-1]
    save_to_mysql(resStr)

def main():
    firstUrl = 'https://www.zhipin.com/job_detail/?query=python&city=101010100&industry=&position='
    url = 'https://www.zhipin.com/job_detail/?query=python&city=101010100&industry=&position='
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept - language': 'zh - CN, zh;q = 0.9',
        'cache-control': 'max-age=0',
        'referer': 'https://www.zhipin.com/beijing/'
    }
    cookie = {
        'lastCity':'101010100',
        '_uab_collina':'158233910076371617050322',
        '_bl_uid':'d1kwa6pCx5R59F8Cv8dj3wjke29R',
        '__c':'1582973565',
        '__g':'-',
        'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a':'1582676834,1582937864,1582969539,1582973565',
        '__l':'l=https%3A%2F%2Fwww.zhipin.com%2Fbeijing%2F&r=https%3A%2F%2Fwww.zhipin.com%2Fbeijing%2F&friend_source=0&friend_source=0',
        '__zp_stoken__':'2e9cRIcHRRcNv4k4JvCHRWTiqzkzXxnzaMMej8pi2DcJqhd1%2BVToUGXKw0js9t5AG8yreFoVrpwuZb6K4mI9CLCD2YsW3rlTJctSPwmqfwrL6d4SH%2BS89joQwqP1EZO73zFT',
        '__a':'53900574.1582339101.1582937864.1582973565.277.7.7.277',
        'Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a':'1582984755'
}
    response = requests.get(firstUrl,headers=headers)
    returnCookie = requests.utils.dict_from_cookiejar(response.cookies)
    cookie.update(returnCookie)
    response = requests.get(url,headers=headers,cookies = cookie)
    print(response.text)
    save_request(response.text)



if __name__ == '__main__':
        main()