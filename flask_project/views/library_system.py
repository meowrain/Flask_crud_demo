from flask import Blueprint
from dbutils.pooled_db import PooledDB
import pymysql
lib_sys = Blueprint('lib_sys',__name__)

POOL = PooledDB(
    creator=pymysql,  # 使用连接数据库的模块
    maxconnections=6,  # 最大连接数
    mincached=2, # 初始化时候至少创建的空闲连接
    blocking=True, # 
    ping=1,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='meowrain',
    charset='utf8',
)

# db = pymysql.connect(host="127.0.0.1",user="root",password="123456",port=3306,database="meowrain")
db = POOL.connection()

def excute_sql(sql):
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close() # 把连接放回到连接池
    return result


@lib_sys.route('/login')
def login():
    result = excute_sql('SELECT VERSION()')
    return f'''
<h1>Mysql Version: {str(result[0][0])}
'''