import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector
import pandas as pd
import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import plotly.express as px
import numpy as np
from PIL import Image
st.set_page_config(page_title='Employee Management System',page_icon='random')


st.markdown(f'<h1 style="color: orange; text-align: center;">Employee Management System</h1>',unsafe_allow_html=True)
st.markdown("-----")
st.sidebar.image("man.jpg")
choice=st.sidebar.selectbox("All Apps",("Home","Employee DataBase","Personal Staffing Details","Official Details","Project Details","E-Learn","Cab Booking","Expense Claim")) 
if(choice=="Home"):
    
    st.image("https://i.pinimg.com/originals/33/93/b0/3393b04a2f206143b17f7a67a7ad5f0a.gif",width=500,channels="RBG")
    st.caption(':red[dreams & teams work together--------->Believe in Yourself--------->Hard Work Matters-------->Success]')
    st.markdown("-----")
    st.markdown(f'<p1 style="color:black; background-color: white;text-align: center;">The purpose of an employee management system is to help improve workforce productivity, identify ways to engage and retain talent, and alleviate administrative burdens for HR professionals. Achieving greater efficiency through the use of technology can also help control costs and minimize compliance risks.</p1>',unsafe_allow_html=True)
    st.markdown(f'<h2 style="color: blue; text-align: center;">WELCOME!!</h2>',unsafe_allow_html=True)
