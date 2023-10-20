import streamlit as st
import pandas as pd
import mysql.connector
import datetime
from sqlalchemy import create_engine
st.set_page_config(page_title="Employee Management System",page_icon="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.kpi.com%2Fen%2Fblog%2F2019%2F07%2F17%2Fcore-elements-of-human-resource-management-system%2F&psig=AOvVaw1ibjTtQ_avY3eTfUN9HyMH&ust=1684576791869000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCMCUoOOPgf8CFQAAAAAdAAAAABAD")
choice=st.sidebar.selectbox("MyMenu",("Home","Employee Login","Admin","Employee List"))
if(choice=="Home"):
    st.image("https://www.kpi.com/wp-content/uploads/2019/07/cropped-Core-elements-of-human-resource-management-system-1200x630.png")
    st.markdown("<center><h1>Employee Management System</h1><center>",unsafe_allow_html=True)
    st.markdown("<center><h2 style=font-size:20px; text-align: center; color: grey;>This is a web Application developed by Gagan as part of project </h2>", unsafe_allow_html=True)
elif(choice=="Employee Login"):
    if 'login' not in st.session_state:
        st.session_state['login']=False
    eid=st.text_input("Enter employee id")
    upwd=st.text_input("Enter Password")
    btn=st.button("Login")
    if btn: 
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")
        c=mydb.cursor()
        c.execute("select * from users")
        for r in c:
            if(r[1]==upwd) and (r[2]==eid):
                st.session_state['login']=True
                break
        if(not st.session_state['login']):
                st.write("Incorrect id or password")
    if(st.session_state['login']):
        choice2=st.selectbox("Features",("None","Information"))  
        if(choice2=="Information"): 
            my_conn = create_engine("mysql+mysqldb://root:12345678@localhost/employee")
            query="select employee_name,employee_designation,employee_Salary from employee LEFT JOIN users ON employee.employee_id=users.employee_id where employee.employee_id=%s AND user_pwd=%s"
            df= pd.read_sql(query,my_conn,params=(eid,upwd,))
            st.dataframe(df)
            
elif(choice=="Admin"):
    if 'alogin' not in st.session_state:
        st.session_state['alogin']=False
    aid=st.text_input("Enter admin id")
    apwd=st.text_input("Enter Password")
    btn=st.button('login')
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")
        c=mydb.cursor()
        c.execute("select * from admins")
        for r in c:
            if(r[0]==aid) and (r[1]==apwd):
                st.session_state['alogin']=True
                break
            if(not st.session_state['alogin']):
                st.write("Incorrect id or password")
    if(st.session_state['alogin']):
        choice3=st.selectbox("Features",("None","Add new employee account","Delete employee account","Change existing employee account"))
        if(choice3=="Add new employee account"):
            eid=st.text_input("Enter employee id")
            email=st.text_input("Enter email id")
            epwd=st.text_input("Enter employee password")
            ename=st.text_input("Enter employee name")
            edesig=st.text_input("Enter employee designation")
            esal=st.text_input("Enter employee salary")
            btn=st.button('Add account')
            if btn:
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")
                c=mydb.cursor()
                c.execute("insert into users values(%s,%s,%s)",(email,epwd,eid))
                c.execute("insert into employee values(%s,%s,%s,%s)",(eid,ename,edesig,esal))
                mydb.commit()
                st.header("Employee Added Successfully")
        elif(choice3=="Delete employee account"):
            eid=st.text_input("Enter employee id")
            btn=st.button('Delete account')
            if btn:
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")
                c=mydb.cursor()
                c.execute("Delete from employee where employee_id=%s",(eid,))
                c.execute("Delete from users where employee_id=%s",(eid,))
                mydb.commit()
                st.header("Employee account deleted Successfully")
        elif(choice3=="Change existing employee account"):
            eid=st.text_input("Enter employee id")
            pid=st.text_input("Enter promoted profile")
            sid=st.text_input("Enter updated Salary")
            btn=st.button("Update account")
            if btn:
                 mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")
                 c=mydb.cursor() 
                 c.execute("Update employee set employee_designation=%s, employee_salary=%s where employee_id=%s",(pid,sid,eid,))
                 mydb.commit()
                 st.header("Employee account updated Successfully")
elif(choice=="Employee List"):
    if 'blogin' not in st.session_state:
        st.session_state['blogin']=False
    eid=st.text_input("Enter user ID")
    epwd=st.text_input("Enter password")
    btn=st.button('login')
    if(btn):
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")
        c=mydb.cursor()
        c.execute("select * from users")
        for r in c:
            if((r[0]==eid) and (r[1]==epwd)):
                st.session_state['blogin']=True
                break
            if(not st.session_state['blogin']):
                st.write("Incorrect id or password")
    if(st.session_state['blogin']):
        choice4=st.selectbox("Features",("None","Show the list of all employees"))
        if(choice4=="Show the list of all employees"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")
            df=pd.read_sql("select employee_name, employee_designation from employee",mydb)
            st.dataframe(df)
    
        
    
    
    

    
                

            
                    
       
           
                
            
                
                
                
                
                
        
