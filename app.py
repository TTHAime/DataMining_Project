import streamlit as st
import joblib
import os
import pandas as pd


st.set_page_config(page_title="CVD Prediction", layout="wide")

if not os.path.exists("model.pkl") :
    st.error("🚨 Model or Scaler file missing! Please check 'cvd_model.pkl' and 'cvd_scaler.pkl'.")
    st.stop()

model = joblib.load("model.pkl")

# ===== Data_map ===== # 
general_health_map = {'Poor': 0, 'Fair': 1, 'Good': 2, 'Very Good': 3, 'Excellent': 4}
age_category_map = {'18-24': 0, '25-29': 1, '30-34': 2, '35-39': 3, '40-44': 4,
                    '45-49': 5, '50-54': 6, '55-59': 7, '60-64': 8, '65-69': 9,
                    '70-74': 10, '75-79': 11, '80+': 12}


# ===== CSS ===== # 
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f3d3e, #1b6b6a, #6ebf8b);
        color: #ffffff;
        font-family: 'Arial', sans-serif;
        text-align: center;
        height: 100vh;
    }
    
    label, p {
        font-size: 18px !important;
        font-weight: bold;
        color: #1e3c72;
      
    }
    
    .stSelectbox, .stRadio, .stTextInput , .stNumberInput {
        background: #f5f5f5 !important;
        color: #000000 !important;
        font-size: 18px !important;
        border-radius: 8px;
        padding: 10px;
        border: 2px solid #d4af37;
    }
    
    .stFormSubmitButton>button {
            font-size:40px;
            background: #f5f5f5 !important;
            color: black;
            margin: 0 auto;
            height: 50px;
            p {
                font-size: 40px;
            }
        }
    .stFormSubmitButton>button:hover {
            transform: scale(1.05);
    }
    
    .stFormSubmitButton>button:active {
            transform: scale(0.98);
    }
    
    .stAlert {
            background-color: #fff3cd !important;
            border-left: 5px solid #ffcc00 !important;
            color: #856404 !important;
            font-size: 18px !important;
            padding: 20px !important;
            border-radius: 8px !important;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2) !important;
            animation: fadeIn 0.5s ease-in-out;
        }

    @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
    }
   
</style>
""", unsafe_allow_html=True)

# ===== ส่วน UI =====

st.title("💙 Cardiovascular Disease Risk Prediction 💙")
st.subheader("🔍 Fill in the details to predict your CVD risk")

with st.form("prediction_form"):
    
    col1, col2 = st.columns(2)
    with col1:
        gender = st.radio("👤 Gender", ["Male", "Female"], index=None)
        general_health = st.selectbox("📋 General Health", list(general_health_map.keys()), index=None)
        age_category = st.selectbox("🎂 Age Category", list(age_category_map.keys()), index=None)
        exercise = st.selectbox("🏋️‍♂️ Do you exercise?", ["Yes", "No"], index=None)
        height = st.number_input("📏 Height (cm)", min_value=0, max_value=250, value=0)
        weight = st.number_input("⚖️ Weight (kg)", min_value=0.0, max_value=300.0, value=0.0, step=0.1)
        alcohol = st.number_input("🍺 Alcohol Consumption (per week )", min_value=0, max_value=50, value=0)
        
    fruit = st.number_input("🍎 Fruit Consumption (per week )", min_value=0, max_value=200, value=0)    
    with col2:
        smoking = st.selectbox("🚬 Do you smoke?", ["Yes", "No"], index=None)
        arthritis = st.selectbox("🦴 Arthritis?", ["Yes", "No"], index=None)
        skin_cancer = st.selectbox("🌞 Skin Cancer?", ["Yes", "No"], index=None)
        other_cancer = st.selectbox("🧬 Other Cancer?", ["Yes", "No"], index=None)
        depression = st.selectbox("😔 Depression?", ["Yes", "No"], index=None)
        vegetables = st.number_input("🥦 Green Vegetables Consumption (per week)", min_value=0, max_value=200, value=0)
        fried_potato = st.number_input("🍟 Fried Potato Consumption (per week)", min_value=0, max_value=200, value=0)
    
    submit_button = st.form_submit_button("🔍 Predict")
    
    



# ===== การประมวลผลข้อมูล =====
if submit_button:
    if None in [gender, general_health, age_category, smoking, exercise, arthritis, skin_cancer, other_cancer, depression]:
        st.warning("⚠️ Please fill in all the fields before predicting.")
        st.stop()
    else:
        bmi = round( weight / ((height / 100) ** 2), 2)
        input_data = pd.DataFrame({
            'General_Health': [general_health_map[general_health]],
            'Exercise': [1 if exercise == "Yes" else 0],
            'Skin_Cancer': [1 if skin_cancer == "Yes" else 0],
            'Other_Cancer': [1 if other_cancer == "Yes" else 0],
            'Depression': [1 if depression == "Yes" else 0],
            'Arthritis': [1 if arthritis == "Yes" else 0],
            'Age_Category': [age_category_map[age_category]],
            'Height_(cm)': [height],
            'Weight_(kg)': [weight],
            'BMI': [bmi],
            'Smoking_History': [1 if smoking == "Yes" else 0],
            'Alcohol_Consumption': [alcohol],
            'Fruit_Consumption': [fruit],
            'Green_Vegetables_Consumption': [vegetables],
            'FriedPotato_Consumption': [fried_potato],
            'Sex_Female': [1 if gender == "Female" else 0],
            'Sex_Male': [1 if gender == "Male" else 0]
        })      

        st.write("### Input Data for Prediction")
        st.session_state["input_data"] = input_data
        st.dataframe(input_data)

        st.switch_page("pages/Result.py")