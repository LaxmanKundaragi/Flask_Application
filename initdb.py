import psycopg2

conn=psycopg2.connect(database="connectdb",host="localhost",user="postgres",password="1234",port="5432")
cur=conn.cursor()

cur.execute(''' create table if not exists courses(id serial primary key,name varchar(50),fees integer,duration integer)''')

cur.execute('''insert into courses(name,fees,duration) values ('C++',5000,55)''')
conn.commit()
cur.close()
conn.close()    