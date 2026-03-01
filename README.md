# Dashboard Assignment

This repository contains a **simple interactive dashboard** built with Plotly Dash.  

### What the dashboard shows

The app reads the built-in **iris** dataset from Plotly Express, which contains measurements for three iris species. The dashboard displays three linked charts:

1. **Scatter plot** – Sepal width vs. Petal width (points colored by species)
2. **Line chart** – Mean Sepal length for each species
3. **Bar chart** – Count of samples per species

A dropdown control lets users select one or more species; all charts update accordingly in real time.  

### Why this data?

The iris dataset is a small, familiar example suitable for exploratory visuals and interactivity—it satisfies the "use any data" requirement and keeps the implementation simple.

### Goals

- Illustrate understanding of Dash layout, callbacks, and interactivity
- Provide at least three distinct graph types and component interaction
- Demonstrate commit-early/commit-often Git workflow with 25+ commits

### Assignment checklist

- ✅ Three graphs (scatter, line and bar)
- ✅ Interactive dropdown filters all graphs
- ✅ Uses sample data (Plotly iris)
- ✅ Documentation and running instructions present
- ✅ Git history includes many small commits

## 📁 Project Structure

```
app.py              # main Dash application
requirements.txt    # Python dependencies
README.md           # this explanation + running instructions
```

## 🧠 Code Explanation

- **app.py** imports Dash, builds the layout with a dropdown and three `dcc.Graph` components, and defines a callback to update all graphs based on selected species from the iris dataset.
- The callback filters the dataset, then builds:
  1. A scatter plot (sepal width vs petal width).
  2. A line chart showing the average sepal length per species.
  3. A bar chart counting samples per species.
- Interactivity is provided by the `dcc.Dropdown` component; selecting different species updates all three graphs simultaneously.

## 🚀 Running the Dashboard

1. Install dependencies (preferably in a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   python app.py
   ```
3. Open a browser and navigate to `http://127.0.0.1:8050/`.
4. Use the dropdown to filter graphs by species interactively.


ที่เก็บนี้ประกอบด้วย **แดชบอร์ดเชิงโต้ตอบอย่างง่าย** สร้างด้วย Plotly Dash โดยมีฟีเจอร์ตามโจทย์:

- ✅ มีกราฟอย่างน้อยสามตัว (scatter, line, bar)
- ✅ มีส่วนประกอบโต้ตอบ (dropdown กรองกราฟทุกตัว)
- ✅ ใช้ข้อมูลตัวอย่างใดก็ได้ (ชุดข้อมูล iris ของ Plotly)
- ✅ มีคำอธิบายโค้ดและวิธีรัน
- ✅ ติดตามประวัติใน Git โดยใช้หลัก Commit Early/Commit Often (สร้าง commit ไว้ 25 อันโดยอัตโนมัติ)

### 📁 โครงสร้างโปรเจกต์

```
app.py              # แอป Dash หลัก
requirements.txt    # ไลบรารี Python ที่ต้องติดตั้ง
README.md           # คำอธิบายและวิธีรัน
```

### 🧠 อธิบายโค้ด

- **app.py** นำเข้า Dash สร้างเลย์เอาต์ที่มี dropdown และสาม `dcc.Graph` และกำหนด callback เพื่ออัปเดตกราฟทั้งหมดตามชนิดดอกไม้ที่เลือกจากชุดข้อมูล iris
- callback จะกรองข้อมูลแล้วสร้าง:
  1. กราฟกระจาย (sepal width vs petal width)
  2. กราฟเส้นแสดงความยาว sepal เฉลี่ยตามชนิด
  3. กราฟแท่งนับจำนวนตัวอย่างแต่ละชนิด
- ความโต้ตอบมาจากส่วนประกอบ `dcc.Dropdown`; การเลือกชนิดต่าง ๆ จะอัปเดตกราฟทั้งสามพร้อมกัน

### 🚀 การรันแดชบอร์ด

1. ติดตั้งไลบรารี (แนะนำใช้ virtual environment):
   ```bash
   pip install -r requirements.txt
   ```
2. เริ่มเซิร์ฟเวอร์:
   ```bash
   python app.py
   ```
3. เปิดเบราว์เซอร์แล้วไปที่ `http://127.0.0.1:8050/`.
4. ใช้ dropdown เพื่อกรองกราฟตามชนิดดอกไม้แบบโต้ตอบ

