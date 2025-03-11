import streamlit as st
import joblib
import os


st.set_page_config(page_title="CVD Prediction", layout="wide")

if not os.path.exists("cvd_model.pkl") or not os.path.exists("cvd_scaler.pkl"):
    st.error("🚨 Model or Scaler file missing! Please check 'cvd_model.pkl' and 'cvd_scaler.pkl'.")
    st.stop()

model = joblib.load("cvd_model.pkl")
scaler = joblib.load("cvd_scaler.pkl")

general_health_map = {'Poor': 0, 'Fair': 1, 'Good': 2, 'Very Good': 3, 'Excellent': 4}
age_category_map = {'18-24': 0, '25-29': 1, '30-34': 2, '35-39': 3, '40-44': 4,
                    '45-49': 5, '50-54': 6, '55-59': 7, '60-64': 8, '65-69': 9,
                    '70-74': 10, '75-79': 11, '80+': 12}
diabetes_map = {'No': 0, 'No, pre-diabetes or borderline diabetes': 0,
                'Yes, but female told only during pregnancy': 1, 'Yes': 1}

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
    
    .stSelectbox, .stRadio, .stTextInput  {
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

st.title("💙 Cardiovascular Disease Risk Prediction")
st.subheader("🔍 Fill in the details to predict your CVD risk")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        gender = st.radio("👤 Gender", [" Male", " Female"], index=None)
        general_health = st.selectbox("📋 General Health", list(general_health_map.keys()), index=None)
        age_category = st.selectbox("🎂 Age Category", list(age_category_map.keys()), index=None)
        exercise = st.selectbox("🏋️‍♂️ Do you exercise?", ["Yes", "No"], index=None)
        
    with col2:

        diabetes = st.selectbox("🩸 Diabetes?", list(diabetes_map.keys()), index=None)
        smoking = st.selectbox("🚬 Do you smoke?", ["Yes", "No"], index=None)
        arthritis = st.selectbox("🦴 Arthritis?", ["Yes", "No"], index=None)

    submit_button = st.form_submit_button("🔍 Predict")



# ===== การประมวลผลข้อมูล =====
if submit_button:
    if None in [gender, general_health, age_category, diabetes, smoking, exercise, arthritis]:
        st.warning("⚠️ Please fill in all the fields before predicting.")
        st.stop()
    else:
        sex_male_value = 1 if gender == "Male" else 0
        sex_female_value = 1 if gender == "Female" else 0
        general_health_value = general_health_map[general_health]
        age_category_value = age_category_map[age_category]
        diabetes_value = diabetes_map[diabetes]
        smoking_value = 1 if smoking == "Yes" else 0
        exercise_value = 1 if exercise == "Yes" else 0
        arthritis_value = 1 if arthritis == "Yes" else 0

        st.session_state["input_data"] = [
            sex_male_value, sex_female_value, general_health_value,
            age_category_value, diabetes_value, smoking_value,
            exercise_value, arthritis_value
        ]

        st.switch_page("pages/Result.py")