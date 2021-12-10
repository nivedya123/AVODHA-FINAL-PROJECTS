import pymysql
x=pymysql.connect('localhost','root',''root1','avodha')
cr=x.cursor()
cr.execute('create table Employee(name char(20),age int)')
cr.execute('insert into Employee values("Adith",28)')
a='select * from Employee'
cr.execute(a)
res=cr.fetchall()
for i in res:
   print(i)
x.commit()
x.close()
