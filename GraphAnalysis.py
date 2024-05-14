import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Load data from CSV file into a DataFrame
df = pd.read_csv('All_patients.csv')  # Replace 'resampled_data.csv' with your actual file path

# Filter data where hypertension is equal to 0
# df_filtered = df.loc[(df['hypertension'] == 1) & (df['cardiac_surgery'] == 1), :]

x = df['avg_HR(rem)_s1'].values.reshape(-1, 1)
y = df['AHI_s1'].values

# Polynomial regression
poly_features = PolynomialFeatures(degree=3)  # You can change the degree as needed
x_poly = poly_features.fit_transform(x)
model = LinearRegression()
model.fit(x_poly, y)

# Predictions
x_range = np.linspace(min(x), max(x), 100).reshape(-1, 1)
x_range_poly = poly_features.transform(x_range)
y_pred = model.predict(x_range_poly)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x_range, y_pred, color='red', label='Curve fit')
plt.title('Heart Rate(REM) vs AHI')
plt.xlabel('avg_HR(rem)_s1')
plt.ylabel('AHI_s1')
plt.legend()
plt.grid()
plt.show()


# Calculate correlation coefficient
correlation_coefficient = df_filtered['AHI_after_surgery'].corr(df_filtered['Avg_length_of_cycle (In Sec)'])
plt.text(2.2, 30, f"Correlation coefficient: {correlation_coefficient:.2f}", fontsize=12, ha='right')

correlation_coefficient = df['avg_HR(rem)_s1'].corr(df['AHI_s1'])

print("Correlation coefficient:", correlation_coefficient)

plt.show()
