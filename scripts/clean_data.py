import pandas as pd

# Load original data
df = pd.read_csv('data/insurance_data.csv')

print(f"Original shape: {df.shape}")

# Basic cleaning
df_clean = df.dropna(subset=['TotalPremium', 'TotalClaims'])
df_clean = df_clean[df_clean['TotalPremium'] > 0]

# Add derived columns
df_clean['LossRatio'] = df_clean['TotalClaims'] / df_clean['TotalPremium']
df_clean['Margin'] = df_clean['TotalPremium'] - df_clean['TotalClaims']

# Remove extreme outliers (top 1% of claims)
cap = df_clean['TotalClaims'].quantile(0.99)
df_clean = df_clean[df_clean['TotalClaims'] <= cap]

print(f"Cleaned shape: {df_clean.shape}")
print(f"Rows removed: {len(df) - len(df_clean)}")

# Save cleaned data
df_clean.to_csv('data/insurance_data_clean.csv', index=False)
print("Saved: data/insurance_data_clean.csv")
