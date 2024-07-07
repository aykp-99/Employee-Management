import mysql.connector
import datetime

mydb=mysql.connector.connect(host='localhost',user='root',password='12345678',database='Employee')
c=mydb.cursor()

login=False
eid=input("enter id")
ename=input("enter name")
c.execute("select * from emp_details")
for row in c:
    if(eid==row[0] and ename==row[1]):
        login=True
        break
if(login):
    print("login successful")
else:
    print("incorrect eid or name")
