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
# MEMBUAT DATABASE JIKA BELUM ADA
# =====================================================

create_table()

# =====================================================
# LOAD CSS
# =====================================================

css_file = Path("assets/style.css")

if css_file.exists():
    with open(css_file, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div style="
background: linear-gradient(135deg,#2563EB,#7C3AED);
padding:40px;
border-radius:20px;
color:white;
text-align:center;
margin-bottom:30px;
box-shadow:0 8px 25px rgba(0,0,0,0.15);
">

<h1>🍽️ Analisis Pola Transaksi Shopee Food</h1>

<h3>Menggunakan Metode K-Means Clustering</h3>

<p style="font-size:18px;">
Buffet The Padang Pasir
</p>

</div>
""", unsafe_allow_html=True)
# =====================================================
# DESKRIPSI APLIKASI
# =====================================================

st.markdown("""
## 👋 Selamat Datang

Aplikasi ini dikembangkan sebagai media pendukung penelitian skripsi dengan judul:

**ANALISIS POLA TRANSAKSI SHOPEE FOOD MENGGUNAKAN METODE K-MEANS CLUSTERING BERDASARKAN DATA PEMESANAN PADA TOKO BUFFET THE PADANG PASIR**

Melalui aplikasi ini, pengguna dapat mengelola data transaksi, melakukan preprocessing,
menjalankan algoritma K-Means Clustering, melihat hasil pengelompokan, serta mengunduh
hasil analisis.
""")

st.divider()

# =====================================================
# FITUR UTAMA
# =====================================================

st.subheader("✨ Fitur Utama Aplikasi")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="
        background:#ffffff;
        padding:20px;
        border-radius:15px;
        box-shadow:0 4px 12px rgba(0,0,0,0.08);
        height:220px;
    ">
        <h3>📂 Kelola Data</h3>
        <hr>
        <p>
        • Tambah Data<br>
        • Edit Data<br>
        • Hapus Data<br>
        • Import CSV
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background:#ffffff;
        padding:20px;
        border-radius:15px;
        box-shadow:0 4px 12px rgba(0,0,0,0.08);
        height:220px;
    ">
        <h3>🤖 K-Means Clustering</h3>
        <hr>
        <p>
        • StandardScaler<br>
        • K = 3 Cluster<br>
        • Euclidean Distance<br>
        • Centroid Update
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        background:#ffffff;
        padding:20px;
        border-radius:15px;
        box-shadow:0 4px 12px rgba(0,0,0,0.08);
        height:220px;
    ">
        <h3>📊 Visualisasi</h3>
        <hr>
        <p>
        • Dashboard<br>
        • Grafik Interaktif<br>
        • Hasil Cluster<br>
        • Download CSV
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
# =====================================================
# ALUR PENGGUNAAN
# =====================================================

st.subheader("🚀 Alur Penggunaan Aplikasi")

st.markdown("""
1. 📂 **Kelola Data** → Tambahkan data transaksi atau impor file CSV.
2. 🧹 **Preprocessing** → Lakukan normalisasi data menggunakan StandardScaler.
3. 🤖 **K-Means** → Jalankan proses clustering dengan jumlah cluster **K = 3**.
4. 📊 **Hasil** → Lihat visualisasi, centroid, dan interpretasi cluster.
5. 📥 **Download** → Unduh hasil analisis dalam format CSV.
""")

st.divider()

# =====================================================
# INTERPRETASI CLUSTER
# =====================================================

st.subheader("🎯 Interpretasi Cluster")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="
        background:#dcfce7;
        padding:20px;
        border-radius:15px;
        border-left:6px solid #22c55e;
        height:220px;
    ">
        <h3>🟢 Cluster 1</h3>
        <h4>Pola Pemesanan Personal</h4>
        <ul>
            <li>Jumlah pesanan relatif sedikit</li>
            <li>Total harga cenderung rendah</li>
            <li>Umumnya untuk konsumsi individu</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background:#dbeafe;
        padding:20px;
        border-radius:15px;
        border-left:6px solid #2563eb;
        height:220px;
    ">
        <h3>🔵 Cluster 2</h3>
        <h4>Pola Pemesanan Reguler</h4>
        <ul>
            <li>Jumlah pesanan sedang</li>
            <li>Nilai transaksi menengah</li>
            <li>Mewakili pelanggan dengan pembelian rutin</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        background:#f3e8ff;
        padding:20px;
        border-radius:15px;
        border-left:6px solid #9333ea;
        height:220px;
    ">
        <h3>🟣 Cluster 3</h3>
        <h4>Pola Pemesanan Kelompok</h4>
        <ul>
            <li>Jumlah pesanan lebih banyak</li>
            <li>Total transaksi relatif tinggi</li>
            <li>Umumnya dilakukan untuk kebutuhan bersama</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =====================================================
# INFORMASI TEKNOLOGI
# =====================================================

st.subheader("🛠️ Teknologi yang Digunakan")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.metric("🐍 Bahasa", "Python")
tech2.metric("🌐 Framework", "Streamlit")
tech3.metric("🗄️ Database", "SQLite")
tech4.metric("🤖 Machine Learning", "Scikit-learn")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div style="
text-align:center;
padding:20px;
color:#6b7280;
font-size:14px;
">
<hr>
<b>Analisis Pola Transaksi Shopee Food Menggunakan Metode K-Means Clustering</b><br>
Universitas Putra Indonesia YPTK Padang<br>
© 2026
</div>
""", unsafe_allow_html=True)
