'''
Author: callus
Date: 2023-07-26 17:35:31
LastEditors: callus
Description: some description
FilePath: /drug-shortage-forecast/realDataDate.py
'''

import pandas as pd
from datetime import date
xlsx_file = pd.read_excel('./realData/2020.6.xlsx', sheet_name=None)
output_file = './realData/2020.6date.xlsx'
# for sheet_name, df in xlsx_file.items():
#     df['日期'] = sheet_name

# writer = pd.ExcelWriter(output_file, engine='openpyxl')

writer = pd.ExcelWriter(output_file, engine='openpyxl')

for sheet_name, df in xlsx_file.items():
    df['日期'] = sheet_name
    df.to_excel(writer, sheet_name=sheet_name, index=False)

writer._save()


