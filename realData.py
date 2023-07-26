'''
Author: callus
Date: 2023-07-26 16:59:48
LastEditors: callus
Description: some description
FilePath: /drug-shortage-forecast/realData.py
'''

# import pandas as pd
# import openpyxl

# df = pd.read_excel('./realData/2020.6.xlsx', sheet_name=None)
# output_file = './realData/2020.6output.xlsx'
# writer = pd.ExcelWriter(output_file, engine='openpyxl')
# selected_columns = ['药品名称','增加数量','减少数量','期初库存','期末库存']
# result = {}

# for sheet_name in df:
#     data = df[sheet_name].loc[:, selected_columns]
#     result[sheet_name] = data

# for sheet_name in result:
#     print(f'{sheet_name}:')
#     print(result[sheet_name])

import pandas as pd
from openpyxl import Workbook

xlsx_file = pd.read_excel('./realData/2020.6output.xlsx', sheet_name=None)
output_file = './realData/2020.6output.xlsx'
writer = pd.ExcelWriter(output_file, engine='openpyxl')

selected_columns = ['药品名称','增加数量','减少数量','期初库存','期末库存']  # 指定要提取的列名称或索引

workbook = Workbook()
workbook.save(output_file)

for sheet_name, dataframe in xlsx_file.items():
    selected_data = dataframe[selected_columns]
    selected_data.to_excel(writer, sheet_name=sheet_name, index=False)

writer.save()


