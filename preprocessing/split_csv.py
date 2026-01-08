import pandas as pd
import os

# -----------------------------
# 1. Load raw dataset
# -----------------------------
input_file = "WA_Fn-UseC_-Telco-Customer-Churn.csv"
df = pd.read_csv(input_file)

# -----------------------------
# 2. Create output directories
# -----------------------------
base_path = "project-data/raw"

folders = {
    "customers": ["customerID", "gender", "SeniorCitizen", "Partner", "Dependents"],
    
    "subscriptions": [
        "customerID", "tenure", "Contract", "InternetService", "PhoneService",
        "MultipleLines", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
        "TechSupport", "StreamingTV", "StreamingMovies"
    ],
    
    "billing": [
        "customerID", "PaymentMethod", "PaperlessBilling",
        "MonthlyCharges", "TotalCharges"
    ],
    
    "labels": ["customerID", "Churn"]
}

for folder in folders.keys():
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

# -----------------------------
# 3. Split and save raw tables
# -----------------------------
for folder, columns in folders.items():
    output_path = os.path.join(base_path, folder, f"{folder}.csv")
    df[columns].to_csv(output_path, index=False)
    print(f"Saved: {output_path}")

print("\n✅ Raw data successfully split into production-style tables.")
