'''
Author: callus
Date: 2023-07-26 17:51:19
LastEditors: callus
Description: some description
FilePath: /drug-shortage-forecast/realDataDateAll.py
'''
# import pandas as pd

# xlsx_file = pd.read_excel('./realData/2020.6date.xlsx', sheet_name=None)
# output_file = './realData/2020.6dateAll.xlsx'
# output_dataframe = pd.DataFrame()

# # for sheet_name, df in xlsx_file.items():
# #     columns = df.columns
# #     for column in columns:
# #         if column not in output_dataframe.columns:
# #             output_dataframe[column] = df[column]
# #         else:
# #             # 这种写法是把sheet页的名称加到列名后面
# #             # new_column_name = f'{column}_{sheet_name}'
# #             # output_dataframe[new_column_name] = df[column]
# #             # 这种写法是把sheet页的名称加到列名前面
# #             # output_dataframe[column] = output_dataframe[column].astype(str) + '\n' + df[column].astype(str)
# #            output_dataframe=output_dataframe._append(df[column])

# # 读取每个sheet的数据,将每个sheet的数据写入汇总sheet,按照sheet的顺序写入，在汇总sheet中sheet的顺序也是按照sheet的顺序，新写入的sheet数据在下一行

# writer = pd.ExcelWriter(output_file, engine='openpyxl')
# output_dataframe.to_excel(writer, sheet_name='Result', index=True)
# writer._save()




import pandas as pd
from openpyxl import load_workbook
readExcel=['./realData/2020.6date.xlsx','./realData/2020.7date.xlsx','./realData/2020.8date.xlsx','./realData/2020.9date.xlsx','./realData/2020.10date.xlsx','./realData/2020.11date.xlsx','./realData/2020.12date.xlsx']
writeExcel=['./realData/2020.6dateAll.xlsx','./realData/2020.7dateAll.xlsx','./realData/2020.8dateAll.xlsx','./realData/2020.9dateAll.xlsx','./realData/2020.10dateAll.xlsx','./realData/2020.11dateAll.xlsx','./realData/2020.12dateAll.xlsx']
for i in range(0,7):
    xlsx_file = pd.read_excel(readExcel[i], sheet_name=None)
    output_file = writeExcel[i]
    output_dataframe = pd.DataFrame()
    for sheet_name, df in xlsx_file.items():
        output_dataframe = output_dataframe._append(df, ignore_index=True)
       
    writer = pd.ExcelWriter(output_file, engine='openpyxl')
    output_dataframe.to_excel(writer, sheet_name='Result', index=True)
    writer._save()

# xlsx_file = pd.read_excel('./realData/2020.6date.xlsx', sheet_name=None)
# merged_data = pd.DataFrame()
# xlsx_file7 = pd.read_excel('./realData/2020.7date.xlsx', sheet_name=None)
# merged_data7 = pd.DataFrame()
# xlsx_file8 = pd.read_excel('./realData/2020.8date.xlsx', sheet_name=None)
# merged_data8 = pd.DataFrame()
# xlsx_file9 = pd.read_excel('./realData/2020.9date.xlsx', sheet_name=None)
# merged_data9 = pd.DataFrame()
# xlsx_file10 = pd.read_excel('./realData/2020.10date.xlsx', sheet_name=None)
# merged_data10 = pd.DataFrame()
# xlsx_file11 = pd.read_excel('./realData/2020.11date.xlsx', sheet_name=None)
# merged_data11 = pd.DataFrame()
# xlsx_file12 = pd.read_excel('./realData/2020.12date.xlsx', sheet_name=None)
# merged_data12 = pd.DataFrame()

# for sheet_name, df in xlsx_file.items():
#     merged_data = merged_data._append(df, ignore_index=True)

# output_file = './realData/2020.6dateAll.xlsx'
# merged_data.to_excel(output_file, index=False)
# output_file7 = './realData/2020.7dateAll.xlsx'
# merged_data7.to_excel(output_file7, index=False)
# output_file8 = './realData/2020.8dateAll.xlsx'
# merged_data8.to_excel(output_file8, index=False)
# output_file9 = './realData/2020.9dateAll.xlsx'
# merged_data9.to_excel(output_file9, index=False)
# output_file10 = './realData/2020.10dateAll.xlsx'
# merged_data10.to_excel(output_file10, index=False)
# output_file11 = './realData/2020.11dateAll.xlsx'
# merged_data11.to_excel(output_file11, index=False)
# output_file12 = './realData/2020.12dateAll.xlsx'
# merged_data12.to_excel(output_file12, index=False)





