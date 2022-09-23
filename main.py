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
