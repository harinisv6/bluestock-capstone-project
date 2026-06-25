from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///bluestock_mf.db")

pd.read_csv(
    "data/processed/nav_history_clean.csv"
).to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded Successfully")