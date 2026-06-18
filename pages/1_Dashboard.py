import streamlit as st
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
Selamat datang pada aplikasi **Analisis Pola Transaksi Shopee Food Menggunakan Metode K-Means Clustering**.

Dashboard ini menampilkan ringkasan data transaksi dan hasil analisis yang digunakan dalam penelitian.
""")

st.divider()

# =====================================================
# JIKA DATABASE KOSONG
# =====================================================

if df.empty:

    st.warning(
        "⚠️ Database masih kosong. Silakan tambahkan data pada menu **Kelola Data**."
    )

    st.stop()

# =====================================================
# METRIC
# =====================================================

total_transaksi = len(df)

total_omzet = df["Total_harga"].sum()

total_item = df["Jumlah_pesanan"].sum()

rata_harga = df["rata_rata_harga"].mean()

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "📦 Total Transaksi",
    f"{total_transaksi:,}"
)

c2.metric(
    "💰 Total Omzet",
    f"Rp {total_omzet:,.0f}"
)

c3.metric(
    "🛒 Total Item",
    f"{int(total_item):,}"
)

c4.metric(
    "📈 Rata-rata Harga",
    f"Rp {rata_harga:,.0f}"
)

st.divider()

# =====================================================
# GRAFIK 1
# =====================================================

kiri, kanan = st.columns(2)

with kiri:

    st.subheader("💰 Distribusi Total Harga")

    fig1 = px.histogram(

        df,

        x="Total_harga",

        nbins=25,

        title="Distribusi Total Harga"

    )

    st.plotly_chart(

        fig1,

        use_container_width=True

    )

with kanan:

    st.subheader("🛒 Distribusi Jumlah Pesanan")

    fig2 = px.histogram(

        df,

        x="Jumlah_pesanan",

        nbins=15,

        title="Distribusi Jumlah Pesanan"

    )

    st.plotly_chart(

        fig2,

        use_container_width=True

    )

st.divider()

# =====================================================
# PREVIEW DATA
# =====================================================

st.subheader("📋 Preview Data")

st.dataframe(

    df.head(10),

    use_container_width=True,

    hide_index=True

)

st.divider()

# =====================================================
# INFORMASI CLUSTER
# =====================================================

st.subheader("🎯 Interpretasi Cluster")

col1, col2, col3 = st.columns(3)

with col1:

    st.success("""
### 🟢 Cluster 1

**Pola Pemesanan Personal**

Jumlah pesanan relatif sedikit dan
mencerminkan kebutuhan individu.
""")

with col2:

    st.info("""
### 🔵 Cluster 2

**Pola Pemesanan Reguler**

Karakteristik transaksi sedang dan
mencerminkan pola pembelian rutin.
""")

with col3:

    st.warning("""
### 🟣 Cluster 3

**Pola Pemesanan Kelompok**

Jumlah pesanan relatif tinggi dan
umumnya dilakukan secara bersama.
""")
