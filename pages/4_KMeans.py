import streamlit as st
import plotly.express as px

from utils.database import get_all_data
from utils.preprocessing import preprocessing_pipeline
from utils.clustering import (
    calculate_elbow,
    calculate_silhouette,
    run_kmeans,
    add_cluster_to_dataframe,
    interpret_cluster,
    cluster_summary
)

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="K-Means Clustering",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Proses K-Means Clustering")
st.caption(
    "Analisis pola transaksi Shopee Food menggunakan metode K-Means Clustering."
)

st.divider()

# =====================================================
# AMBIL DATA
# =====================================================

df = get_all_data()

if df.empty:
    st.warning("⚠️ Database masih kosong. Silakan tambahkan data terlebih dahulu.")
    st.stop()

# =====================================================
# NILAI K DIKUNCI MENJADI 3
# =====================================================

k = 3

st.success(
    "✅ Jumlah cluster ditetapkan sebanyak **3 cluster (K = 3)** "
    "sesuai dengan metodologi penelitian."
)

st.info("""
Interpretasi cluster yang digunakan:

- 🟢 Cluster 1 → Pola Pemesanan Personal
- 🔵 Cluster 2 → Pola Pemesanan Reguler
- 🟣 Cluster 3 → Pola Pemesanan Kelompok
""")

st.divider()

# =====================================================
# PREPROCESSING
# =====================================================

scaled_data, scaler = preprocessing_pipeline(df)

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
    "Silhouette Score",
    round(score, 4)
)

st.divider()

# =====================================================
# PROSES CLUSTERING
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

    # Simpan ke session_state
    st.session_state["hasil_cluster"] = hasil
    st.session_state["cluster_summary"] = summary
    st.session_state["centroid"] = centroid
    st.session_state["k_value"] = 3

    st.success("✅ Proses clustering berhasil dilakukan.")

    st.subheader("📋 Hasil Clustering")

    st.dataframe(
        hasil,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("📊 Distribusi Cluster")

    fig_bar = px.bar(
        summary,
        x="Interpretasi",
        y="Jumlah Data",
        text="Jumlah Data",
        color="Interpretasi"
    )

    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )

    st.subheader("📍 Nilai Centroid")

    centroid_df = (
        px.data.iris().head(0)
    )  # placeholder kosong

    import pandas as pd

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
Interpretasi akhir:

🟢 Cluster 1 → Pola Pemesanan Personal

🔵 Cluster 2 → Pola Pemesanan Reguler

🟣 Cluster 3 → Pola Pemesanan Kelompok
""")
