import pandas as pd

df = pd.read_excel("excel_with_multiple_sheets-1.xlsx", sheet_name="marks")
print(df)

data = pd.ExcelFile("excel_with_multiple_sheets-1.xlsx")
print(data.sheet_names)

df = pd.read_excel("excel_with_multiple_sheets-1.xlsx",sheet_name=data.sheet_names[0])
print(df)

df = data.parse("height")
print(df.head())
print(df.tail())
print(df.columns)
print(df.columns.tolist())