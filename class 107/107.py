import pandas as pd
import plotly.graph_objects as px
import csv

data=pd.read_csv('data.csv')
print(data.groupby('level')['attempt'].mean())
figure=px.Figure(px.Bar(x=data.groupby('level')['attempt'].mean(),y=['level 1','level 2','level 3','level 4'],orientation='h'))
figure.show()



