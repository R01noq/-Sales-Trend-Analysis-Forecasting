import pandas as pd
import matplotlib.pyplot as plt
from openpyxl.drawing.image import Image
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook

# read csv data
dt = pd.read_csv("D:/my python/Project/sale_data.csv")

# Handling missing values and converting numeric columns
cols = ["Price", "Quantity", "Profit_Percentage"]
for col in cols:
    dt[col] = pd.to_numeric(dt[col], errors="coerce")

# Revenue Account and Date Conversion
dt["Revenue"] = dt["Price"] * dt["Quantity"]
dt["Date"] = pd.to_datetime(dt["Date"])

# Revenue collection by date
dt = dt.groupby("Date")["Revenue"].sum().reset_index()

# Calculate the 3 and 7-day moving average without additional groupby
dt["MA_3"] = dt["Revenue"].rolling(window=3, min_periods=1).mean().round(2)
dt["MA_7"] = dt["Revenue"].rolling(window=7, min_periods=1).mean().round(2)

# Predict next week using MA_3
next_week = dt["Date"].max() + pd.Timedelta(weeks=1)
next_ma = dt["MA_3"].iloc[-1]

# Data plot drawing

plt.figure(figsize=(12, 6))
plt.plot(dt["Date"], dt["Revenue"], label="Actual Revenue", marker="o", color="green")
plt.plot(dt["Date"], dt["MA_3"], label="MA_3", linestyle="--", marker="o", color="red")
plt.plot(dt["Date"], dt["MA_7"], label="MA_7", linestyle="--", marker="x", color="blue")

# Draw forecast
plt.scatter(next_week, next_ma, color="purple", label="Next Week Forecast")
plt.text(next_week, next_ma, f"{next_ma:.2f}", ha="left", fontsize=10)

plt.title("Revenue Trend with 3 & 7-Day Moving Averages")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Revenue_Forecast.png", dpi=300)
plt.show()

# Export results to Excel
wb = Workbook()
ws1 = wb.active
ws1.title = "Sales Analysis"
for r in dataframe_to_rows(dt[["Date", "Revenue", "MA_3", "MA_7"]], index=False, header=True):
    ws1.append(r)

ws2 = wb.create_sheet("Chart")
img = Image("Revenue_Forecast.png")
ws2.add_image(img, "A1")

wb.save("Revenue_Trend_Analysis.xlsx")
