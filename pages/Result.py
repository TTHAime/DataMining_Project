import streamlit as st
import numpy as np
import joblib
import os
import json
 # Load Model and Scaler
model = joblib.load("cvd_model.pkl")
scaler = joblib.load("cvd_scaler.pkl")
 
st.set_page_config(page_title="CVD Prediction Result", layout="centered")


# Load Mock Data
mock_input_path = os.path.join(os.path.dirname(__file__), "mock_input.json")
if os.path.exists(mock_input_path):
    with open(mock_input_path, "r") as file:
        mock_input = json.load(file)
else:
    st.error(f"🚨 File '{mock_input_path}' not found! Please check the file path.")
    st.stop()

# Assign mock data if session state doesn't exist
if "input_data" not in st.session_state:
    st.session_state["input_data"] = list(mock_input.values())
    
#  # Retrieve Input Data (Use session state or URL parameters)
# if "input_data" not in st.session_state:
#     st.error("No input data found! Please go back and submit the form again.")
#     st.stop()
 
input_data = st.session_state["input_data"]
 
 # Scale the Input Data
input_data_scaled = scaler.transform(np.array([input_data]))
 
 # Predict
prediction_proba = model.predict_proba(input_data_scaled)[0]
risk_percentage = prediction_proba[1] * 100
 
 # Display Result
st.markdown("""
    <style>
     .stApp {
          background: linear-gradient(to bottom , #0f3d3e, #1b6b6a, #6ebf8b);
          color: #ffffff;
          font-family: 'Arial', sans-serif;
          text-align: center;
          height: 100vh;
    }
    .stError {
          background-color: #ff4d4d; 
          color: white;            
          border: 3px solid #b30000; 
          border-radius: 15px;      
          padding: 15px;
          font-size: 20px;
          box-shadow: 3px 3px 15px rgba(255, 0, 0, 0.3); 
     }
     .stSuccess {
        background-color: white; 
        color: black;              /* ตัวอักษรสีขาว */
        border: 3px solid #ffffff; /* ขอบหนาสีเขียวเข้ม */
        border-radius: 15px;       /* มุมโค้งมน */
        padding: 15px;
        box-shadow: 3px 3px 15px rgba(0, 128, 0, 0.3); /* เพิ่มเงา */
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        margin: 20px 0;
     }
     
     .stExpander {
    background: white !important;
    color: black !important;
    font-size: 20px;
    border-radius: 15px !important;
    padding: 15px !important;
    box-shadow: 3px 3px 15px rgba(0, 0, 0, 0.1) !important;
    width: 450px; 
    margin: auto; 
    transition: max-height 0.4s ease-in-out; 
    overflow: hidden;
}
     


          
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='result-title'>🩺 Cardiovascular Risk Result 🩺</h1>", unsafe_allow_html=True)

if risk_percentage >= 50:
     risk_text = f"⚠️ **High Risk**: {risk_percentage:.2f}%"
     st.markdown(f"<div class='stError'>{risk_text}</div>", unsafe_allow_html=True)
else:
     risk_text = f"✅ **Low Risk**: {risk_percentage:.2f}%"
     st.markdown(f"<div class='stSuccess'>{risk_text}</div>", unsafe_allow_html=True)




 
st.markdown(f"📊 **Chance of Cardiovascular Disease:** {risk_percentage:.2f}%")

 # Show Explanation
with st.expander("📌 More Details"):
     st.write("This prediction is based on your provided health details.")
     st.write("**If you have a high risk, consider consulting a healthcare professional.**")
     
    


if "go_home" not in st.session_state:
     st.session_state["go_home"] = False
 
def go_home():
     st.session_state["go_home"] = True
 
st.button("🔙 Back to Home", on_click=go_home)
 
 # ถ้าค่าถูกตั้งให้กลับไปหน้าแรก
if st.session_state["go_home"]:
     st.session_state["go_home"] = False  # รีเซ็ตค่า
     st.switch_page("app.py")