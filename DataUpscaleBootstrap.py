import pandas as pd
import numpy as np

# Read the original dataset
original_data = pd.read_csv('surgery_data_sao2.csv')

# Define the number of bootstrap samples you want to generate
num_bootstrap_samples = 10

# Initialize an empty list to store bootstrap samples
bootstrap_samples = []

# Perform bootstrap resampling
for _ in range(num_bootstrap_samples):
    # Generate a bootstrap sample by randomly sampling with replacement from the original dataset
    bootstrap_sample = original_data.sample(n=len(original_data), replace=True)

    # Append the bootstrap sample to the list
    bootstrap_samples.append(bootstrap_sample)

# Concatenate all bootstrap samples into a single DataFrame
upscaled_data = pd.concat(bootstrap_samples, ignore_index=True)

# Save the upscaled data to a new CSV file
upscaled_data.to_csv('upscaled_data23.csv', index=False)