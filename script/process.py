
import pandas as pd

# Load CSV file
data = pd.read_csv('../data/rawdata/data.csv')

# Clean column names
data.columns = data.columns.str.strip()

# Filter TP53
tp53 = data[data['Hugo_Symbol'] == 'TP53']
print(data.columns)

# Save processed data
tp53.to_csv('../data/processed/tp53_data.csv', index=False)

print("TP53 rows:", len(tp53))
