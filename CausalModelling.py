import pandas as pd
import dowhy
from dowhy import CausalModel

# Load health data
data = pd.read_csv('cleaned_data.csv')  # Replace 'health_data.csv' with your data file path

# Define causal model
model = CausalModel(
    data=data,
    treatment='Hypertension',  # Apnea-Hypopnea Index
    outcome='BP',   # Oxygen Saturation
    # graph="causal_graph.dot",
    common_causes=['age_at_s1', 'gender', 'bmi_s1', 'smoking_status_s1']  # Potential confounders
)

# Plot causal graph
model.view_model()

# Identify causal effect
identified_estimand = model.identify_effect()

# Estimate causal effect
estimate = model.estimate_effect(identified_estimand,
                                  method_name="backdoor.linear_regression")

# Print causal effect
print(estimate)