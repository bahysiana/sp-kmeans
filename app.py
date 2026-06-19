import streamlit as st
from pathlib import Path
from utils.database import create_table

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Analisis Pola Transaksi Shopee Food",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# LOAD CSS
# =====================================================

css_path = Path("assets/style.css")

if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================================
# INISIALISASI DATABASE
# =====================================================

create_table()

# =====================================================
# HALAMAN UTAMA
# =====================================================

st.title("🍽️ Analisis Pola Transaksi Shopee Food")

st.markdown("""
### Menggunakan Metode K-Means Clustering

Selamat datang di aplikasi analisis pola transaksi Shopee Food yang dikembangkan sebagai media pendukung penelitian skripsi.

Aplikasi ini menyediakan beberapa fitur utama, antara lain:

- 📂 Kelola Data Transaksi
- 📤 Import Dataset CSV
- 🧹 Preprocessing Data
- 🤖 Proses K-Means Clustering
- 📊 Visualisasi Hasil Cluster
- 📥 Download Hasil Analisis

Silakan gunakan menu di **sidebar sebelah kiri** untuk memulai proses analisis.
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
### 📂 Kelola Data

Menambah, mengubah, menghapus, dan mengimpor data transaksi Shopee Food.
""")

with col2:
    st.success("""
### 🤖 K-Means Clustering

Melakukan pengelompokan data menggunakan metode K-Means dengan K = 3.
""")

with col3:
    st.warning("""
### 📊 Hasil Analisis

Menampilkan hasil clustering, visualisasi, dan interpretasi setiap cluster.
""")

st.divider()

st.caption(
    "© 2026 | Analisis Pola Transaksi Shopee Food Menggunakan Metode K-Means Clustering"
)
