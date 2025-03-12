import streamlit as st
import numpy as np
import joblib
import os
import json
 # Load Model and Scaler
model = joblib.load("model.pkl")
 
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
    
 # Retrieve Input Data (Use session state or URL parameters)
if "input_data" not in st.session_state:
    st.error("No input data found! Please go back and submit the form again.")
    st.stop()
 
input_data = st.session_state["input_data"]
 
 
 # Predict
input_data = np.array(input_data).reshape(1, -1)
prediction_proba = model.predict_proba(input_data)[0]
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
          text-align: center;
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
          background-color: #e6f7ff;
          color: black;
          font-size: 20px;
          border: 2px solid #007acc;
          border-radius: 12px;
          padding: 15px;
          box-shadow: 3px 3px 15px rgba(0, 0, 0, 0.1);
}
     .input-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        padding: 10px;
    }
    .input-item {
        background-color: #f0f8ff;
        border-radius: 8px;
        padding: 5px 10px;
        border: 1px solid #ccc;
        text-align: left;
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



st.markdown("---")

st.markdown(f"📊 **Chance of Cardiovascular Disease:** {risk_percentage:.2f}%")

 # Show Explanation
with st.expander("📌 More Details"):
     st.write("This prediction is based on your provided health details.")
     st.write("**If you have a high risk, consider consulting a healthcare professional.**")
     
     # Display Input Data in Detailed Format
     st.markdown("### Input Data")
     input_keys = ["General_Health", "Exercise", "Skin_Cancer", "Other_Cancer", "Depression",
                    "Arthritis", "Age_Category", "Height_(cm)", "Weight_(kg)", "BMI",
                    "Smoking_History", "Alcohol_Consumption", "Fruit_Consumption",
                    "Green_Vegetables_Consumption", "FriedPotato_Consumption",
                    "Sex_Female", "Sex_Male"]
     input_details = dict(zip(input_keys, input_data[0]))
    
     st.markdown("<div class='input-grid'>", unsafe_allow_html=True)
     for key, value in input_details.items():
          st.markdown(f"<div class='input-item'><b>{key}:</b> {value}</div>", unsafe_allow_html=True)
     st.markdown("</div>", unsafe_allow_html=True)
    


if "go_home" not in st.session_state:
     st.session_state["go_home"] = False
 
def go_home():
     st.session_state["go_home"] = True
 
st.button("🔙 Back to Home", on_click=go_home)
 
 # ถ้าค่าถูกตั้งให้กลับไปหน้าแรก
if st.session_state["go_home"]:
     st.session_state["go_home"] = False  # รีเซ็ตค่า
     st.switch_page("app.py")