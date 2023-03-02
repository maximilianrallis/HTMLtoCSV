# Open the HTML file for reading
filename = r"C:\Users\WF6444\HTML_MSCons\MSCONS_TL_9907388000002_9904771000003_20230217_121800870PF_X1276873888159.txt_imp.html"
with open(filename , "r") as file:
    # Read the contents of the file
    contents = file.read()

# Print the contents of the file
print(contents)
