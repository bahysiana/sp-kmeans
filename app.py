```python
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
🟢 **Cluster 1**

Pola Pemesanan Personal
""")

    st.info("""
🔵 **Cluster 2**

Pola Pemesanan Reguler
""")

    st.warning("""
🟣 **Cluster 3**

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
# HERO
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

### ANALISIS POLA TRANSAKSI SHOPEE FOOD MENGGUNAKAN METODE K-MEANS CLUSTERING BERDASARKAN DATA PEMESANAN PADA TOKO BUFFET THE PADANG PASIR

Melalui aplikasi ini pengguna dapat:

- 📂 Mengelola data transaksi
- 📤 Mengimpor dataset CSV
- 🧹 Melakukan preprocessing
- 🤖 Menjalankan K-Means Clustering
- 📊 Melihat hasil clustering
- 📥 Mengunduh hasil analisis
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

- StandardScaler
- K-Means
- K = 3
- Clustering
""")

with col3:
    st.warning("""
### 📊 Visualisasi

- Dashboard
- Grafik
- Hasil
- Download
""")

st.divider()

# =====================================================
# ALUR
# =====================================================

st.subheader("🚀 Alur Penggunaan")

st.markdown("""
1. Tambahkan atau import data transaksi.

2. Jalankan preprocessing menggunakan StandardScaler.

3. Jalankan proses K-Means Clustering.

4. Analisis hasil pengelompokan data.

5. Download hasil clustering apabila diperlukan.
""")

st.divider()

# =====================================================
# INTERPRETASI
# =====================================================

st.subheader("🎯 Interpretasi Cluster")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("""
### 🟢 Cluster 1

Pola Pemesanan Personal

- Jumlah pesanan rendah
- Total harga rendah
- Konsumsi individu
""")

with c2:
    st.info("""
### 🔵 Cluster 2

Pola Pemesanan Reguler

- Jumlah pesanan sedang
- Pembelian rutin
- Transaksi menengah
""")

with c3:
    st.warning("""
### 🟣 Cluster 3

Pola Pemesanan Kelompok

- Jumlah pesanan tinggi
- Total harga tinggi
- Kebutuhan bersama
""")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "© 2026 | Python • Streamlit • SQLite • Plotly • Scikit-learn"
)
```
