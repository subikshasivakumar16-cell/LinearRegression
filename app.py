# app.py
import streamlit as st
import pickle
import numpy as np

# ===== Page Config =====
st.set_page_config(page_title="Salary Predictor", page_icon="💼", layout="centered")

# ===== Load Model =====
with open("SalaryPrediction.pkl", "rb") as f:
    model = pickle.load(f)

# ===== Sidebar Info =====
st.sidebar.title("📌 About the App")
st.sidebar.write(
    """
    This is a **simple Salary Prediction App**  
    based on **Linear Regression**.
    
    Just enter your **years of experience**  
    and see your predicted salary instantly.
    """
)
st.sidebar.markdown("👩‍💻 *Created by Subiksha Sivakumar*")

# ===== Main Title =====
st.markdown("<h1 style='text-align: center;'>💼 Salary Prediction App</h1>", unsafe_allow_html=True)
st.write("### 🚀 Enter your details below:")

# ===== Input Form =====
with st.form("salary_form"):
    years_exp = st.number_input(
        "Years of Experience",
        min_value=0.0,
        step=0.1,
        format="%.1f",
        help="Enter your work experience in years."
    )
    predict_btn = st.form_submit_button("🔍 Predict Salary")

# ===== Prediction =====
if predict_btn:
    with st.spinner("Calculating salary... 💭"):
        salary_pred = model.predict(np.array([[years_exp]]))[0]
    st.success(f"💰 **Predicted Salary:** ₹{salary_pred:,.2f}")
    st.balloons()

# ===== Footer =====
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
