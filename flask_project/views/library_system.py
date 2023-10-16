from ..utils.sqlhelper import *
from flask import Blueprint,Flask,render_template,jsonify,request,redirect,url_for,make_response,session
lib_sys = Blueprint('lib_sys',__name__)



# db = pymysql.connect(host="127.0.0.1",user="root",password="123456",port=3306,database="meowrain")


@lib_sys.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    password = request.form.get('password')
    result = fetchone('select username,password_hash from users where username=%s and password_hash=%s',user,password)
    username_sql = result[0]
    passowrd_sql = result[1]

    if user == username_sql and password == passowrd_sql:
        session['user'] = user
        session['password'] = password
        resp = make_response("<h2>Cookie</h2>")
        return '登录成功'
    else:
        msg_err = '用户名或者密码错误'
        return render_template('login.html',msg_err=msg_err)

