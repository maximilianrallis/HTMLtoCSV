from bs4 import BeautifulSoup
import re

url = r"C:\Users\WF6444\HTML_MSCons\MSCONS_TL_9907388000002_9904771000003_20230217_121800870PF_X1276873888159.txt_imp.html"
with open(url, "r") as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')

# Split the HTML into rows using the <br> tag
rows = html.split('<br>')

pattern = r"[a-zA-Z0-9]{3}_\d{13}" # example pattern to search for
amount = 0
for row in rows:
    # Search for the pattern in the row
    match = re.search(pattern, row)
    # If a match is found, print the number
    if match:
        number = match.group(0)
        print(number)
        amount +=1

print(amount)