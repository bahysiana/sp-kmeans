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
# MEMBUAT DATABASE
# =====================================================

create_table()

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    # Logo
    st.image(
        "assets/tes.png",
        width=120
    )

    st.markdown("## 🍽️ Shopee Food Analytics")

    st.caption(
        "Analisis Pola Transaksi Menggunakan Metode K-Means Clustering"
    )

    st.divider()

    st.markdown("""
### 📚 Metode

- 🤖 K-Means Clustering
- 📊 StandardScaler
- 📈 Elbow Method
- 📉 Silhouette Score
""")

    st.divider()

    st.markdown("""
### 🎯 Interpretasi Cluster

🟢 **Cluster 1**
- Pola Pemesanan Personal

🔵 **Cluster 2**
- Pola Pemesanan Reguler

🟣 **Cluster 3**
- Pola Pemesanan Kelompok
""")

    st.divider()

    st.info("""
👨‍🎓 **Penelitian Skripsi**

Analisis Pola Transaksi Shopee Food Menggunakan Metode K-Means Clustering Berdasarkan Data Pemesanan pada Toko Buffet The Padang Pasir.
""")

    st.divider()

    st.caption(
        "© 2026 | Universitas Putra Indonesia YPTK Padang"
    )

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div style="
padding:30px;
border-radius:20px;
background:linear-gradient(90deg,#2563eb,#4f46e5);
color:white;
text-align:center;
margin-bottom:25px;
box-shadow:0 8px 20px rgba(37,99,235,0.25);
">

<h1>🍽️ Analisis Pola Transaksi Shopee Food</h1>

<h3>Menggunakan Metode K-Means Clustering</h3>

<p style="font-size:20px;">
Buffet The Padang Pasir
</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# DESKRIPSI
# =====================================================

st.markdown("""
# 👋 Selamat Datang

Aplikasi ini dikembangkan sebagai media analisis untuk penelitian skripsi.

### Judul Penelitian

**ANALISIS POLA TRANSAKSI SHOPEE FOOD MENGGUNAKAN METODE K-MEANS CLUSTERING BERDASARKAN DATA PEMESANAN PADA TOKO BUFFET THE PADANG PASIR**

Melalui aplikasi ini pengguna dapat:

- 📂 Mengelola data transaksi
- 📤 Mengimpor dataset CSV
- 🧹 Melakukan preprocessing data
- 🤖 Menjalankan algoritma K-Means Clustering
- 📊 Melihat hasil analisis dan visualisasi
- 📥 Mengunduh hasil clustering
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
- K-Means Clustering
- 3 Cluster
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
# ALUR
# =====================================================

st.subheader("🚀 Alur Penggunaan")

st.markdown("""
1. 📤 Tambahkan atau impor data transaksi.
2. 🧹 Lakukan preprocessing menggunakan StandardScaler.
3. 🤖 Jalankan proses K-Means Clustering.
4. 📊 Analisis hasil pengelompokan data.
5. 📥 Unduh hasil analisis jika diperlukan.
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

- Jumlah pesanan relatif sedikit
- Total harga relatif rendah
- Umumnya untuk kebutuhan individu
""")

with c2:
    st.info("""
### 🔵 Cluster 2

**Pola Pemesanan Reguler**

- Jumlah pesanan sedang
- Nilai transaksi menengah
- Mewakili pola pembelian rutin
""")

with c3:
    st.warning("""
### 🟣 Cluster 3

**Pola Pemesanan Kelompok**

- Jumlah pesanan lebih banyak
- Total harga relatif tinggi
- Umumnya dilakukan untuk kebutuhan bersama
""")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "© 2026 | Aplikasi Analisis Pola Transaksi Shopee Food | Python • Streamlit • SQLite • Scikit-learn • Plotly"
)
