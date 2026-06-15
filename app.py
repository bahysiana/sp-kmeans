import streamlit as st
from utils.database import create_table

create_table()

st.set_page_config(
    page_title="Shopee Food Transaction Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 Shopee Food Transaction Analytics")

st.subheader(
    "Analisis Pola Transaksi Menggunakan Metode K-Means Clustering"
)

st.markdown("---")

st.info("""
Selamat datang di aplikasi analisis pola transaksi Shopee Food.

Silakan gunakan menu di sidebar untuk:
- Dashboard
- Kelola Data
- Preprocessing
- Analisis K-Means
- Hasil Clustering
- Download CSV
""")
