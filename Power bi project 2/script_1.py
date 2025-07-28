import pandas as pd
df = pd.read_csv('healthcare_data.csv')
subset = df.sample(50, random_state=42)
subset.to_csv('sample_data.csv', index=False)
print('sample_data.csv created with 50 records')