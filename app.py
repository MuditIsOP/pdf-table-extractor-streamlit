
import streamlit as st
import pdfplumber
import pandas as pd
import io
st.title("PDF Table Extractor and Excel Merger")
uploaded_files = st.file_uploader("Upload multiple PDF files", type="pdf", accept_multiple_files=True)  # ← Replaces manual file list

if st.button("Start") and uploaded_files:
    dfs = []
    for file in uploaded_files:
        with pdfplumber.open(file) as pdf:
            l = len(pdf.pages)
            for i in range(1, l):
                page = pdf.pages[i]
                table = page.extract_tables()
                for i, table in enumerate(table):
                    df = pd.DataFrame(table)
                    if df.shape[0] > 1:
                        df.columns = df.iloc[0]
                        df = df[1:]
                        df = df.reset_index(drop=True)
                        mask = (df == df.columns).all(axis=1)
                        df = df[~mask].reset_index(drop=True)
                        if df.shape[1] > 8:
                            for col in [df.columns[9], df.columns[8]]:
                                        df[col] = (df[col].astype(str).str.replace(r'\n+', ' ', regex=True).str.replace(r'[—–\-]+', '\n', regex=True).str.replace('ENGINEERIN G','ENGINEERING').str.strip())
                    dfs.append(df)
    final_df = pd.concat(dfs, ignore_index=True)
    buffer = io.BytesIO()
    final_df.to_excel(buffer, index=False, engine='openpyxl')
    buffer.seek(0)
    st.success("Done! Click below to download the merged Excel file:")
    st.download_button(
        label="Download Excel File",
        data=buffer,
        file_name="merged_output.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
