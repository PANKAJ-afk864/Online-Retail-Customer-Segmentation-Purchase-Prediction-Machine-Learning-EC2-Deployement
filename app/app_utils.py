import numpy as np

def predict_purchase(model, scaler, recency, frequency, monetary):
    input_data = np.array([[recency, frequency, monetary]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]
    return prediction, probability