elif(choice=="Employee DataBase"):
    if 'login' not in st.session_state:
        st.session_state['login']=False
    adid=st.text_input("Enter  ADID")
    adpass=st.text_input("Enter Admin password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host='localhost',user='root',password='12345678',database='Employee')
        c=mydb.cursor()
        c.execute("select * from admin")
        for row in c:
            if(row[0]==adid and row[1]==adpass):
                st.session_state['login']=True
                st.subheader("Login Successful")
                break
        if(st.session_state['login']==False):
            st.subheader("Incorrect ID or password")
    if(st.session_state['login']==True):
        st.subheader("login Successful")
        url=st.text_input("Enter Google Sheet URL")
        r=st.text_input("Enter Range")
        btn2=st.button("View Details")
        if btn2:
            if 'cred' not in st.session_state:
                f=InstalledAppFlow.from_client_secrets_file('key.json',['https://www.googleapis.com/auth/spreadsheets'])
                st.session_state['cred']=f.run_local_server(port=0)
            service=build('Sheets','v4',credentials=st.session_state['cred']).spreadsheets().values()
            d=service.get(spreadsheetId=url,range=r).execute()
            
            mycolumn=d['values'][0]   
            mydata=d['values'][1:]
            df=pd.DataFrame(data=mydata,columns=mycolumn)
            st.dataframe(df)
            
elif(choice=="Personal Staffing Details"):
    st.markdown(f'<h2 style="color: black; text-align: center;">After successful login you can see your details(my data,my time and my beneficials)</h2>',unsafe_allow_html=True)
    if 'login' not in st.session_state:
        st.session_state['login']=False
    empid=st.text_input("Enter Employee ID")
    emppass=st.text_input("Enter Your password")
    btn1=st.button("Login")
    if btn1:
        mydb=mysql.connector.connect(host='localhost',user='root',password='12345678',database='Employee')
        c1=mydb.cursor()
        c1.execute("select * from emp_details")
        for row in c1:
            if(row[0]==empid and row[1]==emppass):
                st.session_state['login']=True
                st.subheader("Login Successful")
                break
        if(st.session_state['login']==False):
            st.subheader("Incorrect ID or password")
    if(st.session_state['login']==True):
        st.subheader("............")
        v=st.text_input("Enter your name")
    
            
   
            
        
        choice2=st.selectbox("ALL Data",("Select","My Data","My Time","My Policies"))
        if(choice2=="My Data"):
            mydb=mysql.connector.connect(host='localhost',user='root',password='12345678',database='Employee')
            c=mydb.cursor()
            c.execute("select * from emp_details")
           
           
            l=[]
            for row in c:
                
               
                l.append(row)
            
            df=pd.DataFrame(data=l,columns=["empid","emppass","emp_name","designation","salary","date_of_birth","Aadhar","nationality"])
            df2=df[df['emp_name']==v]
            st.dataframe(df2)
        elif(choice2=="My Time"):
            with st.form('time'):
                dno=st.number_input("No of days you worked in a week",0,7)
                eff=st.number_input("fill your efforts in hours.",0,10)
                start=st.date_input('select Start Date ')
                end=st.date_input('Select End date')
                sh=st.radio("Select your Shift",['Day','Night'])
                c=st.form_submit_button('Save')
                if c:
                    doi=str(datetime.datetime.now())
                    mydb=mysql.connector.connect(host='localhost',user='root',password='12345678',database='Employee')
                    c=mydb.cursor()
                    c.execute("insert into attendance values(%s,%s,%s,%s,%s,%s)",(dno,eff,doi,sh,start,end))
                    mydb.commit()
                    st.header("Data Added Successfully")
        elif(choice2=="My Policies"):
            st.title("Beneficials")
            st.markdown('<iframe src="https://www.wpi.edu/sites/default/files/FinalEmployeeHandbook.pdf" width="100%" height="400px"></iframe>',unsafe_allow_html=True)
                
            
                    
                    
            
           
elif(choice=="Official Details"):
    with st.form('My Form'):
        dname=st.text_input('Department Name')
        did=st.text_input('Department ID')
        ma=st.text_input('Manager ID')
        loc=st.text_input("Location")
        k=st.form_submit_button('Save')
          
        if k:
            mydb=mysql.connector.connect(host='localhost',user='root',password='12345678',database='Employee')
            c=mydb.cursor()
            c.execute("insert into dept_details values(%s,%s,%s,%s)",(did,dname,ma,loc))
            mydb.commit()
            st.header("Data Added Successfully")
            
elif(choice=='Project Details'):
    with st.form("My Manager"):
        empid=st.text_input("Employee ID")
        p=st.text_input("Project ID")
        Pn=st.text_input("Project Name")
        pm=st.text_input("Project Manager")
        nm=st.text_input("Your Name")
        m=st.form_submit_button('Save')
        if m:
            
            mydb=mysql.connector.connect(host='localhost',user='root',password='12345678',database='Employee')
            c=mydb.cursor()
            c.execute("insert into project_details values(%s,%s,%s,%s)",(p,pm,Pn,empid))
            mydb.commit()
            st.header("Data Added Successfully")
elif(choice=="Cab Booking"):
    st.image("car.gif")
    st.markdown(f'<h1 style="color: RED; text-align: center;">EASY TO GO ----- EASY FOR RIDE</h1>',unsafe_allow_html=True)
    st.caption(':blue[<<<Transport Booking System>>>>]')
    with st.form("my cab"):
        Eid=st.text_input("Employee ID")
        pid=st.text_input("Project ID")
        fac=st.selectbox("facility",["BDC1","CDC2","DDC2","DDC1","BDC14"])
        trip=st.date_input("Your Trip")
        mo=st.radio("Mode",["Pick","Drop"])
        sh=st.radio("Shift",["Day","Night"])
        l1=st.sidebar.selectbox("Locations",["DELHI NCR","HEYDRABAD","PUNE","BANGALORE","CHENNAI"])
        if(l1=="DELHI NCR"):
            st.selectbox("DELHI NCR ",["Sector 41","Sector 52","Alpha-1","KP2","Subhash Nagar","Pragati Maidan","Gurugram"])
        elif(l1=="BANGALORE"):
            st.selectbox("Locations",["JayaNagar","Indira Nagar","Rajaaji Nagar"])
        elif(l1=="CHENNAI"):
            st.subheader("Sorry Routes are not available for now")
        elif(l1=="HEYDRABAD"):
            st.selectbox("Locations",["Miyapur","Midhapur","Bibinagar","Ramoji Film City"])
        else:
            st.selectbox("Locations",["Bandra","Mulshi","Lavasa"])
        b=st.form_submit_button("Reserve Your Seat")
        if b:
            
            mydb=mysql.connector.connect(host='localhost',user='root',password='12345678',database='Employee')
            c=mydb.cursor()
            c.execute("insert into cab_book values(%s,%s,%s,%s,%s,%s,%s)",(Eid,pid,fac,trip,mo,sh,l1))
            mydb.commit()
            st.header("Data Added Successfully")
elif(choice=="Expense Claim"):
    #with st.form("my Expense"):
        selected=option_menu(
            menu_title="Select Category",
            options=["CONVEYANCE","MISCELLANEOUS","RELOCATION"],
            icons=["bus-front","menu-up","building"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
        )
        if selected=="CONVEYANCE":
            st.title("NOT APPLICABLE")
        elif selected =="MISCELLANEOUS":
            Pro=st.selectbox("Project",["HDFC8","apple","BOB Bank","ICICI Bank"])
            prom=st.selectbox("Project Manager",["Nitya","Nirala","Niraja","Priya"])
            ec=st.text_input("Expense Claim Amount")
            sb=st.selectbox("Sub Category",["Books","Broadband/Dongal/Data","Business Meet","Visa Fee","Incidental Meal","Courier Charges"])
            s=st.header("will be added")
            if s:
                mydb=mysql.connector.connect(host='localhost',user='root',password='12345678',database='Employee')
                c=mydb.cursor()
                c.execute("insert into expense_claim values(%s,%s,%s,%s)",(Pro,prom,ec,sb))
                mydb.commit()
                
            
        
            
                    
        
else:
    st.markdown(f'<h3 style="text-align: center; color: orange;">Welcome to E-Learn</h3>',unsafe_allow_html=True)
    st.markdown("------------")
    st.title("Dashboard")
    chart_data=pd.DataFrame(np.random.randn(10,2),columns=['your progress','your failure'])
    st.bar_chart(chart_data)
    choice3=st.selectbox("All Courses",("JAVA Programming Language","Python For DataScience","Data Structure","Basics In C","Cloud Computing"))
    if(choice3=="JAVA Programming Language"):
        st.image("javaimg.jfif",width=200)
        st.video("https://www.youtube.com/watch?v=-2CqJC-GnR4")
    elif(choice3=="Python For DataScience"):
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRh1ODZKxICuUJ5ajBerN6rNyXrs2yIF6dmXg&usqp=CAU")
        st.markdown('<iframe src="https://www.halvorsen.blog/documents/programming/python/resources/Python%20Programming.pdf" width="100%" height="400px"></iframe>',unsafe_allow_html=True)
    elif(choice3=="Data Structure"):
        st.video("https://www.youtube.com/watch?v=8e_PwxYGZrA")
    elif(choice3=="Basics In C"):
        st.video("https://www.youtube.com/watch?v=gEJBFKDkqTE")
    else:
        st.video("https://www.youtube.com/watch?v=M988_fsOSWo")
            

        
        
        
        
            
            
    
        
        



        
