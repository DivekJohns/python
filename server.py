from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.TaskManager

app = Flask(__name__)

app.config.update(dict(SECRET_KEY='yoursecretkey'))
@app.route('/add/<int:a>/<int:b>')
def show_blog(a,b):
   return str(a+b)

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/admin')
def hello_admin():
    return 'Hello admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as guest'% guest

@app.route('/user/<name>')
def hello_user(name):
    if name =='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest = name))

@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return 'welcome post %s' % user
    else:
        user = request.args.get('name')
        return render_template('student.html', url = request.url_root+'result')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
       return render_template("result.html",result =  request.form)

@app.route('/mongo',methods = ['POST', 'GET'])
def adddb():
   if request.method == 'POST': 
    task = {'id':"task_id", 'title':'title', 'shortdesc':'shortdesc', 'priority':'priority'}
    db.tasks.insert_one(task)
    return 'updated'

if __name__ == '__main__':
   app.run()