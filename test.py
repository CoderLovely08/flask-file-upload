import pandas as pd
from xlrd import open_workbook
# data=pd.read_excel('input.xlsx')

# rows=int(data.shape[0])
# cols=int(data.shape[1])
# print(rows,cols)
myfile=open('input.xlsx')
open_workbook(myfile)