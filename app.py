# app.py
import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("SalaryPrediction.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("💼 Salary Prediction App")
st.write("Enter your years of experience to predict your salary.")

# User input
years_exp = st.number_input("Years of Experience", min_value=0.0, step=0.1)

# Predict button
if st.button("Predict Salary"):
    salary_pred = model.predict(np.array([[years_exp]]))
    st.success(f"Predicted Salary: ₹{salary_pred[0]:,.2f}")
