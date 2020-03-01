import pymysql
db = pymysql.connect("localhost","root","root","pc20")
sql = 'insert into dataPosition values (123,"python","北京","百度","实习生","7.5",3,"研究生")'
cursor=db.cursor()
cursor.execute(sql) #执行sql语句，返回sql查询成功的记录数目,我只在表中插入一条记录，查询成功最多所以也就一条记录数
db.commit()
db.close()


