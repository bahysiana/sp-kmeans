import streamlit as st
from pathlib import Path
from utils.database import create_table

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Shopee Food K-Means Analysis",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# MEMBUAT DATABASE
# =====================================================

create_table()

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
# HERO SECTION
# =====================================================

st.markdown("""
<div style="
padding:35px;
border-radius:20px;
background:linear-gradient(90deg,#2563eb,#4f46e5);
color:white;
text-align:center;
margin-bottom:25px;
box-shadow:0 8px 24px rgba(37,99,235,0.25);
">

<h1>🍽️ Analisis Pola Transaksi Shopee Food</h1>

<h3>Menggunakan Metode K-Means Clustering</h3>

<p>
Buffet The Padang Pasir
</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# DESKRIPSI
# =====================================================

st.markdown("""
## 👋 Selamat Datang

Aplikasi ini dikembangkan sebagai media analisis untuk penelitian skripsi:

> **ANALISIS POLA TRANSAKSI SHOPEE FOOD MENGGUNAKAN METODE K-MEANS CLUSTERING BERDASARKAN DATA PEMESANAN PADA TOKO BUFFET THE PADANG PASIR**

Melalui aplikasi ini, pengguna dapat mengelola data transaksi, melakukan preprocessing, menjalankan algoritma K-Means Clustering, melihat hasil analisis, serta mengunduh laporan hasil clustering.
""")

st.divider()

# =====================================================
# FITUR
# =====================================================

st.subheader("✨ Fitur Utama")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
### 📂 Kelola Data

- Tambah Data
- Edit Data
- Hapus Data
- Import CSV
""")

with col2:
    st.success("""
### 🤖 Analisis

- Preprocessing
- StandardScaler
- K-Means
- Cluster 3
""")

with col3:
    st.warning("""
### 📊 Visualisasi

- Dashboard
- Grafik
- Hasil Cluster
- Download CSV
""")

st.divider()

# =====================================================
# ALUR PENELITIAN
# =====================================================

st.subheader("🚀 Alur Penggunaan")

st.markdown("""
1. 📤 Import atau tambah data transaksi.
2. 🧹 Lakukan preprocessing data.
3. 🤖 Jalankan K-Means Clustering (K = 3).
4. 📊 Analisis hasil pengelompokan.
5. 📥 Unduh hasil dalam format CSV.
""")

st.divider()

# =====================================================
# INTERPRETASI CLUSTER
# =====================================================

st.subheader("🎯 Interpretasi Cluster")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("""
### 🟢 Cluster 1

**Pola Pemesanan Personal**

- Jumlah pesanan rendah
- Total harga relatif kecil
- Konsumsi individu
""")

with c2:
    st.info("""
### 🔵 Cluster 2

**Pola Pemesanan Reguler**

- Nilai transaksi sedang
- Pembelian rutin
- Pelanggan reguler
""")

with c3:
    st.warning("""
### 🟣 Cluster 3

**Pola Pemesanan Kelompok**

- Jumlah pesanan tinggi
- Total harga besar
- Kebutuhan bersama
""")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "© 2026 | Dibangun menggunakan Python, Streamlit, SQLite, Plotly, dan Scikit-learn"
)
