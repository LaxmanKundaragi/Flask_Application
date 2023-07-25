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
    cur.execute('''select * from Todo order by id''')    
    data=cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html',data=data)

@app.route('/create',methods=['POST'])
def create():
    conn=db_conn()
    cur=conn.cursor()
    Task=request.form['Task']
    no_of_days=request.form['no_of_days']
    status=request.form['status']
    cur.execute('''insert into todo (Task,no_of_days,status) values(%s,%s,%s)''',(Task,no_of_days,status))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update',methods=['POST'])
def update():
    conn=db_conn()
    cur=conn.cursor()
    Task=request.form['Task']   
    no_of_days=request.form['no_of_days']
    status=request.form['status']
    id=request.form['id']
    cur.execute('''update todo set Task=%s,no_of_days=%s,status=%s where id=%s''',(Task,no_of_days,status,id))
    conn.commit()
    return redirect(url_for('index'))



@app.route('/delete',methods=['POST'])
def delete():
    conn=db_conn()
    cur=conn.cursor()
    id=request.form['id']
    cur.execute('''delete from todo where id=%s''',(id))
    conn.commit()   
    return redirect(url_for('index'))




