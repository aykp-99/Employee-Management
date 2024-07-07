from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pandas as pd
import plotly.express as px
#permission
                             
f=InstalledAppFlow.from_client_secrets_file('key.json',['https://www.googleapis.com/auth/spreadsheets'])
cred=f.run_local_server(port=0)
#to create a service
service=build('Sheets','v4',credentials=cred).spreadsheets().values()
#retrieve data from google sheets
d=service.get(spreadsheetId='1jwxRQkcJ-ZH8b4hZKn0S7w-lZNGeWkakDzhphR_Zyb4',range='A:M').execute()
print(d['values'])
mycolumn=d['values'][0]
mydata=d['values'][1:]
df=pd.DataFrame(data=mydata,columns=mycolumn)          
