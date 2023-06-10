import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='db1')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
sql = "select * from category"

cursor.execute(sql)

results = cursor.fetchall()

for i in results:
    print(i)
    print(type(i))

# 执行sql语句
db.commit()

# 关闭数据库连接
db.close()

