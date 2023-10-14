from flask import Flask,render_template,jsonify,request,redirect,url_for,make_response
app = Flask(__name__)

DATA_DICT = {
    '1': {'name': 'meowrain',"age":73},
    '2': {'name': 'meow',"age":84}
}

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    password = request.form.get('password')
    if user == 'meowrain' and password == 'yyds':
        resp = make_response("<h2>Cookie</h2>")
        resp.set_cookie('username',user,domain='127.0.0.1:7890')
        resp.set_cookie('password',password,domain='127.0.0.1:7890')
        return redirect('/index')
    else:
        msg_err = '用户名或者密码错误'
        return render_template('login.html',msg_err=msg_err)

@app.route('/index',endpoint='idx')
def index():
    data_dict = DATA_DICT
    length = len(data_dict)
    return render_template('layout.html',datas=data_dict,length=length)

@app.route('/edit/<nid>',methods=['GET','POST'])
def edit(nid):
    if request.method== 'GET':
        info = DATA_DICT[str(nid)]
        return render_template('edit.html',info=info)
    user = request.form.get('user')
    age = request.form.get('age')
    DATA_DICT[nid]['name'] = user
    DATA_DICT[nid]['age'] = age
    return redirect(url_for('idx'))

@app.route('/delete/<nid>')
def delete(nid):
   del DATA_DICT[nid]
   return redirect(url_for('idx'))

@app.route('/add_users',methods=['GET','POST'])
def add_users():
    if request.method == 'GET':
        return render_template('add.html')
    user = request.form.get('user')
    age = request.form.get('age')
    new_id = str(len(DATA_DICT) + 1)
    DATA_DICT[new_id] = {'name':user,'age':age}
    return redirect(url_for('idx'))

@app.route('/cookie',methods=['GET'])
def cookie():
    resp = make_response("<h2>Cookie</h2>")
    resp = make_response("<h2>Cookie</h2>")
    resp.set_cookie('username','meowrain',domain='127.0.0.1:7890')
    resp.set_cookie('password','yyds',domain='127.0.0.1:7890')
    return resp
if __name__ == '__main__':
    app.run(debug=True)