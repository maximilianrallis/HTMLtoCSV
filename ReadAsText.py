import os
from bs4 import BeautifulSoup
import re
import openpyxl
import pandas as pd
import webbrowser

# Replace 'path/to/folder' with the path to your folder
folder_path = r"C:\Users\WF6444\HTML_MSCons"
countNumber = 0
count_file_path = 0
numbers = []
file_paths = []
pattern = r"[a-zA-Z0-9]{3}_\d{13}"  # example pattern to search for
# Iterate through all files in the folder
for file_name in os.listdir(folder_path):
    # Check if file is an HTML file

    if file_name.endswith('.html'):
        # Create the full file path by joining the folder path and file name
        file_path = os.path.join(folder_path, file_name)

        # Open the HTML file in the default web browser
        with open(file_path, "r") as f:
            html = f.read()
        soup = BeautifulSoup(html, 'html.parser')

        # Split the HTML into rows using the <br> tag
        rows = html.split('<br>')


        amount = 0

        for row in rows:
            # Search for the pattern in the row
            match = re.search(pattern, row)
            # If a match is found, print the number
            if match:
                number = match.group(0)

                if number not in numbers:
                    # Add the number to the list
                    numbers.append(number)
                    countNumber += 1

                # if file_path not in file_paths:
                #     # Add the number to the list
                #     file_paths.append(file_path)
                #     count_file_path += 1



print(countNumber)
print(numbers)
print(count_file_path)
# print(file_paths)

# write excelfile

# create a new workbook and select the active worksheet

workbook = openpyxl.Workbook()
worksheet = workbook.active
ILN = int(number[-13:])
Instanz = [18] * countNumber
fuerInstanz = [6] * countNumber
Zielzeitreihe = ['Normallastprofil.Markt'] * countNumber
# Define the table as a pandas DataFrame object
table_data = {'Instanz': Instanz,
              'fuer_Instanz': fuerInstanz,
              'Zielinstanz': numbers,
              'Zielzeitreihe': Zielzeitreihe,
              'virtuelle_Zaehlpunktbezeichnung': numbers}

# create a pandas DataFrame from the list
df = pd.DataFrame(table_data)
Spath = r"C:\Users\WF6444\ExportCSVFiles\HierCSV" + ILN + '.xlsx'
# create a writer object to save the file
writer = pd.ExcelWriter(Spath)

# write the DataFrame to the Excel file
df.to_excel(writer, index=False)

# save the file
writer.close()