import pandas as pd

df = pd.read_csv(r"C:\Users\Inbox\Downloads\1232.csv")

# First 5 rows
print(df.head())

# Dataset information
print(df.info())

print(df.isnull().sum())

total_missing = df.isnull().sum().sum()
print("Total Missing Values:", total_missing)

df['Quantity'] = df['Quantity'].fillna(df['Quantity'].mean())
df['Price'] = df['Price'].fillna(df['Price'].mean())

df = df.dropna(subset=['Product Category', 'Region'])

import numpy as np

df['Revenue'] = np.multiply(df['Quantity'], df['Price'])

print(df.head())

total_revenue = np.sum(df['Revenue'])
print(total_revenue)

category_revenue = df.groupby('Product Category')['Revenue'].sum()
print(category_revenue)

category_revenue = category_revenue.sort_values(ascending=False)

top3 = category_revenue.head(3)
bottom3 = category_revenue.tail(3)

print(top3)
print(bottom3)

region_revenue = df.groupby('Region')['Revenue'].sum()
print(region_revenue)

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

df['Month'] = df['Date'].dt.month

monthly_revenue = df.groupby('Month')['Revenue'].sum()
print(monthly_revenue)

# Statistics
mean_rev = np.mean(df['Revenue'])
median_rev = np.median(df['Revenue'])
std_rev = np.std(df['Revenue'])

print("Mean:", mean_rev)
print("Median:", median_rev)
print("Standard Deviation:", std_rev)