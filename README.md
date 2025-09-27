# 🚨 Fraud Detection Prediction

A machine learning project that predicts whether a financial transaction is **Fraud** or **Not Fraud**, implemented using **Python, Scikit-learn, Pandas, NumPy** and deployed as a **Streamlit web app**.

---

## 📂 Project Structure

fraud_detection_prediction/
├── fraud_detection_pipeline_updated.pkl
├── fraud_detection.py
├── analysis_model.ipynb
├── data.txt
├── README.md
└── requirements.txt

yaml
Copy code

- `fraud_detection_pipeline_updated.pkl`: Trained ML pipeline  
- `fraud_detection.py`: Streamlit app code  
- `analysis_model.ipynb`: Notebook with EDA, model training, experiments  
- `data.txt`: Dataset info or small sample (if included)  
- `requirements.txt`: Python dependencies  
- `README.md`: Project documentation  

---

## 🧠 Project Description

This project tackles the problem of **fraud detection in financial transactions**.  
Given transaction details like type, amount, and balances, the model classifies a transaction as either **Fraud (1)** or **Not Fraud (0)**.  
A user-friendly Streamlit interface allows anyone to enter transaction details and get predictions in real time.

---

## 🚀 Features & Innovation

- End-to-end **ML pipeline**: preprocessing + classification  
- Uses **Logistic Regression** with class balancing  
- Handles numeric and categorical inputs  
- **Streamlit Web App** for interactive user predictions  
- Can be expanded in the future (other models, dashboards)  

---

## 📊 Model Performance & Metrics

Use the notebook `analysis_model.ipynb` to view detailed metrics:  
- Accuracy  
- Precision, Recall, F1-score  
- Confusion Matrix  

---

## 🎯 Demo Input Examples

### ✅ Not Fraud
**Type:** PAYMENT  
**Amount:** 2000  
**OldBalance Sender:** 5000  
**NewBalance Sender:** 3000  
**OldBalance Receiver:** 1000  
**NewBalance Receiver:** 3000  

### 🚨 Fraud
**Type:** TRANSFER  
**Amount:** 8000  
**OldBalance Sender:** 5000  
**NewBalance Sender:** 0  
**OldBalance Receiver:** 2000  
**NewBalance Receiver:** 2000  

Use these to test your inputs when running the app.

---

## 🛠 Installation & Usage

1. Clone repository  
   ```bash
   git clone https://github.com/Shihab25-0/fraud_detection_prediction.git
Change directory

bash
Copy code
cd fraud_detection_prediction
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app

bash
Copy code
streamlit run fraud_detection.py
📦 Dataset Info
The full dataset is too large to be uploaded directly on GitHub.
You can download the dataset from Kaggle:

👉 Fraud Detection Dataset on Kaggle

After downloading, place the dataset file inside the project folder before running the notebook or training the model.

🌍 Social Impact & Usefulness
Helps banks, fintechs, payment apps detect and prevent fraudulent transactions

Protects users from financial loss

Contributes to safer digital transactions in socio-economic context

🧩 Future Enhancements
Integrate other models (RandomForest, XGBoost, Neural Networks)

Add transaction history dashboard for bankers/admin

Deploy in cloud / production environment

Enhance with behavioral & temporal features

⚖️ License
This project is licensed under the MIT License. Feel free to use, modify, and distribute.

✍ Author
Shihab25-0
