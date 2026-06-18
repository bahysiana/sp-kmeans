import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Hasil Clustering",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Hasil Clustering")
st.caption(
    "Menampilkan hasil analisis K-Means Clustering pada data transaksi Shopee Food."
)

st.divider()

# =====================================================
# CEK HASIL CLUSTERING
# =====================================================

if "hasil_cluster" not in st.session_state:

    st.warning(
        "⚠️ Belum ada hasil clustering. Silakan jalankan proses K-Means terlebih dahulu."
    )

    st.stop()

# =====================================================
# AMBIL DATA DARI SESSION
# =====================================================

hasil = st.session_state["hasil_cluster"]
summary = st.session_state["cluster_summary"]
statistik = st.session_state["cluster_statistics"]
centroid = st.session_state["centroid"]

# =====================================================
# METRIC
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📦 Total Data",
        len(hasil)
    )

with col2:
    st.metric(
        "🤖 Jumlah Cluster",
        3
    )

with col3:
    st.metric(
        "✅ Status",
        "Selesai"
    )

st.divider()

# =====================================================
# TABEL HASIL
# =====================================================

st.subheader("📋 Data Hasil Clustering")

st.dataframe(
    hasil,
    use_container_width=True,
    hide_index=True
)

st.divider()

# =====================================================
# RINGKASAN CLUSTER
# =====================================================

st.subheader("📊 Ringkasan Cluster")

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

fig_bar = px.bar(
    summary,
    x="Interpretasi",
    y="Jumlah Data",
    color="Interpretasi",
    text="Jumlah Data",
    title="Distribusi Anggota Cluster"
)

st.plotly_chart(
    fig_bar,
    use_container_width=True
)

st.divider()

# =====================================================
# VISUALISASI SCATTER
# =====================================================

st.subheader("📈 Visualisasi Cluster")

fig_scatter = px.scatter(
    hasil,
    x="Total_harga",
    y="Jumlah_pesanan",
    color="Interpretasi",
    hover_data=[
        "username",
        "menu_yang_dibeli"
    ],
    title="Visualisasi Cluster berdasarkan Total Harga dan Jumlah Pesanan"
)

st.plotly_chart(
    fig_scatter,
    use_container_width=True
)

st.divider()

# =====================================================
# STATISTIK CLUSTER
# =====================================================

st.subheader("📑 Statistik Tiap Cluster")

st.dataframe(
    statistik,
    use_container_width=True,
    hide_index=True
)

st.divider()

# =====================================================
# CENTROID
# =====================================================

st.subheader("📍 Nilai Centroid")

centroid_df = pd.DataFrame(
    centroid,
    columns=[
        "Total_harga",
        "Jumlah_pesanan",
        "rata_rata_harga",
        "waktu_persiapan_digunakan"
    ]
)

centroid_df.index = [
    "Cluster 1",
    "Cluster 2",
    "Cluster 3"
]

st.dataframe(
    centroid_df,
    use_container_width=True
)

st.divider()

# =====================================================
# INTERPRETASI
# =====================================================

st.subheader("📝 Interpretasi Hasil")

st.success("""
### 🟢 Cluster 1 - Pola Pemesanan Personal

Kelompok transaksi dengan karakteristik jumlah pesanan
dan total harga relatif rendah sehingga mencerminkan
pola pemesanan untuk kebutuhan individu atau personal.
""")

st.info("""
### 🔵 Cluster 2 - Pola Pemesanan Reguler

Kelompok transaksi dengan karakteristik jumlah pesanan
dan total harga sedang yang menggambarkan pola
pemesanan rutin pelanggan.
""")

st.warning("""
### 🟣 Cluster 3 - Pola Pemesanan Kelompok

Kelompok transaksi dengan karakteristik jumlah pesanan
dan total harga relatif tinggi sehingga umumnya
merepresentasikan pemesanan untuk kebutuhan bersama
atau dalam jumlah besar.
""")

st.divider()

# =====================================================
# KESIMPULAN
# =====================================================

st.subheader("📚 Kesimpulan")

st.markdown("""
Berdasarkan hasil proses **K-Means Clustering** dengan
jumlah cluster sebanyak **3**, data transaksi Shopee Food
berhasil dikelompokkan menjadi:

- 🟢 **Pola Pemesanan Personal**
- 🔵 **Pola Pemesanan Reguler**
- 🟣 **Pola Pemesanan Kelompok**

Pengelompokan ini dapat digunakan sebagai dasar
analisis perilaku pelanggan dan membantu pengambilan
keputusan dalam strategi pelayanan maupun pemasaran.
""")
