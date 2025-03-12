# DataMining_Project

# 🫀 CVD Prediction Web App
https://datamining-g9.streamlit.app/

### 🔍 ทำนายความเสี่ยงของโรคหัวใจและหลอดเลือดด้วย Machine Learning

เว็บแอปนี้ช่วยให้คุณสามารถพยากรณ์ **ความเสี่ยงของโรคหัวใจและหลอดเลือด (Cardiovascular Disease - CVD)** ได้โดยใช้ **Machine Learning** ผ่าน **Streamlit** 🔥  
เพียงกรอกข้อมูลด้านสุขภาพ ระบบจะคำนวณโอกาสเสี่ยงและแสดงผลลัพธ์แบบเข้าใจง่าย ✅

---

## 🏗️ เทคโนโลยีที่ใช้
- **Python 3.12**  - ภาษาโปรแกรมหลัก
- **Streamlit**  - ใช้สร้างเว็บแอป
- **Scikit-Learn**  - ใช้สำหรับโมเดล Machine Learning
- **Joblib**  - โหลดโมเดลที่ถูกฝึกมาแล้ว (`cvd_model.pkl`)
- **NumPy**  - จัดการข้อมูลตัวเลข
- **Pandas**  - ใช้จัดการข้อมูล (ถ้าจำเป็น)
- **XGBoost**, a powerful gradient boosting algorithm 

---
## 📂 โครงสร้างไฟล์โปรเจกต์

/project-root
│
├── pages/
│   └── Result.py         # ไฟล์ที่อาจใช้แสดงผลลัพธ์
│
├── app.py                # ไฟล์หลักที่รันเว็บแอปพลิเคชัน
├── model.pkl             # ไฟล์โมเดล Machine Learning ที่บันทึกไว้
├── README.md             # คำอธิบายโปรเจกต์
└── requirements.txt      # รายการไลบรารีที่ต้องติดตั้ง

---

## Libraly install Command
pip install streamlit numpy joblib scikit-learn pandas xgboost

---

## 🏃 Running Command
streamlit run app.py
