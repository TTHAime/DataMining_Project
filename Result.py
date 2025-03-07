import streamlit as st
import numpy as np
import joblib
import time

model = joblib.load("cvd_model.pkl")
scaler = joblib.load("cvd_scaler.pkl")

st.set_page_config(page_title="CVD Prediction Result", layout="centered")

st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            color: #333;
        }
        .result-title {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            color: #1e3c72;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        }
        .result-box {
            font-size: 24px;
            font-weight: bold;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            margin: 20px auto;
            width: 60%;
        }
        .high-risk {
            background-color: #ffdddd;
            color: #b30000;
            border-left: 6px solid #b30000;
        }
        .low-risk {
            background-color: #e6ffe6;
            color: #006400;
            border-left: 6px solid #006400;
        }
        .streamlit-expanderHeader {
            font-size: 18px !important;
            font-weight: bold !important;
            color: #1e3c72 !important;
        }
        .back-button {
            background: linear-gradient(to right, #1e3c72, #0f2c61);
            color: white;
            font-size: 18px;
            padding: 12px;
            border-radius: 8px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            margin: 20px auto;
            width: 200px;
        }
        .back-button:hover {
            background: linear-gradient(to right, #d4af37, #b8860b);
        }
    </style>
""", unsafe_allow_html=True)

if "input_data" not in st.session_state:
    st.error("No input data found! Please go back and submit the form again.")
    st.stop()

input_data = st.session_state["input_data"]

input_data_scaled = scaler.transform(np.array([input_data]))

prediction_proba = model.predict_proba(input_data_scaled)[0]
risk_percentage = prediction_proba[1] * 100

st.markdown("<h1 class='result-title'>🩺 Cardiovascular Risk Result 🩺</h1>", unsafe_allow_html=True)

st.markdown("---")

if risk_percentage >= 50:
    st.markdown(f"<div class='result-box high-risk'>⚠️ <b>High Risk:</b> {risk_percentage:.2f}%</div>", unsafe_allow_html=True)
    st.error(f"⚠️ High Risk: {risk_percentage:.2f}%")
else:
    st.markdown(f"<div class='result-box low-risk'>✅ <b>Low Risk:</b> {risk_percentage:.2f}%</div>", unsafe_allow_html=True)
    st.success(f"✅ Low Risk: {risk_percentage:.2f}%")

st.markdown(f"📊 **Chance of Cardiovascular Disease:** {risk_percentage:.2f}%")

with st.expander("📌 More Details"):
    st.write("This prediction is based on your provided health details.")
    st.write("**If you have a high risk, consider consulting a healthcare professional.**")

st.markdown("---")

if "go_home" not in st.session_state:
    st.session_state["go_home"] = False

def go_home():
    st.session_state["go_home"] = True

st.markdown('<div class="back-button">🔙 Back to Home</div>', unsafe_allow_html=True)

if st.session_state["go_home"]:
    st.session_state["go_home"] = False
    st.switch_page("app.py")