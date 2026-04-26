import pandas as pd
import matplotlib.pyplot as plt
import os

# Create results folders
os.makedirs('../results/figures', exist_ok=True)

# Load processed data
data = pd.read_csv('../data/processed/tp53_data.csv')

# Load full dataset
raw = pd.read_csv('../data/rawdata/data.csv')

# Calculate mutation frequency
freq = (len(data) / len(raw)) * 100

# Mutation type distribution
counts = data['Variant_Classification'].value_counts()

# Save results to file
with open('../results/results.txt', 'w') as f:
    f.write(f"TP53 Mutation Frequency: {freq:.2f}%\n\n")
    f.write("Mutation Type Distribution:\n")
    f.write(counts.to_string())

print("Results file created")

# Plot
counts.plot(kind='bar')
plt.title("TP53 Mutation Types")
plt.xlabel("Mutation Type")
plt.ylabel("Count")

# Save plot
plt.savefig('../results/figures/mutation_plot.png')

print("Plot saved")
