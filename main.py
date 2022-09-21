import pandas as pd
import csv

if __name__ == "__main__":
 #with open("test.csv", 'r+', newline="") as f:```
    df = pd.read_csv("test.csv")
    print(df)