import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='db')


cursor = db.cursor()
name = input("请输入姓名:")
age = int(input("请输入年龄:"))
sex = input("请输入性别:")
math = int(input("请输入数学成绩:"))
Chinese = int(input("请输入语文成绩:"))
English = int(input("请输入英语成绩:"))
# print(param)
# sql = "select * from grade where math > 80"
sql = f"insert into grade(cname,cage,csex,math,Chinese,English) values ('{name}',{age},'{sex}',{math},{Chinese},{English})"
# print(sql)
cursor.execute(sql)

# results = cursor.fetchall()
#
# for i in results:
#     print(i)
#     print(type(i))

# 执行sql语句
db.commit()

# 关闭数据库连接
db.close()
cursor.close()



























