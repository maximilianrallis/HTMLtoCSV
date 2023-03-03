import os
from bs4 import BeautifulSoup
import re
import webbrowser

# Replace 'path/to/folder' with the path to your folder
folder_path = r"C:\Users\WF6444\HTML_MSCons"
countNumber = 0
countFile = 0
numbers = []
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

        pattern = r"[a-zA-Z0-9]{3}_\d{13}"  # example pattern to search for
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

print(countNumber)
print(numbers)
