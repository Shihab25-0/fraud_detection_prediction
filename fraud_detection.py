import streamlit as st
import pandas as pd
import joblib

# Load pre-trained ML model
model = joblib.load("fraud_detection_pipeline_updated.pkl")

#  App title and description
st.title("Fraud Detection Prediction App")
st.markdown("Enter transaction details below and check if it is likely to be a fraud.")

st.divider()

#  User Input Fields
transaction_type = st.selectbox(
    "Transaction Type", 
    ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"]
)
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

#  Predict button
if st.button("Predict"):
    # Calculate balance differences
    balanceDiffOrig = oldbalanceOrg - newbalanceOrig
    balanceDiffDest = newbalanceDest - oldbalanceDest

    # Prepare input data for model
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
        "balanceDiffOrig": balanceDiffOrig,
        "balanceDiffDest": balanceDiffDest
    }])

    # Make prediction and get probability
    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0][1]  # probability of fraud class

    # Display prediction
    st.subheader(f"Prediction: {int(prediction)}")
    if prediction == 1:
        st.error("⚠️ This transaction can be FRAUD")
    else:
        st.success("✅ This transaction looks NOT FRAUD")

    # Display probability as color-coded bar
    st.markdown("### Fraud Probability")
    st.progress(float(prediction_proba))  # shows as a progress bar
    st.write(f"Fraud Likelihood: {prediction_proba*100:.2f}%")
