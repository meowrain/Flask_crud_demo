from dbutils.pooled_db import PooledDB
import pymysql
POOL = PooledDB(
    creator = pymysql,  # 使用连接数据库的模块
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


def fetchall(sql,*args):    
    db = POOL.connection()
    cursor = db.cursor()
    cursor.execute(sql,args)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def fetchone(sql,*args):
    db = POOL.connection()
    cursor = db.cursor()
    cursor.execute(sql,args)
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result