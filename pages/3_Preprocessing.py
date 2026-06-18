import streamlit as st
import pandas as pd

from utils.database import get_all_data
from utils.preprocessing import preprocessing_pipeline

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Preprocessing",
    page_icon="🧹",
    layout="wide"
)

st.title("🧹 Preprocessing Data")
st.caption(
    "Tahapan persiapan data sebelum proses K-Means Clustering."
)

st.divider()

# =====================================================
# AMBIL DATA
# =====================================================

df = get_all_data()

if df.empty:
    st.warning(
        "⚠️ Belum ada data pada database."
    )
    st.stop()

# =====================================================
# INFORMASI FITUR
# =====================================================

st.subheader("📌 Fitur yang Digunakan")

st.info("""
Fitur yang digunakan dalam proses clustering:

- Total_harga
- Jumlah_pesanan
- rata_rata_harga
- waktu_persiapan_digunakan

Normalisasi dilakukan menggunakan **StandardScaler**.
""")

# =====================================================
# DATA SEBELUM PREPROCESSING
# =====================================================

st.subheader("📋 Data Sebelum Preprocessing")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# =====================================================
# PROSES PREPROCESSING
# =====================================================

if st.button(
    "🚀 Jalankan Preprocessing",
    use_container_width=True
):

    try:

        scaled_data, scaler = preprocessing_pipeline(df)

        fitur = [
            "Total_harga",
            "Jumlah_pesanan",
            "rata_rata_harga",
            "waktu_persiapan_digunakan"
        ]

        hasil_preprocessing = pd.DataFrame(
            scaled_data,
            columns=fitur
        )

        st.session_state["scaled_data"] = scaled_data
        st.session_state["preprocessing_result"] = hasil_preprocessing
        st.session_state["scaler"] = scaler

        st.success(
            "✅ Preprocessing berhasil dilakukan."
        )

        st.subheader("📊 Hasil Standardisasi")

        st.dataframe(
            hasil_preprocessing,
            use_container_width=True,
            hide_index=True
        )

    except Exception as e:

        st.error(
            f"Terjadi kesalahan: {e}"
        )

st.divider()

# =====================================================
# KETERANGAN
# =====================================================

st.success("""
### 📖 Keterangan

Pada tahap preprocessing dilakukan normalisasi data
menggunakan metode **StandardScaler** agar setiap
fitur memiliki skala yang sebanding sebelum diproses
menggunakan algoritma K-Means Clustering.
""")
