'''
Author: callus
Date: 2023-07-26 17:18:31
LastEditors: callus
Description: some description
FilePath: /drug-shortage-forecast/realDataOutputExcelAll.py
'''
import pandas as pd
from openpyxl import Workbook
readExcel=['./realData/2020.6dateAll.xlsx','./realData/2020.7dateAll.xlsx','./realData/2020.8dateAll.xlsx','./realData/2020.9dateAll.xlsx','./realData/2020.10dateAll.xlsx','./realData/2020.11dateAll.xlsx','./realData/2020.12dateAll.xlsx']
writeExcel=['./realData/2020.6dateAll.xlsx','./realData/2020.7dateAll.xlsx','./realData/2020.8dateAll.xlsx','./realData/2020.9dateAll.xlsx','./realData/2020.10dateAll.xlsx','./realData/2020.11dateAll.xlsx','./realData/2020.12dateAll.xlsx']
for i in range(0,7):
    xlsx_file = pd.read_excel(readExcel[i], sheet_name=None)
    output_file = writeExcel[i]
    writer = pd.ExcelWriter(output_file, engine='openpyxl')
    selected_columns = ['药品名称','增加数量','减少数量','期初库存','期末库存','日期'] # 指定要提取的列名称或索引
    output_data = {}
    for sheet_name, df in xlsx_file.items():
        selected_data = df[selected_columns]
        output_data[sheet_name] = selected_data
    output_dataframe = pd.concat(output_data, axis=1)
    output_dataframe.to_excel(writer, sheet_name='Result2', index=True)
    writer._save()
   
# xlsx_file = pd.read_excel('./realData/2020.6dateAll.xlsx', sheet_name=None)
# output_file = './realData/2020.6dateAll.xlsx'
# writer = pd.ExcelWriter(output_file, engine='openpyxl')

# selected_columns = ['药品名称','增加数量','减少数量','期初库存','期末库存'] # 指定要提取的列名称或索引
# output_data = {}

# for sheet_name, df in xlsx_file.items():
#     selected_data = df[selected_columns]
#     output_data[sheet_name] = selected_data

# output_dataframe = pd.concat(output_data, axis=1)
# output_dataframe.to_excel(writer, sheet_name='Result2', index=True)

# writer._save()
