# fraud_detection_prediction
A machine learning project for fraud detection in financial transactions using Python and Streamlit.

# 🚀 Fraud Detection System

A **Machine Learning based Fraud Detection System** that predicts whether a financial transaction is **Fraud** or **Not Fraud**.  
This project is implemented using **Python, Scikit-learn, Pandas, NumPy, and Streamlit** for a user-friendly web interface.  

---

## 📖 Overview
Fraudulent financial transactions are a major challenge in the banking sector.  
This project builds a **classification model** that detects fraudulent transactions based on transaction details like amount, balance, and type.  
Finally, a **Streamlit app** is developed to allow real-time prediction.

---

## ⚙️ Features
- 🧠 Machine Learning pipeline with preprocessing and Logistic Regression.
- 📊 Handles categorical & numerical transaction features.  
- 🌐 Interactive **Streamlit Web App** for easy usage.  
- ✅ Predicts transactions as **Fraud** or **Not Fraud** instantly.  
- 🔍 Demo inputs for testing the model.  

---

## 📂 Project Structure

Navigate into the project:

cd fraud-detection


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run fraud_detection.py

🧪 Demo Inputs
✅ Not Fraud Example

Transaction Type: Payment

Amount: 2000

Old Balance (Sender): 5000

New Balance (Sender): 3000

Old Balance (Receiver): 1000

New Balance (Receiver): 3000

🚨 Fraud Example

Transaction Type: Transfer

Amount: 8000

Old Balance (Sender): 5000

New Balance (Sender): 0

Old Balance (Receiver): 2000

New Balance (Receiver): 2000

📊 Model Performance

Accuracy: ~95% (depends on dataset split)

Evaluation Metrics: Precision, Recall, F1-score, Confusion Matrix

🌍 Social Impact

Helps financial institutions detect fraud.

Saves customers from monetary loss.

Contributes to safer and trustworthy digital transactions.

👨‍💻 Technologies Used

Python 🐍

Pandas, NumPy

Scikit-learn

Streamlit

Matplotlib, Seaborn

📜 License

This project is licensed under the MIT License – feel free to use and modify.

✨ Author

Rahan Shihab
Fresher Frontend Developer & Machine Learning Enthusiast

