'''
Author: callus
Date: 2023-07-26 17:35:31
LastEditors: callus
Description: some description
FilePath: /drug-shortage-forecast/realDataDate.py
'''

import pandas as pd
from datetime import date
readExcel=['./realData/2020.6.xlsx','./realData/2020.7.xlsx','./realData/2020.8.xlsx','./realData/2020.9.xlsx','./realData/2020.10.xlsx','./realData/2020.11.xlsx','./realData/2020.12.xlsx']
writeExcel=['./realData/2020.6date.xlsx','./realData/2020.7date.xlsx','./realData/2020.8date.xlsx','./realData/2020.9date.xlsx','./realData/2020.10date.xlsx','./realData/2020.11date.xlsx','./realData/2020.12date.xlsx']
for i in range(0,7):
    xlsx_file = pd.read_excel(readExcel[i], sheet_name=None)
    output_file = writeExcel[i]
    writer = pd.ExcelWriter(output_file, engine='openpyxl')
    for sheet_name, df in xlsx_file.items():
        df['日期'] = sheet_name
        df['日期'] = pd.to_datetime(df['日期'], format='%m.%d')
        df['日期'] = df['日期'].dt.strftime('%-m/%-d')
        df.to_excel(writer, sheet_name=sheet_name, index=False)
    writer._save()
# xlsx_file = pd.read_excel('./realData/2020.6.xlsx', sheet_name=None)
# output_file = './realData/2020.6date.xlsx'
# xlsx_file7 = pd.read_excel('./realData/2020.7.xlsx', sheet_name=None)
# output_file7 = './realData/2020.7date.xlsx'
# xlsx_file8 = pd.read_excel('./realData/2020.8.xlsx', sheet_name=None)
# output_file8 = './realData/2020.8date.xlsx'
# xlsx_file9 = pd.read_excel('./realData/2020.9.xlsx', sheet_name=None)
# output_file9 = './realData/2020.9date.xlsx'
# xlsx_file10 = pd.read_excel('./realData/2020.10.xlsx', sheet_name=None)
# output_file10 = './realData/2020.10date.xlsx'
# xlsx_file11 = pd.read_excel('./realData/2020.11.xlsx', sheet_name=None)
# output_file11 = './realData/2020.11date.xlsx'
# xlsx_file12 = pd.read_excel('./realData/2020.12.xlsx', sheet_name=None)
# output_file12 = './realData/2020.12date.xlsx'



# writer = pd.ExcelWriter(output_file, engine='openpyxl')
# writer7 = pd.ExcelWriter(output_file7, engine='openpyxl')
# writer8 = pd.ExcelWriter(output_file8, engine='openpyxl')
# writer9 = pd.ExcelWriter(output_file9, engine='openpyxl')
# writer10 = pd.ExcelWriter(output_file10, engine='openpyxl')
# writer11 = pd.ExcelWriter(output_file11, engine='openpyxl')
# writer12 = pd.ExcelWriter(output_file12, engine='openpyxl')

# for sheet_name, df in xlsx_file.items():
#     df['日期'] = sheet_name
#     df['日期'] = pd.to_datetime(df['日期'], format='%m.%d')
#     df['日期'] = df['日期'].dt.strftime('%-m/%-d')
#     df.to_excel(writer, sheet_name=sheet_name, index=False)

# writer._save()
# writer7._save()
# writer8._save()
# writer9._save()
# writer10._save()
# writer11._save()
# writer12._save()



