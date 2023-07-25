import psycopg2
from flask import Flask,render_template,redirect,request,url_for    

app=Flask(__name__)

def db_conn():
    conn=psycopg2.connect(database="connectdb",host="localhost",port="5432",user="postgres",password="1234")
    return conn



@app.route('/')
def index():    
    conn=db_conn()
    cur=conn.cursor()
    cur.execute('''select * from courses order by id''')    
    data=cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html',data=data)

@app.route('/create',methods=['POST'])
def create():
    conn=db_conn()
    cur=conn.cursor()
    name=request.form['name']
    fees=request.form['fees']
    duration=request.form['duration']
    cur.execute('''insert into courses (name,fees,duration) values(%s,%s,%s)''',(name,fees,duration))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update',methods=['POST'])
def update():
    conn=db_conn()
    cur=conn.cursor()
    name=request.form['name']   
    fees=request.form['fees']
    duration=request.form['duration']
    id=request.form['id']
    cur.execute('''update courses set name=%s,fees=%s,duration=%s where id=%s''',(name,fees,duration,id))
    conn.commit()
    return redirect(url_for('index'))



@app.route('/delete',methods=['POST'])
def delete():
    conn=db_conn()
    cur=conn.cursor()
    id=request.form['id']
    cur.execute('''delete from courses where id=%s''',(id))
    conn.commit()   
    return redirect(url_for('index'))




