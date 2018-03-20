import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('clientsecret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("MAR").sheet1

# Extract and print all of the values

sheet.update_cell(2, 1, "sahith")
sheet.update_cell(3,1,"yash")
sheet.update_cell(3,2,30)
sheet.update_cell(3,3,1)
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)

def getCellValue(row, col):
    return

def setCellValue(row,col,value):
    print()

def setRowValue(row, values):
    print()
