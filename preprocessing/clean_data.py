import pandas as pd

billing = pd.read_csv("data/raw/billing/billing.csv")

billing["TotalCharges"] = pd.to_numeric(
    billing["TotalCharges"], errors="coerce"
)

billing["TotalCharges"].fillna(billing["TotalCharges"].median(), inplace=True)

billing.to_csv("data/processed/billing_cleaned.csv", index=False)
