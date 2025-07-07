import pandas as pd
from datetime import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Load data
df = pd.read_csv("online_retail_II.csv", encoding='ISO-8859-1')  # change filename if needed

# Remove missing Customer IDs
df.dropna(subset=["Customer ID"], inplace=True)

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["Price"]

# Reference date for recency calculation
NOW = df["InvoiceDate"].max() + pd.Timedelta(days=1)

# Group by customer for RFM
rfm = df.groupby("Customer ID").agg({
    "InvoiceDate": lambda x: (NOW - x.max()).days,  # Recency
    "Invoice": "nunique",                           # Frequency
    "TotalPrice": "sum"                             # Monetary
}).reset_index()

rfm.columns = ["CustomerID", "Recency", "Frequency", "Monetary"]

# Create target label: Purchase = 1 if Frequency >= 5 else 0 (you can adjust this rule)
rfm["Purchase"] = (rfm["Frequency"] >= 5).astype(int)

# Features and label
X = rfm[["Recency", "Frequency", "Monetary"]]
y = rfm["Purchase"]

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Model training
model = LogisticRegression()
model.fit(X_scaled, y)

# Create model folder if not exists
os.makedirs("model", exist_ok=True)

# Save model and scaler
joblib.dump(model, "model/purchase_predictor.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("✅ Model and scaler saved successfully!")
