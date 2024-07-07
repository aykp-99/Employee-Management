import streamlit as st
import mysql.connector
st.title("Application")
empid=st.text_input("Enter employee ID:")
ename=st.text_input("Enter Your name:")
salary=st.text_input("Enter Salary")
loan=st.selectbox("Do you have a Loan",("Yes","No"))
btn=st.button("submit")
if btn:
    mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee1")
    c=mydb.cursor()
    c.execute("insert into info values(%s,%s,%s,%s)",(empid,ename,loan,salary))
    mydb.commit()
    st.header("Data Submitted Successfully")