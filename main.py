import pandas as pd
import requests

# Adding this line to disable checking copy in the dataframe. So it doesn't push warning.
pd.set_option('mode.chained_assignment', None)
# Reading the CSV file
data = pd.read_csv(r'status.csv')   
# Selecting Specific Column of the CSV file
#df = pd.DataFrame(data, columns=['brand','price'])
# Displaying the selected specific column
#print(df)
# print(df.describe())
# Single cell value selection in a variable
r=data['URL'][1]
print(r)
print("Total number of rows :", len(data.axes[0]))

# For loop for the operations
for i in range(len(data.axes[0])):
    # Printing all the values in the row of URLs
    print (data['URL'][i])
    s=data['URL'][i]
    # Checking the status code 
    r = requests.get(s, allow_redirects=False)
    print (r.status_code) 
    # Copying the status code to the rows
    data['Status'][i] = int(r.status_code)
# This will convert status column from floating to int
data.Status = data.Status.astype(int)
# Print on console
print(data)
# Write to the CSV File
data.to_csv('status-1.csv', index = False)