# 📊 Monthly Product Performance Analysis

This project analyzes monthly product performance using a commercial dataset. The goal is to identify missing values, compute average profits, and detect the most stable products in terms of profit across months.

## 🔍 Project Description

The project performs the following key tasks:

- Loads and cleans the dataset.
- Detects missing values in numerical columns (`Revenue`, `Cost`, `Profit`, `Margin(%)`).
- Calculates average monthly profit per product.
- Completes missing Month–Product combinations with zero profit where needed.
- Builds a pivot table to show monthly profit trends for each product.
- Identifies the top 3 most **stable** products based on standard deviation of monthly profit.
- Visualizes the result using a **heatmap**.

## 📈 Resulting Visualization

Below is the heatmap showing the average monthly profit for each product:

![Monthly Product Profit Matrix](monthly_product_profit_matrix.png)

## 🗂️ Files

- `monthly_product_performance.csv` – Input dataset
- `analysis_script.py` – Python script containing the full analysis
- `monthly_product_profit_matrix.png` – Output heatmap visualization

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


