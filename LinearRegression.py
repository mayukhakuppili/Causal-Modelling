import statsmodels.api as sm
import pandas as pd
from sklearn.metrics import mean_squared_error

# Load data from CSV file into a DataFrame
df = pd.read_csv('cleaned_data.csv')  # Replace 'cleaned_data.csv' with your actual file path

# Define independent variables (X) and dependent variable (y)
X = df[['avg_HR(rem)_s1', 'sys_bp_s1', 'avg_HR(nrem)_s1', 'dia_bp_s1', 'bmi_s1','avg_sao2_s1', 'gender','smoking_status_s1','hypertension_s1']]
y = df['AHI_s1']

# Add constant term for the intercept
X = sm.add_constant(X)

# Fit the linear regression model
model = sm.OLS(y, X).fit()

# Calculate predicted values
y_pred = model.predict(X)

# Calculate mean squared error
mse = mean_squared_error(y, y_pred)
print("Mean Squared Error:", mse)

# Print the model summary
print(model.summary())