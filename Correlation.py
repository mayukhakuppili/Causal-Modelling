import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Load data from CSV file into a DataFrame
df = pd.read_csv('All_patients.csv')  # Replace 'resampled_data.csv' with your actual file path

# Filter data where hypertension is equal to 0
# df_filtered = df.loc[(df['hypertension_s1'] == 1) & (df['cardiac_surgery_s1'] == 1), :]

df_filtered = df.loc[(df['gender'] == 2)]

plt.figure(figsize=(10, 6))
sns.barplot(data=df_filtered, x="hypertension_s1", y="sys_bp_s1", errorbar=None, saturation=0.75, capsize=0.1, width=0.3)
plt.title("Correlation between Hypertension and Diastolic BP")
plt.xlabel("hypertension_s1")
plt.ylabel("sys_bp_s1")
plt.grid(axis='y')

# Calculate correlation coefficient
correlation_coefficient = df_filtered['hypertension_s1'].corr(df['dia_bp_s1'])
plt.text(2.2, 20, f"Correlation coefficient: {correlation_coefficient:.2f}", fontsize=12, ha='right')