# import pandas as pd
#
# df = pd.read_csv("data/raw/nav_history.csv")
#
# df['date'] = pd.to_datetime(df['date'])
#
# df = df.sort_values(['amfi_code','date'])
#
# df = df.drop_duplicates()
#
# df = df[df['nav'] > 0]
#
# df.to_csv("data/processed/nav_history_clean.csv",index=False)

import os

print(os.listdir("data/raw"))