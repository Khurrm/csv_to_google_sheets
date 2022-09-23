import pandas as pd
import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials

if __name__ == "__main__":
 #with open("test.csv", 'r+', newline="") as f:```
    df = pd.read_csv("test.csv")
    print(df)
    credentials_google_sheet = ServiceAccountCredentials.from_json_keyfile_name('Sheets.json', SCOPES_Google_Sheet)
    client_google_sheet = gspread.authorize(credentials_google_sheet)
    credentials_google_sheet = ServiceAccountCredentials.from_json_keyfile_name('Sheets.json', SCOPES_Google_Sheet)
    client_google_sheet = gspread.authorize(credentials_google_sheet)
    
    spreadsheet_key = 'XXXXXXXXXXXXX' #spreadsheet_key is obfuscated. Kindly use your own key here. 
    worksheet_name = 'XXXX' #worksheet_name is obfuscated Kindly use your own name here. 
    """df is the name of data frame. 
        worksheet_name is the name of the sheet. 
        Credentials are json data derived from https://console.developers.google.com/.""" 
    d2g.upload(df, spreadsheet_key, worksheet_name, credentials=credentials_google_sheet, row_names=False)

