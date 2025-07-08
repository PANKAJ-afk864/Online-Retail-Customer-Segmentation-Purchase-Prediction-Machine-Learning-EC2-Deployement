🛍️ Online Retail Customer Segmentation & Purchase Prediction

📌 Overview
This project solves a practical business problem for online retailers:
Which customers are most likely to purchase again?

Using historical transaction data, we perform:

Customer segmentation (Unsupervised Learning)

Purchase likelihood prediction (Supervised Learning)

Deployment via Streamlit on AWS EC2 with Docker

## Problem Statement
Retail businesses need to understand:

Which customers are valuable?

Who is likely to churn?

Who is ready to buy again?

This project builds a machine learning pipeline that:

Segments customers using RFM features

Predicts future purchases using classification models

Delivers real-time predictions in a web app

->Dataset
📦 Dataset: UCI Online Retail II Dataset

🧾 Rows: 500,000+ transaction records

🛍️ Features: InvoiceNo, CustomerID, Country, Date, ProductID, Quantity, UnitPrice

📍 Location: UK-based e-commerce store

🧪 Features Engineered
Recency: Days since last purchase

Frequency: Total number of purchases

Monetary: Total amount spent

These RFM features help us group customers and predict buying behavior.

🚀 Machine Learning Pipeline
1. Customer Segmentation
Clustering: KMeans

Scaled RFM data

Visualized clusters using Seaborn & Plotly

2. Purchase Prediction
Labels created based on recent purchase window

Models tried:

Logistic Regression

Random Forest

XGBoost (Best performance ✅)

Model evaluation:

Accuracy, ROC-AUC, Confusion Matrix

🖥️ Tech Stack
Tool	Use
Python	Core programming
Pandas, NumPy	Data cleaning
Scikit-learn, XGBoost	ML models
Streamlit	Web interface
Docker	Containerization
AWS EC2	Cloud deployment

🌐 Live Demo
👉 http://13.60.28.46:8501
-- Enter RFM values to predict customer purchase likelihood in real time.

🧰 Folder Structure
Copy
Edit
├── app/
│   ├── streamlit_app.py
│   ├── app_utils.py
│   └── model_loader.py
├── model/
│   ├── purchase_predictor.pkl
│   └── scaler.pkl
├── Dockerfile
├── requirements.txt
📦 Deployment
Built Docker image:

bash
Copy
Edit
docker build -t retail-app .
Deployed on AWS EC2:

bash
Copy
Edit
docker run -d -p 8501:8501 retail-app
Ports opened: 8501, 22, 80 (Security Group)

📚 Learnings
✅ Built a full ML pipeline from raw data to prediction
✅ Understood customer value using RFM
✅ Hands-on Docker + EC2 deployment
✅ Improved model explainability for business use

📌 Future Improvements
Add login-based dashboards for sales teams

Deploy using AWS ECS or Kubernetes

Automate with CI/CD pipeline

Add retention strategy recommendations using Lift analysis

🙋‍♂️ Author
Pankaj Kumar
Data & Business Analytics Enthusiast
🔗 www.linkedin.com/in/pankaj-kumar-singh-396162325
📫 pankajjsinghh376@gmail.com

