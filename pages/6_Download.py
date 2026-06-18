import streamlit as st
import pandas as pd

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Download Hasil",
    page_icon="📥",
    layout="wide"
)

st.title("📥 Download Hasil Clustering")
st.caption(
    "Unduh hasil analisis K-Means Clustering dalam format CSV."
)

st.divider()

# =====================================================
# CEK SESSION
# =====================================================

if "hasil_cluster" not in st.session_state:

    st.warning(
        "⚠️ Belum ada hasil clustering. Silakan jalankan proses K-Means terlebih dahulu."
    )

    st.stop()

# =====================================================
# AMBIL DATA
# =====================================================

hasil_cluster = st.session_state["hasil_cluster"]
cluster_summary = st.session_state["cluster_summary"]
cluster_statistics = st.session_state["cluster_statistics"]

# =====================================================
# PREVIEW
# =====================================================

st.subheader("📋 Preview Hasil Clustering")

st.dataframe(
    hasil_cluster.head(10),
    use_container_width=True,
    hide_index=True
)

st.divider()

# =====================================================
# DOWNLOAD HASIL CLUSTER
# =====================================================

st.subheader("📥 Download Data")

csv_hasil = hasil_cluster.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇️ Download Hasil Clustering (CSV)",
    data=csv_hasil,
    file_name="hasil_clustering.csv",
    mime="text/csv",
    use_container_width=True
)

# =====================================================
# DOWNLOAD SUMMARY
# =====================================================

csv_summary = cluster_summary.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇️ Download Ringkasan Cluster (CSV)",
    data=csv_summary,
    file_name="ringkasan_cluster.csv",
    mime="text/csv",
    use_container_width=True
)

# =====================================================
# DOWNLOAD STATISTIK
# =====================================================

csv_statistik = cluster_statistics.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇️ Download Statistik Cluster (CSV)",
    data=csv_statistik,
    file_name="statistik_cluster.csv",
    mime="text/csv",
    use_container_width=True
)

st.divider()

# =====================================================
# INFORMASI
# =====================================================

st.success("""
### 📌 Informasi

File yang dapat diunduh:

- 📄 **hasil_clustering.csv**
  - Berisi seluruh data transaksi beserta label cluster dan interpretasi.

- 📄 **ringkasan_cluster.csv**
  - Berisi jumlah anggota pada masing-masing cluster.

- 📄 **statistik_cluster.csv**
  - Berisi nilai rata-rata setiap variabel pada tiap cluster.

Seluruh file dapat digunakan sebagai dokumentasi penelitian
dan lampiran hasil analisis skripsi.
""")
