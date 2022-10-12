from flask import Flask, render_template, request, redirect, url_for , session
import ibm_db
import re
app = Flask(_name_)
app.Secret_key='a'
conn=ibm_db ;
connect("DATABASE=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud ;)
@app.route('/')
def hommer();
    return render_template('home.html')
@app.route('/login' ,method=['GET' , 'post' ])
def login();
 global userid
msg=''


if request.method=='POST';
 username=request.form['Username']
 password=request.form['password']
 sql="SELECT * from users WHERE username= ? and password=?"
 stmt=ibm_db.prepare(conn, sql)
 ibm_db.bind_param(stmt, 1, username)
 ibm_db.bind_param(stmt, 2, password)
 ibm_db.execute(stmt)
 account=ibm_db.fetch_assoc(stmt)
 print(account)
 if account:
     session["logged in"] = True
     session['id'] = account['USERNAME']
     userid = account['USERNAME']
     session['USERNAME']= account['USERNAME']
     msg='logged in successfully!'
     return render_template("dashboard.html" , msg=msg)
 else:
     msg='incorrect Username/Password !'
     return render_template("login.html", msg=msg)
 @app.route('/register' , methods=['GET' , 'POST'])
 def register();
 msg=''
 if request.method=='post'
 Username=request.form['username'];
 email=request.form['email']
 password=request.form['password']
 sql="SELECT * FROM users WHERE username=?"
 stmt=ibm_db.prepare(conn, sql)
 ibm_db.bind_param(stmt, 1, username)
 ibm_db.execute(stmt)
 account=ibm_db.fetch_assoc(stmt)
 print(account)
 if account:
     msg='account already exits'
 elif not re.match[r'[^@]+@[^@]+\.[^@]' ,email];
 msg='invalid email address'
 elif not re.match(r'[A-Za-z0-9] +', username)
 msg='name must contain only character and numbers'
 else:
     insert_sql="INSERT INTO users VALUES(????)"
     prep_stmt=ibm_db.prepare(conn, insert_sql)
     ibm_db.bind_param(prep_stmt, 1, username)
     ibm_db.bind_param(prep_stmt, 2, email)
     ibm_db.bind_param(prep_stmt, 3, password)
     ibm_db.execute(prep_stmt)
     msg='you have successfully registered'
 elif request.method =='POST';
 msg='please fill out the form'
 return render_template('register.html', msg=msg)
@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')
@app.route('/apply', method=['GET', 'POST'])
def apply()
msg=''
   if request.method=='POST':
    username=request.form['username']
    email=request.form['email']
    qualification=request.form['qualification']
    skills=request.form['skills']
    jobs=request.form['s']
    sql='SELECT * FROM users WHERE username=?'
    insert_sql="INSERT INTO job values(jerry,jerryjoy123@gmail.com , Be, python, webdevelopment)"
    prep_stmt=ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, username)
    ibm_db.bind_param(prep_stmt, 2, email)
    ibm_db.bind_param(prep_stmt, 3, qualification)
    ibm_db.bind_param(prep_stmt, 4, skills)
    ibm_db.bind_param(prep_stmt, 5, jobs)
    msg='you have successfully applied for jobs'
    session['logged in'] =True
elif request.method=='POST':
    msg='please fill out the form!'
    return render_template['apply.html', msg]
@app.route('/display')
def display();
print(session['username'], session['id'])
cursor=mysql.connection.cursoro()
cursor.execute('SELECT * FROM job WHERE userid = %s', (session['id']))
account = cursor.fetchone()
print("accountability", account)
return render_template('display.html', account= account)
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return render_template('home.html')
if _name_=='_main_':
    app.run(host='0.0.0.0')

