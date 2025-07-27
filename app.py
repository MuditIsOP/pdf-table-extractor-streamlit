
import streamlit as st  # ← Added for Streamlit UI
import pdfplumber
import pandas as pd
import io  # ← Added for in-memory Excel buffer

st.title("PDF Table Extractor and Excel Merger")

# ⬇️ Replaces file list logic with uploader
uploaded_files = st.file_uploader("Upload multiple PDF files", type="pdf", accept_multiple_files=True)  # ← Replaces manual file list

if st.button("Start") and uploaded_files:  # ← Add button logic for control
    dfs = []  # ← Changed variable name from 'df' to 'dfs' for clarity

    for file in uploaded_files:  # ← Replaces your file path loop with uploaded file loop
        with pdfplumber.open(file) as pdf:
            l = len(pdf.pages)
            for i in range(1, l):
                page = pdf.pages[i]
                table = page.extract_tables()
                for i, table in enumerate(table):
                    df = pd.DataFrame(table)
                    # ⬇️ Use first row as header if it's the first table
                    if df.shape[0] > 1:
                        df.columns = df.iloc[0]
                        df = df[1:]
                        df = df.reset_index(drop=True)

                        # Drop duplicate header rows
                        mask = (df == df.columns).all(axis=1)
                        df = df[~mask].reset_index(drop=True)

                        # Clean dashes and newlines in specific columns
                        if df.shape[1] > 8:  # ← safeguard
                            for col in [df.columns[9], df.columns[8]]:
                                        df[col] = (df[col].astype(str).str.replace(r'\n+', ' ', regex=True).str.replace(r'[—–\-]+', '\n', regex=True).str.replace('ENGINEERIN G','ENGINEERING').str.strip())
                    dfs.append(df)

    # ⬇️ Combine all extracted tables
    final_df = pd.concat(dfs, ignore_index=True)

    # ⬇️ Save to Excel in-memory instead of disk
    buffer = io.BytesIO()
    final_df.to_excel(buffer, index=False, engine='openpyxl')
    buffer.seek(0)

    # ⬇️ Provide download button
    st.success("Done! Click below to download the merged Excel file:")
    st.download_button(
        label="Download Excel File",
        data=buffer,
        file_name="merged_output.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
