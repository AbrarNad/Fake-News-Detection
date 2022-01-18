import os
import pandas as pd
import csv
import numpy as np
import math
from datetime import datetime
path = os.getcwd()
files = os.listdir(path)
print(files)
files_xls = [f for f in files if f[-3:] == 'csv']
print(files_xls)
df = pd.DataFrame()
z=[]
for f in files_xls:
    df=pd.read_csv(f)
    # print(df.dtypes)
    
    # print(df['Overperforming(+)/Underperforming(-) Score'])
    
    # df['Overperforming(+)/Underperforming(-) Score']=df['Overperforming(+)/Underperforming(-) Score'].str.replace("x","")
    x=[]
    i=0
    while i in range(df.shape[0]):
        dt_obj = datetime.strptime(df['Score Date (GMT)'][i],
                            '%Y-%m-%d %H:%M:%S')
        millisec = dt_obj.timestamp() * 1000
        x.append(millisec)
        i=i+1
    
    i=0
    x_dash=[]
    while i <len(x)-1:
        x_dash.append(x[i]-x[i+1])
        i=i+1
    print(x_dash)
    df['Overperforming(+)/Underperforming(-) Score']=df['Overperforming(+)/Underperforming(-) Score'].str.replace("x","")
    print(df['Overperforming(+)/Underperforming(-) Score'])
    x_double_dash=[] 
#calculating log of offset
    
    i=0
    while i <len(x_dash):
        
        x_double_dash.append(math.log10(x_dash[i]))
        i=i+1
    print(x_double_dash)
    # y=df['Overperforming(+)/Underperforming(-) Score'].astype(str)
    df=df[:-1]
    y= pd.to_numeric(df['Overperforming(+)/Underperforming(-) Score'], downcast="float")
    y=y
    # z = np.polyfit(x_double_dash,y,2)
    # print(z)
    z.append(np.polyfit(x_double_dash,y,2))
    # x=[]
    # j=0
    # while
z=pd.DataFrame(z)
z.to_csv('result.csv')