from dbutils.pooled_db import PooledDB
import pymysql
class SqlHelper(object):
    def __init__(self):
        self.pool = PooledDB(
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
    def open(self):
        db = self.pool.connection()
        cursor = db.cursor()
        return db,cursor
    def close(self,cursor,db):
        cursor.close()
        db.close()
    def fetchall(self,sql,*args):    
        db,cursor = self.open()
        cursor.execute(sql,args)
        result = cursor.fetchall()
        self.close(cursor,db)
        return result

    def fetchone(self,sql,*args):
        db,cursor = self.open()
        cursor.execute(sql,args)
        result = cursor.fetchone()
        self.close(cursor,db)
        return result


db = SqlHelper()