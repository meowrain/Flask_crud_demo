#!./venv/bin/python
import pymysql

# 打开数据库连接
db = pymysql.connect(host="127.0.0.1",user="root",password="123456",port=3306,database="meowrain")

cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print(data)
db.close()