import streamlit as st
import pandas as pd

from utils.database import get_all_data
from utils.preprocessing import (
    summary,
    check_missing,
    check_duplicate,
    preprocessing_pipeline
)

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Preprocessing Data",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Preprocessing Data")
st.caption(
    "Tahapan persiapan data sebelum proses K-Means Clustering."
)

st.divider()

# =====================================================
# AMBIL DATA
# =====================================================

df = get_all_data()

if df.empty:
    st.warning("Belum ada data pada database.")
    st.stop()

# =====================================================
# RINGKASAN DATA
# =====================================================

st.subheader("📊 Ringkasan Dataset")

info = summary(df)

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Jumlah Data",
    info["Jumlah Data"]
)

c2.metric(
    "Jumlah Kolom",
    info["Jumlah Kolom"]
)

c3.metric(
    "Missing Value",
    info["Missing Value"]
)

c4.metric(
    "Duplikat",
    info["Duplikat"]
)

st.divider()

# =====================================================
# DATA ASLI
# =====================================================

st.subheader("📋 Dataset Sebelum Preprocessing")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# =====================================================
# CEK MISSING VALUE
# =====================================================

st.subheader("🔍 Missing Value")

missing = check_missing(df)

st.dataframe(
    missing.to_frame(
        name="Jumlah Missing"
    ),
    use_container_width=True
)

# =====================================================
# CEK DUPLIKAT
# =====================================================

st.subheader("🧩 Data Duplikat")

duplicate = check_duplicate(df)

if duplicate == 0:

    st.success(
        "Tidak ditemukan data duplikat."
    )

else:

    st.warning(
        f"Ditemukan {duplicate} data duplikat."
    )

st.divider()

# =====================================================
# FITUR YANG DIGUNAKAN
# =====================================================

st.subheader("🎯 Fitur yang Digunakan")

fitur = pd.DataFrame({

    "Variabel": [

        "total_harga",

        "jumlah_pesanan",

        "rata_rata_harga",

        "waktu_persiapan_digunakan"

    ],

    "Digunakan": [

        "✅",

        "✅",

        "✅",

        "✅"

    ]

})

st.table(fitur)

st.divider()

# =====================================================
# NORMALISASI
# =====================================================

st.subheader("📈 Hasil Normalisasi StandardScaler")

normalisasi, scaler = preprocessing_pipeline(df)

st.dataframe(
    normalisasi,
    use_container_width=True,
    hide_index=True
)

st.divider()

# =====================================================
# PENJELASAN
# =====================================================

st.info(
    """
Preprocessing dilakukan untuk menyamakan skala antar variabel
menggunakan StandardScaler sehingga proses K-Means tidak
didominasi oleh atribut yang memiliki nilai lebih besar.
"""
)
