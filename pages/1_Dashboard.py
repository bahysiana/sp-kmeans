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

# =====================================================
# HEADER
# =====================================================

st.title("📊 Dashboard Analisis Shopee Food")

st.caption(
    "Ringkasan data transaksi dan visualisasi hasil analisis menggunakan metode K-Means Clustering."
)

st.divider()

# =====================================================
# DATABASE KOSONG
# =====================================================

if df.empty:

    st.warning(
        "⚠️ Database masih kosong. Silakan tambahkan data pada menu Kelola Data."
    )

    st.stop()

# =====================================================
# METRIC
# =====================================================

total_transaksi = len(df)

total_omzet = df["Total_harga"].sum()

total_item = df["Jumlah_pesanan"].sum()

rata_harga = df["rata_rata_harga"].mean()

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric(
        "📦 Total Transaksi",
        f"{total_transaksi:,}"
    )

with m2:
    st.metric(
        "💰 Total Omzet",
        f"Rp {total_omzet:,.0f}"
    )

with m3:
    st.metric(
        "🛒 Total Item",
        f"{int(total_item):,}"
    )

with m4:
    st.metric(
        "📈 Rata-rata Harga",
        f"Rp {rata_harga:,.0f}"
    )

st.divider()

# =====================================================
# GRAFIK
# =====================================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("💰 Distribusi Total Harga")

    fig_total = px.histogram(
        df,
        x="Total_harga",
        nbins=20
    )

    st.plotly_chart(
        fig_total,
        use_container_width=True
    )

with col2:

    st.subheader("🛒 Distribusi Jumlah Pesanan")

    fig_jumlah = px.histogram(
        df,
        x="Jumlah_pesanan",
        nbins=15
    )

    st.plotly_chart(
        fig_jumlah,
        use_container_width=True
    )

st.divider()

# =====================================================
# DISTRIBUSI CLUSTER
# =====================================================

st.subheader("🤖 Distribusi Cluster")

if "cluster_summary" in st.session_state:

    summary = st.session_state["cluster_summary"]

    fig_cluster = px.pie(
        summary,
        names="Interpretasi",
        values="Jumlah Data",
        hole=0.45
    )

    st.plotly_chart(
        fig_cluster,
        use_container_width=True
    )

else:

    st.info(
        "Silakan jalankan proses K-Means terlebih dahulu untuk melihat distribusi cluster."
    )

st.divider()

# =====================================================
# PREVIEW DATA
# =====================================================

st.subheader("📋 Preview Data Transaksi")

st.dataframe(
    df.head(10),
    use_container_width=True,
    hide_index=True
)

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

- Jumlah pesanan relatif sedikit.
- Total harga relatif rendah.
- Umumnya untuk kebutuhan individu.
""")

with c2:

    st.info("""
### 🔵 Cluster 2

**Pola Pemesanan Reguler**

- Karakteristik transaksi sedang.
- Mencerminkan pola pembelian rutin.
- Aktivitas pelanggan reguler.
""")

with c3:

    st.warning("""
### 🟣 Cluster 3

**Pola Pemesanan Kelompok**

- Jumlah pesanan relatif tinggi.
- Total transaksi lebih besar.
- Umumnya dilakukan untuk kebutuhan bersama.
""")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "© 2026 | Dashboard Analisis Shopee Food Menggunakan Metode K-Means Clustering"
)
