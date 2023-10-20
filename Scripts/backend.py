import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")

#To Retrieve data from database
c=mydb.cursor()
c.execute("select * from employee")
for r in c:
    print(r)

import mysql.connector
import datetime
mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="library")

#To insert data from database
eid=input("Enter employee id")
email=input("Enter email id")
epwd=input("Enter employee password")
ename=input("Enter employee name")
edesig=input("Enter employee designation")
esal=input("Enter employee salary")
c=mydb.cursor()
c.execute("insert into users values(%s,%s,%s)",(email,epwd,eid))
c.execute("insert into employee values(%s,%s,%s,%s)",(eid,ename,edesig,esal))
mydb.commit()
print("Employee Added Successfully")

# To delete data from database
eid=input("Enter employee id of the employee to be deleted")
mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")
c=mydb.cursor()
c.execute("Delete from employee where employee_id=%s",(eid,))
c.execute("Delete from users where employee_id=%s",(eid,))
mydb.commit()
print("Employee account deleted Successfully")

# Change existing employee account
eid=input("Enter employee id")
pid=input("Enter promoted profile")
sid=input("Enter updated Salary")
mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")
c=mydb.cursor() 
c.execute("Update employee set employee_designation=%s, employee_salary=%s where employee_id=%s",(pid,sid,eid,))
mydb.commit()
print("Employee account updated Successfully")