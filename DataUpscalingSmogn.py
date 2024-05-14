import smogn
import pandas as pd

# Read the initial data from the CSV file
initial_data = pd.read_csv('surgery_data.csv')

# Check the distribution of the target variable 'AHI_after_surgery'
print(initial_data['AHI_after_surgery'])

# Set the parameters for the smoter function
k = 36
rel_thres = 0.80
rel_method = 'auto'
rel_xtrm_type = 'high'
rel_coef = 2.25

# Perform synthetic oversampling
ahi_smogn = smogn.smoter(
    data=initial_data,
    y='AHI_after_surgery',
    k=k,
    samp_method='extreme',
    rel_thres=rel_thres,
    rel_method=rel_method,
    rel_xtrm_type=rel_xtrm_type,
    rel_coef=rel_coef
)

# Print the number of records after upscaling
print("Number of records after upscaling:", len(ahi_smogn))

# Save the upscaled data to a new CSV file
ahi_smogn.to_csv('upscaled_data1.csv', index=False)
