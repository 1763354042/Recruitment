import pymysql
def save_to_mysql(data):
    print("start sava_to_mysql")

    db = pymysql.connect("localhost","root","root","pc20")
    sql = 'insert into dataPosition (keyWord,address,company,position,salary,workYear,education)' \
          ' values '+ data+';'#data为传入字符串，在最后以";"结尾
    cursor=db.cursor()
    cursor.execute(sql) #执行sql语句，返回sql查询成功的记录数目,我只在表中插入一条记录，查询成功最多所以也就一条记录数
    db.commit()
    db.close()
    print(sql)

