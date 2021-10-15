import pandas as pd                   
import numpy as np                    
from datetime import datetime             #to manipulate dates
import plotly.express as px           
import plotly.graph_objects as go
from jupyter_dash import JupyterDash 
import dash_core_components as dcc  
import dash_html_components as html 

print("Please provide us with csv file of your tansactions")
df = pd.read_csv("transactions.csv") 
m=int(input("The starting transaction"))
n=int(input("The last transaction"))
df[m:n]
rejected_details=input("enter columns names which you don't want to include")
df = df[df.category != rejected_details] 
df.amount = df.amount*(-1) 
Total_Monthly_Expenses_Table = df.groupby('Year_on_month')['amount'].sum().reset_index(name = 'sum')
Total_Monthly_Expenses_Chart = px.bar(Total_Monthly_Expenses_Table, x = "Year_on_month", y = "sum", title = "Total Monthly Expenses")
Total_Monthly_Expenses_Chart.update_yaxes(title = 'Expenses (Rs)', visible = True, showticklabels = True)
Total_Monthly_Expenses_Chart.update_xaxes(title = 'Date', visible = True, showticklabels = True)
Total_Monthly_Expenses_Chart.show()
df['category'] = np.where(df['description'].str.contains('Uber|Ola|Rapido|Taxi'), 'Transport', df['category'] )
df['starts'] = list( 
    map(lambda x: x.startswith('Paid|To|Transferred'), df['description'])) 
df.loc[df.starts == True, 'category'] = "Transfer"
df.drop('starts', axis=1, inplace=True)
df.category.replace(["Coffee|Tea", "Eating out", "Takeaway", "Lunch"], "Food",inplace=True)
Net_Worth_Table = df.groupby('year_month')['amount'].sum().reset_index(name ='sum')
Net_Worth_Table['cumulative sum'] = Net_Worth_Table['sum'].cumsum()
Net_Worth_Chart = go.Figure(
    data = go.Scatter(x = Net_Worth_Table["year_month"], y = Net_Worth_Table["cumulative sum"]),
    layout = go.Layout(
        title = go.layout.Title(text = "Net Worth Over Time")
    )
)
Net_Worth_Chart.update_layout(
    xaxis_title = "Date",
    yaxis_title = "Net Worth (Rs)",
    hovermode = 'x unified'
    )
Net_Worth_Chart.update_xaxes(
    tickangle = 45)
Net_Worth_Chart.show()
