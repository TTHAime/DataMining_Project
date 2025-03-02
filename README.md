# DataMining_Project

# 🫀 CVD Prediction Web App
https://dataminingproject12345.streamlit.app/

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

---
## โครงสร้างไฟล์โปรเจกต์

📦 CVD_Prediction
├── 📜 app.py                # หน้าแรกของแอป (ฟอร์มกรอกข้อมูล)
├── 📁 pages                 # หน้าผลลัพธ์
│   ├── 📜 Result.py         # แสดงผลลัพธ์การพยากรณ์
│   ├── 📜 Loading.py        # (อาจใช้เป็นหน้าโหลดข้อมูล)
├── 📜 requirements.txt      # รายการ dependencies
├── 📜 cvd_model.pkl         # โมเดล Machine Learning 
├── 📜 cvd_scaler.pkl        # Scaler สำหรับปรับค่าข้อมูล
└── 📜 README.md             # คำอธิบายโปรเจกต์

---

## Running Command
streamlit run app.py
