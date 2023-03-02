import re
from bs4 import BeautifulSoup

# specify the pattern to search for
pattern = r"[a-zA-Z0-9]{3}_\d{13}"

# open the HTML file and parse it using BeautifulSoup
url = r"C:\Users\WF6444\HTML_MSCons\MSCONS_TL_9907388000002_9904771000003_20230217_121800870PF_X1276873888159.txt_imp.html"
with open(url) as f:
    soup = BeautifulSoup(f, "html.parser")

# find all rows in the HTML file and loop through them
for row in soup.find_all("tr"):
    # find all cells in the row
    cells = row.find_all("td")
    # loop through the cells and search for the pattern in the cell text
    for cell in cells:
        # use regex to find the pattern in the cell text
        match = re.search(pattern, cell.text)
        # if a match is found, print the matched number
        if match:
            print(match.group(0))


