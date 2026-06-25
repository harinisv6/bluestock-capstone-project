import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Sort
df = df.sort_values(['amfi_code', 'date'])

# Remove duplicates
df = df.drop_duplicates()

# Keep valid NAV values
df = df[df['nav'] > 0]

# Forward fill NAV
df['nav'] = df.groupby('amfi_code')['nav'].ffill()

# Save
df.to_csv("data/processed/nav_history_clean.csv", index=False)

print(df.shape)
print("NAV History cleaned successfully")