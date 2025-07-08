#  Online Retail Customer Segmentation & Purchase Prediction

A real-world machine learning project to segment customers and predict their likelihood to purchase — deployed on AWS EC2 using Docker and Streamlit.

---

##  Problem Statement

Retail businesses often struggle to identify:
- Who are their most valuable customers?
- Which customers are likely to buy again?
- How can they prioritize marketing efforts?

This project uses RFM analysis, unsupervised learning (clustering) for customer segmentation, and supervised machine learning for purchase prediction — all wrapped into a live dashboard deployed on the cloud.
---

##  Dataset Overview

-  Source: [UCI Online Retail II Dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II)  
-  Rows: 500,000+ transaction records  
-  Region: UK-based e-commerce store  
-  Timeframe: 2009–2011

Each row includes:
- InvoiceNo
- CustomerID
- InvoiceDate
- Quantity
- UnitPrice
- Country

---

##  Features Engineered

RFM features per customer:
- `Recency`: Days since last purchase  
- `Frequency`: Number of purchases  
- `Monetary`: Total spend value

These features are the foundation for:
- Clustering customers
- Predicting future purchases

---

##  Machine Learning Tasks

### 1. **Customer Segmentation (Unsupervised)**
- Algorithm: `KMeans`
- Clusters visualized using Seaborn + Plotly
- Grouped customers by behavior

### 2. **Purchase Prediction (Supervised)**
- Label created using recent purchase windows
- Models compared:
  - Logistic Regression
  - Random Forest
  - XGBoost (Best ✅)
- Metrics:
  - Accuracy
  - ROC-AUC
  - Confusion Matrix

---

##  Tech Stack

| Tool | Role |
|------|------|
| Python | Core programming |
| Pandas, NumPy | Data preprocessing |
| Scikit-learn, XGBoost | Modeling |
| Matplotlib, Seaborn | Visualization |
| Streamlit | UI dashboard |
| Docker | Containerization |
| AWS EC2 | Cloud deployment |

---

##  Live Demo

🟢 [http://13.60.28.46:8501](http://13.60.28.46:8501)  
Use the form to enter RFM values and get instant predictions from the trained model.

---

##  Project Structure
├── app/
│ ├── streamlit_app.py # Streamlit UI logic
│ ├── app_utils.py # Prediction logic
│ └── model_loader.py # Model + scaler loading
├── model/
│ ├── purchase_predictor.pkl # Trained XGBoost model
│ └── scaler.pkl # Standard scaler
├── Dockerfile
├── requirements.txt
└── retail-app.zip # For deployment


🙋‍♂️ Author
Pankaj Kumar Singh
Data & Business Analytics Enthusiast
📫 pankajjsinghh376@gmail.com