import pymongo
import csv
MONGO_URL = 'localhost'
MONGO_DB = 'zhaopin20'
MONGO_TABLE = 'zhaopin20'

keyWord = ["C++","java", "python", "前端","嵌入式", "算法"]
CityList = ["cppCity","javaCity","pythonCity","qianduanCity","qianrushiCity","suanfaCity"]
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
def sava_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('存储成功')
        return None
    return False


def select_on_mongo(i):
    array = list(db[CityList[i]].find().sort("value",pymongo.DESCENDING))
    for j in range(0,len(array)):
        arrayRow=[array[j]['_id'],array[j]['value'],keyWord[i]]
        with open("city.csv","a") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(arrayRow)
    print(array)

def select_salaryRange():
    with open("salaryRange.csv",'a')as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(["keyWord","range","num"])
    salaryRange=list(db['salaryRange'].find({}))
    for i in range(0,len(salaryRange)):
        with open("salaryRange.csv",'a')as csvFile:
            writer=csv.writer(csvFile)
            writer.writerow([salaryRange[i]['keyWord'],salaryRange[i]['range'],salaryRange[i]['num']])

def select_salary():
    with open("avgSalary.csv", "w") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(["keyWord","avgSalary"])
    avg_salary = list(db[MONGO_TABLE].aggregate([{"$group":{"_id":"$keyWord","avgSalary":{"$avg":"$salary"}}}]))
    for i in  range(0,6):
        with open("avgSalary.csv", "a") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([avg_salary[i]['_id'], avg_salary[i]['avgSalary']])


with open("city.csv","w") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["city","value","keyWord"])


select_salaryRange()
# for i in range(0,6):
#   select_on_mongo(i)
# select_salary()