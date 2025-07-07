import streamlit as st

# ⛳️ MUST be the first Streamlit command
st.set_page_config(page_title="Customer Purchase Predictor", layout="centered")

from model_loader import load_model
from app_utils import predict_purchase  

st.title("🛍️ Online Retail – Purchase Likelihood Predictor")
st.write("If you're seeing this, you’ve set up everything correctly.")

# Load model
model, scaler = load_model()

# Input form
st.subheader("📥 Enter Customer RFM Data")
recency = st.number_input("Recency (days since last purchase)", min_value=0)
frequency = st.number_input("Frequency (number of purchases)", min_value=0)
monetary = st.number_input("Monetary Value (total spent)", min_value=0.0, step=10.0)

if st.button("Predict"):
    pred, prob = predict_purchase(model, scaler, recency, frequency, monetary)
    if pred == 1:
        st.success(f"✅ Likely to Purchase (Confidence: {prob:.2%})")
    else:
        st.error(f"❌ Unlikely to Purchase (Confidence: {prob:.2%})")

# Optional: Add cluster segment table/visualizations
st.markdown("---")
st.markdown("👥 Want to see customer segments or dashboard? Add that in next version.")
