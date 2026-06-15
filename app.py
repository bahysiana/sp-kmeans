import streamlit as st
from pathlib import Path

# ==========================
# KONFIGURASI HALAMAN
# ==========================
st.set_page_config(
    page_title="Shopee Food Transaction Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# LOAD CSS
# ==========================
css_file = Path("assets/style.css")

if css_file.exists():
    with open(css_file, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ==========================
# HEADER
# ==========================
st.markdown("""
<div class="hero-container">

<h1>📊 Shopee Food Transaction Analytics</h1>

<h3>
Analisis Pola Transaksi Menggunakan Metode
K-Means Clustering
</h3>

<p>
Buffet The Padang Pasir
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================
# METRIC CARD
# ==========================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📦 Modul",
        "CRUD + K-Means"
    )

with col2:
    st.metric(
        "🧠 Algoritma",
        "K-Means"
    )

with col3:
    st.metric(
        "📈 Visualisasi",
        "Interactive"
    )

with col4:
    st.metric(
        "💾 Database",
        "SQLite"
    )

st.divider()

# ==========================
# DESKRIPSI
# ==========================
left, right = st.columns([2, 1])

with left:

    st.markdown("""
## 🎯 Tentang Aplikasi

Aplikasi ini dikembangkan untuk membantu menganalisis
pola transaksi Shopee Food pada
**Buffet The Padang Pasir**
menggunakan algoritma
**K-Means Clustering**.

Fitur utama aplikasi:

- 📂 Upload dataset CSV
- ➕ Tambah data transaksi
- ✏️ Edit data transaksi
- 🗑️ Hapus data transaksi
- ⚙️ Preprocessing otomatis
- 🤖 Analisis K-Means
- 📉 Elbow Method
- 📊 Silhouette Score
- 📈 Visualisasi cluster
- 📥 Download hasil clustering

Seluruh data disimpan menggunakan
**SQLite Database** sehingga data
tidak hilang ketika aplikasi ditutup.
""")

with right:

    st.info("""
### 📌 Variabel Clustering

Variabel yang digunakan
dalam proses K-Means:

- Total Harga
- Jumlah Pesanan
- Rata-rata Harga
- Waktu Persiapan Digunakan
""")

    st.success("""
### 🧩 Interpretasi Cluster

🟢 Pola Pemesanan Personal

🔵 Pola Pemesanan Reguler

🟣 Pola Pemesanan Kelompok
""")

st.divider()

# ==========================
# ALUR SISTEM
# ==========================
st.markdown("## 🔄 Alur Penggunaan Sistem")

st.markdown("""
1. 📂 Kelola Data Transaksi  
2. ⚙️ Lakukan Preprocessing Data  
3. 🤖 Jalankan Algoritma K-Means  
4. 📈 Analisis Hasil Clustering  
5. 📥 Download Hasil CSV
""")

st.divider()

# ==========================
# PETUNJUK SIDEBAR
# ==========================
st.markdown("""
## 🚀 Mulai Menggunakan

Silakan gunakan menu pada **sidebar sebelah kiri**
untuk berpindah halaman:

- 📊 Dashboard
- 📂 Kelola Data
- ⚙️ Preprocessing
- 🤖 K-Means
- 📈 Hasil
- 📥 Download
- ℹ️ Tentang
""")

st.divider()

# ==========================
# FOOTER
# ==========================
st.caption("""
Dikembangkan untuk penelitian skripsi:

Analisis Pola Transaksi Shopee Food Menggunakan
Metode K-Means Clustering Berdasarkan Data
Pemesanan pada Toko Buffet The Padang Pasir.
""")
