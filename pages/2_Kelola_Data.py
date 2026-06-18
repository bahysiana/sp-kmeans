import streamlit as st
import pandas as pd

from utils.database import (
    get_all_data,
    insert_data,
    import_csv,
    count_data,
    truncate_table,
)

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Kelola Data",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Kelola Data Transaksi")
st.caption(
    "Halaman ini digunakan untuk mengelola dataset transaksi Shopee Food."
)

st.divider()

# =====================================================
# STATISTIK
# =====================================================

try:
    total_data = count_data()
except Exception:
    total_data = 0

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📦 Total Data",
        total_data
    )

with col2:
    st.metric(
        "💾 Database",
        "SQLite"
    )

with col3:
    st.metric(
        "🤖 Status",
        "Aktif"
    )

st.divider()

# =====================================================
# IMPORT CSV
# =====================================================

st.subheader("📤 Import Dataset CSV")

uploaded_file = st.file_uploader(
    "Pilih file CSV",
    type=["csv"]
)

if uploaded_file is not None:

    try:

        preview_df = pd.read_csv(uploaded_file)

        st.success("✅ File berhasil dibaca.")

        st.write("Preview Data:")

        st.dataframe(
            preview_df.head(),
            use_container_width=True,
            hide_index=True
        )

        col_import1, col_import2 = st.columns(2)

        with col_import1:

            if st.button(
                "➕ Tambahkan ke Database",
                use_container_width=True
            ):

                import_csv(preview_df)

                st.success(
                    "Dataset berhasil ditambahkan."
                )

                st.rerun()

        with col_import2:

            if st.button(
                "♻️ Ganti Seluruh Database",
                use_container_width=True
            ):

                truncate_table()

                import_csv(preview_df)

                st.success(
                    "Database berhasil diperbarui."
                )

                st.rerun()

    except Exception as e:

        st.error(
            f"Gagal membaca CSV : {e}"
        )

st.divider()

# =====================================================
# FORM TAMBAH DATA
# =====================================================

st.subheader("➕ Tambah Data Baru")

with st.form(
    "form_tambah",
    clear_on_submit=True
):

    col_a, col_b = st.columns(2)

    with col_a:

        username = st.text_input(
            "Username"
        )

        menu = st.text_input(
            "Menu yang Dibeli"
        )

        total_harga = st.number_input(
            "Total Harga",
            min_value=0.0,
            step=1000.0
        )

        harga_per_menu = st.number_input(
            "Harga per Menu",
            min_value=0.0,
            step=1000.0
        )

    with col_b:

        jumlah_pesanan = st.number_input(
            "Jumlah Pesanan",
            min_value=1,
            step=1
        )

        rata_rata_harga = st.number_input(
            "Rata-rata Harga",
            min_value=0.0,
            step=1000.0
        )

        waktu_persiapan_yang_diberikan = st.number_input(
            "Waktu Persiapan yang Diberikan",
            min_value=0.0,
            step=1.0
        )

        waktu_persiapan_digunakan = st.number_input(
            "Waktu Persiapan Digunakan",
            min_value=0.0,
            step=1.0
        )

    tanggal = st.date_input(
        "Tanggal Pemesanan"
    )

    jam = st.time_input(
        "Jam Pemesanan"
    )

    submit = st.form_submit_button(
        "💾 Simpan Data"
    )

if submit:

    waktu_pesan = f"{tanggal} {jam}"

    try:

        insert_data(

            username,

            menu,

            total_harga,

            harga_per_menu,

            jumlah_pesanan,

            rata_rata_harga,

            waktu_persiapan_yang_diberikan,

            waktu_persiapan_digunakan,

            waktu_pesan

        )

        st.success(
            "Data berhasil ditambahkan."
        )

        st.rerun()

    except Exception as e:

        st.error(e)

st.divider()
