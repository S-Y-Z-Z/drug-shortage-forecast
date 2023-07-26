'''
Author: callus
Date: 2023-07-26 17:18:31
LastEditors: callus
Description: some description
FilePath: /drug-shortage-forecast/realDataOutputExcel.py
'''
import pandas as pd
from openpyxl import Workbook

xlsx_file = pd.read_excel('./realData/2020.6.xlsx', sheet_name=None)
output_file = './realData/2020.6output.xlsx'
writer = pd.ExcelWriter(output_file, engine='openpyxl')

selected_columns = ['药品名称','增加数量','减少数量','期初库存','期末库存'] # 指定要提取的列名称或索引
output_data = {}

for sheet_name, df in xlsx_file.items():
    selected_data = df[selected_columns]
    output_data[sheet_name] = selected_data

output_dataframe = pd.concat(output_data, axis=1)
output_dataframe.to_excel(writer, sheet_name='Result', index=True)

writer._save()
