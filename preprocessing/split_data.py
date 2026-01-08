df = df.sort_values("tenure")

train = df.iloc[:int(0.7*len(df))]
val   = df.iloc[int(0.7*len(df)):int(0.85*len(df))]
test  = df.iloc[int(0.85*len(df)):]
