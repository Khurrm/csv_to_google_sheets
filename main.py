import pandas as pd
import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials

if __name__ == "__main__":
 #with open("test.csv", 'r+', newline="") as f:```
    df = pd.read_csv("test.csv")
    print(df)