import streamlit as st
import pandas as pd
import plotly.express as px

from utils.database import get_all_data

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

df = get_all_data()

st.title("📊 Dashboard Analisis Shopee Food")
st.markdown("""
Selamat datang di aplikasi **Analisis Pola Transaksi Shopee Food Menggunakan Metode K-Means Clustering**
berdasarkan data pemesanan pada **Buffet The Padang Pasir**.

Dashboard ini menyajikan ringkasan data transaksi, statistik, visualisasi,
serta status proses clustering.
""")

st.divider()

# =====================================================
# VALIDASI DATA
# =====================================================

if df.empty:
    st.warning("⚠️ Database masih kosong. Silakan tambahkan data pada menu **Kelola Data**.")
    st.stop()

# =====================================================
# KONVERSI TIPE DATA
# =====================================================

df["Total_harga"] = pd.to_numeric(df["Total_harga"], errors="coerce")
df["Jumlah_pesanan"] = pd.to_numeric(df["Jumlah_pesanan"], errors="coerce")
df["rata_rata_harga"] = pd.to_numeric(df["rata_rata_harga"], errors="coerce")

# =====================================================
# METRIC
# =====================================================

total_transaksi = len(df)
total_omzet = df["Total_harga"].sum()
total_item = df["Jumlah_pesanan"].sum()
rata_harga = df["rata_rata_harga"].mean()

status_cluster = (
    "✅ Sudah Diproses"
    if "hasil_cluster" in st.session_state
    else "❌ Belum Diproses"
)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "📦 Total Transaksi",
        f"{total_transaksi:,}"
    )

with col2:
    st.metric(
        "💰 Total Omzet",
        f"Rp {total_omzet:,.0f}"
    )

with col3:
    st.metric(
        "🛒 Total Pesanan",
        f"{int(total_item):,}"
    )

with col4:
    st.metric(
        "📈 Rata-rata Harga",
        f"Rp {rata_harga:,.0f}"
    )

with col5:
    st.metric(
        "🤖 Status Clustering",
        status_cluster
    )

st.divider()

# =====================================================
# GRAFIK
# =====================================================

col_chart1, col_chart2 = st.columns(2)

with col_chart1:

    st.subheader("Distribusi Total Harga")

    fig_total = px.histogram(
        df,
        x="Total_harga",
        nbins=20,
        title="Distribusi Total Harga"
    )

    st.plotly_chart(
        fig_total,
        use_container_width=True
    )

with col_chart2:

    st.subheader("Distribusi Jumlah Pesanan")

    fig_jumlah = px.histogram(
        df,
        x="Jumlah_pesanan",
        nbins=15,
        title="Distribusi Jumlah Pesanan"
    )

    st.plotly_chart(
        fig_jumlah,
        use_container_width=True
    )

st.divider()

# =====================================================
# DISTRIBUSI CLUSTER
# =====================================================

st.subheader("📊 Distribusi Cluster")

if "cluster_summary" in st.session_state:

    summary = st.session_state["cluster_summary"]

    fig_cluster = px.pie(
        summary,
        names="Interpretasi",
        values="Jumlah Data",
        hole=0.45,
        title="Distribusi Hasil Clustering"
    )

    st.plotly_chart(
        fig_cluster,
        use_container_width=True
    )

else:

    st.info(
        "Belum ada hasil clustering. Jalankan proses pada menu **K-Means**."
    )

st.divider()

# =====================================================
# PREVIEW DATA
# =====================================================

st.subheader("📋 Preview 10 Data Terbaru")

if "id" in df.columns:

    preview = (
        df.sort_values(
            by="id",
            ascending=False
        )
        .head(10)
    )

else:

    preview = df.tail(10)

st.dataframe(
    preview,
    use_container_width=True,
    hide_index=True
)

st.divider()

# =====================================================
# INFORMASI PENELITIAN
# =====================================================

st.subheader("🎯 Interpretasi Cluster")

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.success("""
### 🟢 Cluster 1

**Pola Pemesanan Personal**

Karakteristik:
- Total harga relatif rendah
- Jumlah pesanan sedikit
- Umumnya untuk konsumsi individu
""")

with col_b:
    st.info("""
### 🔵 Cluster 2

**Pola Pemesanan Reguler**

Karakteristik:
- Nilai transaksi sedang
- Jumlah pesanan sedang
- Mewakili pola pembelian rutin
""")

with col_c:
    st.warning("""
### 🟣 Cluster 3

**Pola Pemesanan Kelompok**

Karakteristik:
- Total harga tinggi
- Jumlah pesanan banyak
- Umumnya untuk kebutuhan bersama
""")

st.divider()

# =====================================================
# METODE PENELITIAN
# =====================================================

st.subheader("📚 Informasi Metode")

st.markdown("""
- **Metode Clustering** : K-Means Clustering
- **Jumlah Cluster (K)** : 3
- **Metode Evaluasi** : Elbow Method dan Silhouette Score
- **Variabel yang Digunakan** :
  - `Total_harga`
  - `Jumlah_pesanan`
  - `rata_rata_harga`
  - `waktu_persiapan_digunakan`
""")

st.caption(
    "Aplikasi ini dikembangkan untuk mendukung penelitian skripsi "
    "Analisis Pola Transaksi Shopee Food Menggunakan Metode K-Means Clustering "
    "Berdasarkan Data Pemesanan pada Toko Buffet The Padang Pasir."
)
