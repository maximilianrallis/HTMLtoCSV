import pandas as pd

# Open the Excel workbook
ILN = 9901066000003

EIC =r"C:\Users\WF6444\EIC.xlsx"

# read the Excel file and select the specific table
excel_file = pd.read_excel(EIC)

# extract the character from the same row but 2 columns
match_char = ILN  # the character you want to match against
result_char = excel_file.loc[excel_file['ILN'] == match_char, 'EICAREANR'].iloc[0]

print(result_char)

