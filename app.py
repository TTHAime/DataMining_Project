import streamlit as st
import numpy as np
import joblib
import os

# ตรวจสอบว่าไฟล์โมเดลและ scaler มีอยู่จริง
if not os.path.exists("cvd_model.pkl") or not os.path.exists("cvd_scaler.pkl"):
    st.error(" Model or Scaler file missing! Please check 'cvd_model.pkl' and 'cvd_scaler.pkl'.")
    st.stop()

# โหลดโมเดลและตัวปรับสเกล
model = joblib.load("cvd_model.pkl")
scaler = joblib.load("cvd_scaler.pkl")

st.set_page_config(page_title="CVD Prediction", layout='centered')

# Mapping ค่าที่เป็นข้อความไปเป็นตัวเลข
general_health_map = {
    'Poor': 0, 'Fair': 1, 'Good': 2, 'Very Good': 3, 'Excellent': 4
}

age_category_map = {
    '18-24': 0, '25-29': 1, '30-34': 2, '35-39': 3, '40-44': 4, 
    '45-49': 5, '50-54': 6, '55-59': 7, '60-64': 8, '65-69': 9, 
    '70-74': 10, '75-79': 11, '80+': 12
}

diabetes_map = {
    'No': 0, 
    'No, pre-diabetes or borderline diabetes': 0,
    'Yes, but female told only during pregnancy': 1,
    'Yes': 1
}

# Title
st.markdown(
    "<h1 style='text-align: center; font-size:30px'>Cardiovascular Diseases Risk Prediction</h1>",
    unsafe_allow_html=True
)

with st.form(key='prediction_form'):
    st.subheader(" Enter the following details to predict CVD risk")

    gender = st.radio("👤 Gender", ["Male", "Female"], index=None)
    general_health = st.selectbox(" General Health", list(general_health_map.keys()), index=None)
    age_category = st.selectbox(" Age Category", list(age_category_map.keys()), index=None)
    diabetes = st.selectbox(" Diabetes?", list(diabetes_map.keys()), index=None)
    smoking = st.selectbox(" Do you smoke?", ["Yes", "No"], index=None)
    exercise = st.selectbox(" Do you exercise?", ["Yes", "No"], index=None)
    arthritis = st.selectbox(" Arthritis?", ["Yes", "No"], index=None)

    is_filled = all([
        gender, general_health, age_category, diabetes, smoking, exercise, arthritis
    ])

    submit_button = st.form_submit_button("🔍 Predict")

    if submit_button:
        if is_filled:
            # แปลงค่าข้อมูลเป็นตัวเลข
            sex_male_value = 1 if gender == "Male" else 0
            sex_female_value = 1 if gender == "Female" else 0
            general_health_value = general_health_map[general_health]
            age_category_value = age_category_map[age_category]
            diabetes_value = diabetes_map[diabetes]
            smoking_value = 1 if smoking == "Yes" else 0
            exercise_value = 1 if exercise == "Yes" else 0
            arthritis_value = 1 if arthritis == "Yes" else 0

            # บันทึกค่าลงใน session_state เพื่อนำไปใช้ใน Result.py
            st.session_state["input_data"] = [
                sex_male_value, sex_female_value, general_health_value,
                age_category_value, diabetes_value, smoking_value, 
                exercise_value, arthritis_value
            ]

            # ไปที่หน้าแสดงผลลัพธ์
            st.switch_page("pages/Loading.py")

        else:
            st.warning("⚠️ Please fill in all the fields before predicting.")
