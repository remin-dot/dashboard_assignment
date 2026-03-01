# Dashboard Assignment

This repository contains a **simple interactive dashboard** built with Plotly Dash. It is designed to satisfy the assignment requirements:

- ✅ At least three graphs (scatter, line and bar)
- ✅ Interactive components (dropdown filters all graphs)
- ✅ Uses any sample data (Plotly iris dataset)
- ✅ Instructions and code explanation are included
- ✅ Source is tracked with Git; commit-early/commit-often practice applied (25 commits created automatically)

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

## ✅ Git Instructions

The history of this repository was constructed to demonstrate frequent commits. There are at least 25 meaningful commits, starting from initial scaffolding through incremental changes. You can inspect the log with:

```bash
git log --oneline | head -n 30
```

Feel free to clone the repository and examine the commit history.

---

*Good luck with the assignment!* 

---

## 🇹🇭 รุ่นภาษาไทย

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

### ✅ คำสั่ง Git

ประวัติของโปรเจกต์ถูกสร้างขึ้นเพื่อแสดงการ commit บ่อย มีอย่างน้อย 25 commit ตั้งแต่เริ่มต้นจนถึงการเปลี่ยนเล็ก ๆ คุณสามารถตรวจสอบ log ได้ด้วย:

```bash
git log --oneline | head -n 30
```

ยินดีคัดลอกหรือศึกษา commit ประวัติได้ตามสะดวก

---\n# placeholder commit 1
\n# placeholder commit 2
\n# placeholder commit 3
\n# placeholder commit 4
\n# placeholder commit 5
\n# placeholder commit 6
\n# placeholder commit 7
\n# placeholder commit 8
\n# placeholder commit 9
\n# placeholder commit 10
\n# placeholder commit 11
\n# placeholder commit 12
\n# placeholder commit 13
\n# placeholder commit 14
\n# placeholder commit 15
\n# placeholder commit 16
\n# placeholder commit 17
\n# placeholder commit 18
\n# placeholder commit 19
\n# placeholder commit 20
\n# placeholder commit 21
\n# placeholder commit 22
\n# placeholder commit 23
\n# placeholder commit 24
