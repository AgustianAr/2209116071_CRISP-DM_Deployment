# statistics_website.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from the provided URL
url = "https://raw.githubusercontent.com/AgustianAr/Cities-Sunshine-Hours/main/Data%20Cleaned.csv"
df = pd.read_csv(url)

# Exclude columns for country, city, and year
excl_columns = ["Country", "City", "Year"]
months_columns = [col for col in df.columns if col not in excl_columns]

# Calculate mean duration per month
mean_per_month = df[months_columns].mean()

# Set title of the web app
st.title('Worldwide Monthly Average Sunshine Hours Dashboard')

# Display the mean duration per month as a bar chart
plt.figure(figsize=(10, 6))
plt.bar(mean_per_month.index, mean_per_month.values, color='skyblue')

for i, v in enumerate(mean_per_month.values):
    plt.text(i, v + 0.1, f"{v:.2f}", ha='center', va='bottom', fontsize=10)

plt.xlabel("Month")
plt.ylabel("Average Sunshine Hours")
plt.title("Worldwide Monthly Average Sunshine Hours")
if len(mean_per_month) > 10:
    plt.xticks(rotation=45)

# Show the plot
plt.grid(True)
st.pyplot(plt)

# Additional visualizations (you can add more as needed)
st.subheader('Sunshine Hours Distribution Across Cities')
st.write(df[months_columns].describe())

st.subheader('Sunshine Hours Distribution Across Cities')
st.write(df[months_columns].describe())

# Scatter plot for latitude and longitude
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='Latitude', y='Longitude', data=df)
plt.title('Latitude and Longitude Distribution')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
st.pyplot(fig)
