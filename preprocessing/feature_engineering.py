subs = pd.read_csv("data/raw/subscriptions/subscriptions.csv")

subs["is_long_term_contract"] = subs["Contract"].isin(
    ["One year", "Two year"]
).astype(int)

service_cols = [
    "OnlineSecurity", "OnlineBackup",
    "DeviceProtection", "TechSupport",
    "StreamingTV", "StreamingMovies"
]

subs["num_services"] = subs[service_cols].apply(
    lambda x: (x == "Yes").sum(), axis=1
)

subs.to_csv("data/processed/subscriptions_features.csv", index=False)
