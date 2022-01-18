import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from datetime import datetime
import csv
x = []
y = []

# # with open('history_post_1005886580192569.csv','r') as csv_file:
# #   # Read all rows data
# #   rows = csv.reader(csv_file)

# #   # Iterate thourgh rows
# #   for row in rows:
# #     x.append(row[2])
# #     y.append(row[3])
# # pyplot.plot(x,y)
# # print(x)
# # pyplot.show()
# import pandas as pd
# from matplotlib import pyplot

# # CSV File
# csv_file = ""

# # Read CSV File
# csv_data = pd.read_csv("history_post_1005886580192569.csv", delimiter=",")
# print(csv_data['log(time)'])
# print(csv_data['Score'])
# # Plotting the data
# pyplot.plot(csv_data['log(time)'], csv_data['Score'])

# # Display the Plot
# pyplot.show()
# # # calculate polynomial
# z = np.polyfit(csv_data['log(time)'], csv_data['Score'], 2)
# print(z)
import xlrd
loc = ("real3"+".xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
sheet.cell_value(0, 0)

#converting time to miliseconds 
for i in range(sheet.nrows):
    if i!=0:
        if i!=sheet.nrows-1:      
            y.append(sheet.cell_value(i,1))
        wrongValue = sheet.cell_value(i,0)
        year, m, d, h, i, s = xlrd.xldate_as_tuple(wrongValue, wb.datemode)
        timmme=str(year)+"-"+str(m)+"-"+str(d)+" "+str(h)+":"+str(i)+":"+str(s)
        dt_obj = datetime.strptime(timmme,
                        '%Y-%m-%d %H:%M:%S')
        millisec = dt_obj.timestamp() * 1000
        x.append(millisec)

# calculating offset between times
i=0
x_dash=[]
while i <len(x)-1:
    x_dash.append(x[i]-x[i+1])
    i=i+1
print('hello')
print(x_dash)
print('hello')    

x_double_dash=[] 
#calculating log of offset
import math
i=0
while i <len(x_dash):
    
    x_double_dash.append(math.log10(x_dash[i]))
    i=i+1

print('hello')
# pyplot.plot(x_double_dash,y)

# pyplot.show()
z = np.polyfit(x_double_dash,y,2)
print(z)
# result=[]
# result.append(z[0])
# result.append(z[1])
# result.append(z[2])
# all_coffs.append(result)

# header=['a','b','c','label']

# with open('coeffs.csv', 'w') as f: 
# write = csv.writer(f) 
# write.writerow(header) 
# write.writerows(result) 
