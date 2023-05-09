######################
# 4) excel에서 읽고, 쓰는 방법
#######################


import pandas as pd

myexcel ="https://github.com/dongmisw/python_programming/blob/main/data/population.xlsx?raw=true" 
df = pd.read_excel(myexcel)
print(df)
df.to_excel('excel_write.xlsx')


mycsv = "https://raw.githubusercontent.com/dongmisw/python_programming/main/data/FL_insurance_sample.csv"
df = pd.read_csv(mycsv)   # csv 읽기
print(df)
df.to_csv('csv_write.csv')  # csv 저장하기

 