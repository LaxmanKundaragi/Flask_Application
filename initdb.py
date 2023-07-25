import psycopg2

conn=psycopg2.connect(database="connectdb",host="localhost",user="postgres",password="1234",port="5432")
cur=conn.cursor()

cur.execute(''' create table if not exists Todo(id serial primary key,Task varchar(50),no_of_days integer,status varchar)''')

cur.execute('''insert into Todo(Task,no_of_days,status) values ('Python',25,'completed')''')
conn.commit()
cur.close()
conn.close()    