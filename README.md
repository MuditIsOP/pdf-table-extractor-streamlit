
# 📄 PDF Table Extractor & Excel Merger (Streamlit App)

This Streamlit-powered web app lets you upload multiple PDF files with tables, extract them from each page, clean the data, and export the merged results as a single Excel file.

---

## 🚀 Features

- 📥 Upload multiple `.pdf` files at once
- 📄 Extracts tables from **every page** (except page 1 by default)
- 🧹 Automatically cleans repeated headers and dash lines
- 📊 Combines all tables into a **single Excel sheet**
- ⬇️ One-click download of the final merged file

---

## ⚙️ Tech Stack

- **Python 3.10+**
- [pdfplumber](https://pypi.org/project/pdfplumber/)
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://pypi.org/project/openpyxl/)
- [Streamlit](https://streamlit.io/)

---

## 💻 How to Run

### Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Deploy Online (Free)
1. Upload to a GitHub repo
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Link your repo and deploy in 1 click

---

## 🎯 Use Case

Perfect for automating PDF-to-Excel conversions where tables are spread across many PDFs — such as school data lists, hospital rosters, reports, and more.

---

## 👤 Author

**Mudit Sharma** – B.Tech AI Student 💡  
[LinkedIn: Mudit Sharma](https://www.linkedin.com/in/muditsharma-)  
Feel free to fork, contribute or suggest features!

---

## 📜 License

This project is licensed under the MIT License.
