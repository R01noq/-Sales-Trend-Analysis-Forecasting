import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("D:\my python\Project\weekly_branch_product_sales.csv")
missing_rateo = df.isnull().mean()*100
print(missing_rateo)
df_clean = df.copy()
cols = ["Unit_Price", "Cost_per_Unit", "Profit_Percentage"]
for col in cols:
    df_clean[col] = pd.to_numeric(df[col], errors="coerce").round(2)
    df_clean[col] = df_clean.groupby("Product")[col].transform(lambda x: x.fillna(x.mean()))


df_clean["Profit"] = (df_clean["Unit_Price"]*df_clean["Quantity"]*df_clean["Profit_Percentage"]/100).round(2)
daily_summary = df_clean.groupby(["Date", "Branch", "Category"])["Profit"].mean().reset_index().round(2)
daily_summary.rename(columns={"Profit" : "Average_Profit"},inplace=True)
daily_std = daily_summary.groupby(["Branch", "Category"])["Average_Profit"].std().reset_index().round(2)
daily_std.columns = ["Branch", "Category", "Average_Profit_std"]
most_stable = daily_std.sort_values("Average_Profit_std").head(3)
print(most_stable)
all_compinations = pd.MultiIndex.from_product([
    daily_summary["Date"].unique(),
    daily_summary["Branch"].unique(),
    daily_summary["Category"].unique()
], names = ["Date", "Branch", "Category"]).to_frame(index=False)

full_profit = all_compinations.merge(daily_summary, on=["Date", "Branch", "Category"], how="left")
full_profit["Average_Profit"] = full_profit["Average_Profit"].fillna(0)
print(full_profit)
pivot = full_profit.pivot_table(index="Date", columns=["Branch", "Category"], values="Average_Profit")
print(pivot)

plt.figure(figsize=(12,6))
for col in pivot.columns:
    plt.plot(pivot.index, pivot[col], marker="^" , label=f"{col[0]} - {col[1]}")
plt.title("the average of profit for each branch,category per day")
plt.xlabel("Date")
plt.ylabel("Average profit")
plt.xticks(rotation=45)
plt.legend(title="Branch - Category", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.heatmap(pivot.T, cmap="YlGnBu", linewidths=0.5, linecolor='grey')
plt.title("🔥 Heatmap - Daily Avg Profit by Branch and Category")
plt.xlabel("Date")
plt.ylabel("Branch - Category")
plt.tight_layout()
plt.savefig("heatmap_profit.png", dpi=300, bbox_inches="tight")
plt.show()





