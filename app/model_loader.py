# model_loader.py

import joblib
import os

def load_model():
    model = joblib.load(os.path.join("model", "purchase_predictor.pkl"))
    scaler = joblib.load(os.path.join("model", "scaler.pkl"))
    return model, scaler
