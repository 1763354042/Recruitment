import pymongo
MONGO_URL = 'localhost'
MONGO_DB = 'zhaopin20'
MONGO_TABLE = 'zhaopin20'

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
def sava_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('存储成功')
        return None
    return False