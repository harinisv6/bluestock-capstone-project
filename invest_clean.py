import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Date format
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# Standardize transaction types
df['transaction_type'] = df['transaction_type'].str.strip().str.title()

# Amount validation
df = df[df['amount_inr'] > 0]

# Check KYC values
print("KYC Status Values:")
print(df['kyc_status'].unique())

# Save
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print(df.shape)
print("Transactions cleaned successfully")