import streamlit as st
from pathlib import Path

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
# HEADER
# =====================================================

st.title("🍽️ Analisis Pola Transaksi Shopee Food")
st.subheader("Menggunakan Metode K-Means Clustering")

st.markdown("""
## Selamat Datang 👋

Aplikasi ini dikembangkan untuk mendukung penelitian skripsi:

### **ANALISIS POLA TRANSAKSI SHOPEE FOOD MENGGUNAKAN METODE K-MEANS CLUSTERING BERDASARKAN DATA PEMESANAN PADA TOKO BUFFET THE PADANG PASIR**

Melalui aplikasi ini, pengguna dapat:

- 📂 Mengelola data transaksi (CRUD)
- 📤 Mengimpor dataset dari file CSV
- 🧹 Melakukan preprocessing data
- 🤖 Menjalankan algoritma K-Means Clustering
- 📊 Melihat hasil clustering dan visualisasi
- 📥 Mengunduh hasil analisis dalam format CSV
""")

st.divider()

# =====================================================
# ALUR PENGGUNAAN
# =====================================================

st.header("🚀 Alur Penggunaan Aplikasi")

st.markdown("""
Ikuti langkah-langkah berikut:

### 1️⃣ Dashboard
Melihat ringkasan data dan statistik aplikasi.

### 2️⃣ Kelola Data
- Tambah data transaksi
- Edit data
- Hapus data
- Import dataset CSV

### 3️⃣ Preprocessing
Melakukan normalisasi data menggunakan **StandardScaler**.

### 4️⃣ K-Means Clustering
Menjalankan proses clustering dengan **K = 3**.

### 5️⃣ Hasil
Melihat hasil cluster, statistik, centroid, dan interpretasi.

### 6️⃣ Download
Mengunduh hasil analisis dalam format CSV.

### 7️⃣ Tentang
Melihat informasi aplikasi dan penelitian.
""")

st.divider()

# =====================================================
# INTERPRETASI CLUSTER
# =====================================================

st.header("📊 Interpretasi Cluster")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
### 🟢 Cluster 1

**Pola Pemesanan Personal**

- Total harga relatif rendah
- Jumlah pesanan sedikit
- Umumnya untuk kebutuhan individu
""")

with col2:
    st.info("""
### 🔵 Cluster 2

**Pola Pemesanan Reguler**

- Nilai transaksi sedang
- Jumlah pesanan sedang
- Pola pembelian rutin pelanggan
""")

with col3:
    st.warning("""
### 🟣 Cluster 3

**Pola Pemesanan Kelompok**

- Total harga relatif tinggi
- Jumlah pesanan lebih banyak
- Umumnya untuk kebutuhan bersama
""")

st.divider()

# =====================================================
# INFORMASI TEKNOLOGI
# =====================================================

st.header("🛠️ Teknologi yang Digunakan")

st.markdown("""
- 🐍 Python
- 🌐 Streamlit
- 🗄️ SQLite
- 📊 Pandas
- 🤖 Scikit-learn
- 📈 Plotly
""")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "© 2026 | Aplikasi Pendukung Skripsi - Analisis Pola Transaksi Shopee Food Menggunakan Metode K-Means Clustering"
)
