import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Hasil Clustering",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Hasil Clustering")
st.caption(
    "Menampilkan hasil akhir proses K-Means Clustering."
)

st.divider()

# =====================================================
# CEK HASIL
# =====================================================

if "hasil_cluster" not in st.session_state:

    st.warning(
        "⚠️ Silakan jalankan proses K-Means terlebih dahulu."
    )

    st.stop()

hasil = st.session_state["hasil_cluster"]

summary = st.session_state["cluster_summary"]

centroid = st.session_state["centroid"]

# =====================================================
# METRIC
# =====================================================

c1, c2, c3 = st.columns(3)

c1.metric(
    "Jumlah Data",
    len(hasil)
)

c2.metric(
    "Jumlah Cluster",
    3
)

c3.metric(
    "Interpretasi",
    "3 Kelompok"
)

st.divider()

# =====================================================
# TABEL HASIL
# =====================================================

st.subheader("📋 Dataset Hasil Clustering")

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

# =====================================================
# BAR CHART
# =====================================================

fig_bar = px.bar(

    summary,

    x="Interpretasi",

    y="Jumlah Data",

    color="Interpretasi",

    text="Jumlah Data"

)

st.plotly_chart(

    fig_bar,

    use_container_width=True

)

st.divider()

# =====================================================
# SCATTER PLOT
# =====================================================

st.subheader("🔵 Visualisasi Cluster")

fig_scatter = px.scatter(

    hasil,

    x="Total_harga",

    y="Jumlah_pesanan",

    color="Interpretasi",

    hover_data=[

        "username",

        "menu_yang_dibeli"

    ]

)

st.plotly_chart(

    fig_scatter,

    use_container_width=True

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

st.subheader("📝 Interpretasi")

st.success("""
🟢 Cluster 1

Pola Pemesanan Personal

Kelompok transaksi dengan karakteristik
jumlah pesanan dan total harga relatif rendah.
Umumnya mencerminkan kebutuhan konsumsi individu.
""")

st.info("""
🔵 Cluster 2

Pola Pemesanan Reguler

Kelompok transaksi dengan karakteristik
jumlah pesanan dan total harga sedang.
Mencerminkan pola pembelian rutin pelanggan.
""")

st.warning("""
🟣 Cluster 3

Pola Pemesanan Kelompok

Kelompok transaksi dengan karakteristik
jumlah pesanan dan total harga tinggi.
Biasanya dilakukan untuk kebutuhan bersama
atau pemesanan dalam jumlah besar.
""")
