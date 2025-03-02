import streamlit as st
import numpy as np
import joblib

# Load Model and Scaler
model = joblib.load("cvd_model.pkl")
scaler = joblib.load("cvd_scaler.pkl")

st.set_page_config(page_title="CVD Prediction Result", layout="centered")

# Retrieve Input Data (Use session state or URL parameters)
if "input_data" not in st.session_state:
    st.error("No input data found! Please go back and submit the form again.")
    st.stop()

input_data = st.session_state["input_data"]

# Scale the Input Data
input_data_scaled = scaler.transform(np.array([input_data]))

# Predict
prediction_proba = model.predict_proba(input_data_scaled)[0]
risk_percentage = prediction_proba[1] * 100

# Display Result
st.markdown(
    "<h1 style='text-align: center; font-size:30px'>🩺 Cardiovascular Risk Result 🩺</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

if risk_percentage >= 50:
    risk_text = f"⚠️ **High Risk**: {risk_percentage:.2f}%"
    st.error(risk_text)
else:
    risk_text = f"✅ **Low Risk**: {risk_percentage:.2f}%"
    st.success(risk_text)

st.markdown(f"📊 **Chance of Cardiovascular Disease:** {risk_percentage:.2f}%")

# Show Explanation
with st.expander("📌 More Details"):
    st.write("This prediction is based on your provided health details.")
    st.write("**If you have a high risk, consider consulting a healthcare professional.**")

st.markdown("---")

if "go_home" not in st.session_state:
    st.session_state["go_home"] = False

def go_home():
    st.session_state["go_home"] = True

st.button("🔙 Back to Home", on_click=go_home)

# ถ้าค่าถูกตั้งให้กลับไปหน้าแรก
if st.session_state["go_home"]:
    st.session_state["go_home"] = False  # รีเซ็ตค่า
    st.switch_page("app.py")
