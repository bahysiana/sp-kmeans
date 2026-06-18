import streamlit as st

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Tentang Aplikasi",
    page_icon="ℹ️",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

st.title("ℹ️ Tentang Aplikasi")
st.caption(
    "Informasi mengenai aplikasi dan penelitian skripsi."
)

st.divider()

# =====================================================
# DESKRIPSI APLIKASI
# =====================================================

st.header("📌 Deskripsi")

st.markdown("""
Aplikasi ini dikembangkan untuk mendukung penelitian skripsi yang berjudul:

### **ANALISIS POLA TRANSAKSI SHOPEE FOOD MENGGUNAKAN METODE K-MEANS CLUSTERING BERDASARKAN DATA PEMESANAN PADA TOKO BUFFET THE PADANG PASIR**

Tujuan utama aplikasi adalah membantu menganalisis pola transaksi pelanggan berdasarkan data pemesanan Shopee Food menggunakan algoritma **K-Means Clustering** sehingga dapat memberikan informasi yang berguna bagi pengambilan keputusan.
""")

st.divider()

# =====================================================
# METODE
# =====================================================

st.header("🤖 Metode yang Digunakan")

st.markdown("""
Aplikasi ini menggunakan metode **K-Means Clustering** dengan jumlah cluster sebanyak **3**.

Tahapan analisis meliputi:

1. Pengumpulan data transaksi.
2. Penyimpanan data ke database SQLite.
3. Preprocessing menggunakan **StandardScaler**.
4. Proses clustering menggunakan algoritma K-Means.
5. Evaluasi menggunakan:
   - Elbow Method
   - Silhouette Score
6. Visualisasi dan interpretasi hasil clustering.
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
- Mencerminkan kebutuhan individu
""")

with col2:
    st.info("""
### 🔵 Cluster 2

**Pola Pemesanan Reguler**

- Nilai transaksi sedang
- Jumlah pesanan sedang
- Mencerminkan pola pembelian rutin
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
# FITUR YANG DIGUNAKAN
# =====================================================

st.header("📈 Variabel Clustering")

st.markdown("""
Empat variabel yang digunakan dalam proses K-Means adalah:

- 💰 **Total_harga**
- 🛒 **Jumlah_pesanan**
- 📊 **rata_rata_harga**
- ⏱️ **waktu_persiapan_digunakan**

Seluruh variabel dinormalisasi menggunakan **StandardScaler** sebelum proses clustering dilakukan.
""")

st.divider()

# =====================================================
# FITUR APLIKASI
# =====================================================

st.header("✨ Fitur Aplikasi")

st.markdown("""
Aplikasi menyediakan fitur-fitur berikut:

- 📂 Kelola data transaksi (CRUD)
- 📤 Import dataset CSV
- 🧹 Preprocessing data
- 🤖 K-Means Clustering
- 📊 Visualisasi hasil
- 📈 Statistik cluster
- 📥 Download hasil analisis dalam format CSV
""")

st.divider()

# =====================================================
# KESIMPULAN
# =====================================================

st.header("📚 Kesimpulan")

st.markdown("""
Melalui aplikasi ini, data transaksi Shopee Food dapat dikelompokkan menjadi tiga pola utama:

- 🟢 **Pola Pemesanan Personal**
- 🔵 **Pola Pemesanan Reguler**
- 🟣 **Pola Pemesanan Kelompok**

Hasil pengelompokan diharapkan dapat membantu pihak **Buffet The Padang Pasir** dalam memahami karakteristik transaksi pelanggan dan mendukung pengambilan keputusan berbasis data.
""")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "Dikembangkan sebagai aplikasi pendukung penelitian skripsi menggunakan Python, Streamlit, SQLite, dan Scikit-learn."
)
