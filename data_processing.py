import pandas as pd
import csv

df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

df = pd.concat([df1, df2, df3])
df = df[df["product"] == "pink morsel"]
df["price"] = df["price"].replace("[$]","", regex=True).astype(float)
df["quantity"] = df["quantity"].astype(float)
df["Sales"] = df["quantity"]*df["price"]
df = df[["Sales", "date", "region"]]
df.columns = ["Sales", "Date", "Region"]
df.to_csv("formated_sales_data.csv", index=False)