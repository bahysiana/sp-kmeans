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
# MEMBUAT DATABASE
# =====================================================

create_table()

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown(
        """
        <h1 style="text-align:center;">
            🍽️
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h2 style="text-align:center;">
            Shopee Food Analytics
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="text-align:center;">
            Analisis Pola Transaksi<br>
            Menggunakan Metode<br>
            <b>K-Means Clustering</b>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 📚 Metode")

    st.markdown("""
- 🤖 K-Means Clustering
- 📊 StandardScaler
- 📈 Elbow Method
- 📉 Silhouette Score
""")

    st.divider()

    st.markdown("### 🎯 Interpretasi Cluster")

    st.success("""
🟢 Cluster 1

Pola Pemesanan Personal
""")

    st.info("""
🔵 Cluster 2

Pola Pemesanan Reguler
""")

    st.warning("""
🟣 Cluster 3

Pola Pemesanan Kelompok
""")

    st.divider()

    st.info("""
**Penelitian Skripsi**

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
padding:25px;
border-radius:18px;
background:linear-gradient(90deg,#2563eb,#4f46e5);
color:white;
text-align:center;
margin-bottom:20px;
">

<h1>🍽️ Analisis Pola Transaksi Shopee Food</h1>

<h3>Menggunakan Metode K-Means Clustering</h3>

<p style="font-size:18px;">
Buffet The Padang Pasir
</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# DESKRIPSI
# =====================================================

st.markdown("""
# 👋 Selamat Datang

Aplikasi ini merupakan implementasi penelitian skripsi yang bertujuan
menganalisis pola transaksi pelanggan Shopee Food menggunakan algoritma
**K-Means Clustering**.

### 📖 Judul Penelitian

**ANALISIS POLA TRANSAKSI SHOPEE FOOD MENGGUNAKAN METODE K-MEANS CLUSTERING BERDASARKAN DATA PEMESANAN PADA TOKO BUFFET THE PADANG PASIR**

### 🚀 Fitur Utama

- 📂 Kelola Data Transaksi
- 📤 Import Dataset CSV
- 🧹 Preprocessing Data
- 🤖 K-Means Clustering
- 📊 Visualisasi Hasil
- 📥 Download Hasil Analisis
""")

st.divider()

# =====================================================
# FITUR UTAMA
# =====================================================

st.subheader("✨ Fitur Aplikasi")

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

- StandardScaler
- K-Means Clustering
- K = 3
- Clustering Otomatis
""")

with col3:
    st.warning("""
### 📊 Visualisasi

- Dashboard
- Grafik Interaktif
- Hasil Cluster
- Download CSV
""")

st.divider()

# =====================================================
# ALUR PENGGUNAAN
# =====================================================

st.subheader("🚀 Alur Penggunaan Aplikasi")

st.markdown("""
Ikuti langkah-langkah berikut untuk menggunakan aplikasi:

1. 📂 Masuk ke menu **Kelola Data** dan tambahkan data atau impor file CSV.
2. 🧹 Buka menu **Preprocessing** untuk melakukan normalisasi data menggunakan **StandardScaler**.
3. 🤖 Masuk ke menu **K-Means Clustering** dan jalankan proses clustering dengan **K = 3**.
4. 📊 Lihat hasil pengelompokan pada menu **Hasil** beserta visualisasi yang tersedia.
5. 📥 Unduh hasil analisis melalui menu **Download** apabila diperlukan.
""")

st.divider()

# =====================================================
# INTERPRETASI CLUSTER
# =====================================================

st.subheader("🎯 Interpretasi Hasil Cluster")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
### 🟢 Cluster 1

**Pola Pemesanan Personal**

- Jumlah pesanan relatif sedikit
- Total transaksi relatif rendah
- Umumnya untuk kebutuhan individu
""")

with col2:
    st.info("""
### 🔵 Cluster 2

**Pola Pemesanan Reguler**

- Jumlah pesanan sedang
- Nilai transaksi menengah
- Mencerminkan pola pembelian rutin pelanggan
""")

with col3:
    st.warning("""
### 🟣 Cluster 3

**Pola Pemesanan Kelompok**

- Jumlah pesanan lebih banyak
- Total transaksi relatif tinggi
- Umumnya dilakukan untuk kebutuhan bersama
""")

st.divider()

# =====================================================
# TIPS PENGGUNAAN
# =====================================================

st.subheader("💡 Tips Penggunaan")

st.info("""
Untuk memperoleh hasil clustering yang optimal:

- Pastikan data transaksi sudah lengkap.
- Gunakan menu **Preprocessing** sebelum menjalankan K-Means.
- Nilai **K** telah ditetapkan menjadi **3** sesuai metodologi penelitian.
- Analisis hasil cluster pada menu **Hasil** untuk melihat karakteristik masing-masing kelompok transaksi.
""")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:gray; font-size:14px;">
        © 2026 <b>Analisis Pola Transaksi Shopee Food</b><br>
        Metode K-Means Clustering • Python • Streamlit • SQLite • Plotly • Scikit-learn
    </div>
    """,
    unsafe_allow_html=True
)
