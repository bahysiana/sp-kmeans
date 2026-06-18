import streamlit as st
import pandas as pd
import plotly.express as px

from utils.database import get_all_data
from utils.preprocessing import preprocessing_pipeline
from utils.clustering import (
    calculate_elbow,
    calculate_silhouette,
    run_kmeans,
    add_cluster_to_dataframe,
    interpret_cluster,
    cluster_summary,
    cluster_statistics
)

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="K-Means Clustering",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 K-Means Clustering")
st.caption(
    "Proses pengelompokan pola transaksi Shopee Food menggunakan algoritma K-Means."
)

st.divider()

# =====================================================
# AMBIL DATA
# =====================================================

df = get_all_data()

if df.empty:
    st.warning("⚠️ Database masih kosong.")
    st.stop()

# =====================================================
# PREPROCESSING
# =====================================================

scaled_data, scaler = preprocessing_pipeline(df)

# =====================================================
# INFORMASI
# =====================================================

st.info("""
### Konfigurasi Penelitian

- Metode : K-Means Clustering
- Jumlah Cluster (K) : **3**
- Evaluasi : Elbow Method & Silhouette Score

Interpretasi:
- 🟢 Cluster 1 → Pola Pemesanan Personal
- 🔵 Cluster 2 → Pola Pemesanan Reguler
- 🟣 Cluster 3 → Pola Pemesanan Kelompok
""")

st.divider()

# =====================================================
# ELBOW METHOD
# =====================================================

st.subheader("📉 Elbow Method")

elbow = calculate_elbow(
    scaled_data,
    max_k=5
)

fig_elbow = px.line(
    x=[2, 3, 4, 5],
    y=elbow,
    markers=True,
    labels={
        "x": "Jumlah Cluster (K)",
        "y": "WCSS"
    },
    title="Grafik Elbow Method"
)

st.plotly_chart(
    fig_elbow,
    use_container_width=True
)

# =====================================================
# SILHOUETTE SCORE
# =====================================================

st.subheader("📊 Silhouette Score")

score = calculate_silhouette(
    scaled_data,
    k=3
)

st.metric(
    label="Nilai Silhouette Score",
    value=round(score, 4)
)

st.divider()

# =====================================================
# PROSES K-MEANS
# =====================================================

if st.button(
    "🚀 Jalankan K-Means",
    use_container_width=True
):

    labels, centroid, model = run_kmeans(
        scaled_data,
        k=3
    )

    hasil = add_cluster_to_dataframe(
        df,
        labels
    )

    hasil, mapping = interpret_cluster(
        hasil
    )

    summary = cluster_summary(
        hasil
    )

    statistik = cluster_statistics(
        hasil
    )

    # Simpan ke Session State
    st.session_state["hasil_cluster"] = hasil
    st.session_state["cluster_summary"] = summary
    st.session_state["cluster_statistics"] = statistik
    st.session_state["centroid"] = centroid

    st.success("✅ Clustering berhasil dilakukan.")

    st.subheader("📋 Hasil Clustering")

    st.dataframe(
        hasil,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("📊 Distribusi Cluster")

    fig_cluster = px.bar(
        summary,
        x="Interpretasi",
        y="Jumlah Data",
        text="Jumlah Data",
        color="Interpretasi"
    )

    st.plotly_chart(
        fig_cluster,
        use_container_width=True
    )

    st.subheader("📈 Statistik Cluster")

    st.dataframe(
        statistik,
        use_container_width=True,
        hide_index=True
    )

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

    st.success("""
### Interpretasi Cluster

🟢 **Cluster 1 - Pola Pemesanan Personal**

Kelompok transaksi dengan total harga dan jumlah pesanan relatif rendah.

🔵 **Cluster 2 - Pola Pemesanan Reguler**

Kelompok transaksi dengan karakteristik sedang yang mencerminkan pola pembelian rutin.

🟣 **Cluster 3 - Pola Pemesanan Kelompok**

Kelompok transaksi dengan total harga dan jumlah pesanan relatif tinggi yang umumnya dilakukan untuk kebutuhan bersama.
""")
