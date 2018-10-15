import requests
s = requests.session()
import json
url1= 'https://www.qimai.cn/app/searchHints/device/iphone/country/cn/word/%E5%AD%90%E5%BC%B9%E7%9F%AD%E4%BF%A1'
url2 = 'https://api.qimai.cn/app/searchHints?analysis=IRIdAkAWTkUEA0tSWXELDU1DJRdTUwUGAQEOCQJQAXNCAA%3D%3D'
data2 = {
    'device':'iphone',
    'word%5B0%5D': '%E5%AD%90%E5%BC%B9%E7%9F%AD%E4%BF%A1',
    'country':'cn'
}
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'Host': 'api.qimai.cn',
    'Referer': 'https://www.qimai.cn/app/searchHints/device/iphone/country/cn/word/%E5%AD%90%E5%BC%B9%E7%9F%AD%E4%BF%A1',
    'Accept': 'application/json, text/plain, */*',
    'Cookie': 'PHPSESSID=4k0fr3f1amjgbpgvt2n2h64br2; Hm_lvt_ff3eefaf44c797b33945945d0de0e370=1535336619; Hm_lpvt_ff3eefaf44c797b33945945d0de0e370=1535336714; acw_tc=MTE1MzUzMzY3MDcxMTEuMTYuNjIuMjQ0NzgxYmFkMjMxNTM1MzM2NzA3ODE2Njk3MGU1MGM2YTU4YmRkM2NiNGVkNDljZDIwMTdkYzY1MWY2YWE5ODQ=; synct=1535336802.232',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive' ,
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.qimai.cn',
}
res1 = s.get(url1)
res2 = s.post(url2, data=data2, headers=headers2)

# json_result = res.json()
# print(json_result)
print(res2.text)