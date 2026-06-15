# pages/2_Kelola_Data.py

import streamlit as st
import pandas as pd

from utils.database import (
    get_all_data,
    import_csv,
    count_data,
    truncate_table,
)

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="Kelola Data",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Kelola Data Transaksi")
st.caption(
    "Tambah, ubah, hapus, dan impor data transaksi Shopee Food."
)

st.divider()

# ==========================================
# STATISTIK
# ==========================================

try:
    total_data = count_data()
except Exception:
    total_data = 0

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "📦 Total Data",
        total_data
    )

with c2:
    st.metric(
        "💾 Database",
        "SQLite"
    )

with c3:
    st.metric(
        "📊 Status",
        "Aktif"
    )

st.divider()

# ==========================================
# IMPORT CSV
# ==========================================

st.subheader("📤 Import Dataset CSV")

uploaded_file = st.file_uploader(
    "Upload file CSV",
    type=["csv"]
)

if uploaded_file is not None:

    try:

        preview_df = pd.read_csv(uploaded_file)

        st.success("File berhasil dibaca.")

        st.dataframe(
            preview_df.head(),
            use_container_width=True
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "➕ Tambahkan ke Database",
                use_container_width=True
            ):

                import_csv(preview_df)

                st.success(
                    "Dataset berhasil ditambahkan."
                )

                st.rerun()

        with col2:

            if st.button(
                "♻️ Ganti Seluruh Database",
                use_container_width=True
            ):

                truncate_table()

                import_csv(preview_df)

                st.success(
                    "Database berhasil diganti."
                )

                st.rerun()

    except Exception as e:

        st.error(
            f"Gagal membaca CSV: {e}"
        )

st.divider()

# ==========================================
# PENCARIAN DATA
# ==========================================

st.subheader("🔍 Pencarian Data")

df = get_all_data()

keyword = st.text_input(
    "Cari berdasarkan Username atau Menu"
)

if keyword:

    keyword = keyword.lower()

    df = df[
        df["username"]
        .astype(str)
        .str.lower()
        .str.contains(keyword)

        |

        df["menu_yang_dibeli"]
        .astype(str)
        .str.lower()
        .str.contains(keyword)
    ]

st.write(f"Jumlah data ditampilkan : **{len(df)}**")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)


# ==========================================
# FORM TAMBAH DATA
# ==========================================

from utils.database import insert_data

st.divider()
st.subheader("➕ Tambah Data Transaksi Baru")

with st.form("form_tambah_data", clear_on_submit=True):

    col1, col2 = st.columns(2)

    with col1:

        username = st.text_input(
            "Username",
            placeholder="Contoh: bahy_saina"
        )

        menu_yang_dibeli = st.text_input(
            "Menu yang Dibeli",
            placeholder="Contoh: Nasi Goreng"
        )

        total_harga = st.number_input(
            "Total Harga",
            min_value=0.0,
            step=1000.0,
            format="%.2f"
        )

        harga_per_menu = st.number_input(
            "Harga per Menu",
            min_value=0.0,
            step=1000.0,
            format="%.2f"
        )

    with col2:

        jumlah_pesanan = st.number_input(
            "Jumlah Pesanan",
            min_value=1,
            step=1
        )

        rata_rata_harga = st.number_input(
            "Rata-rata Harga",
            min_value=0.0,
            step=1000.0,
            format="%.2f"
        )

        waktu_persiapan_yang_diberikan = st.number_input(
            "Waktu Persiapan yang Diberikan (menit)",
            min_value=0.0,
            step=1.0
        )

        waktu_persiapan_digunakan = st.number_input(
            "Waktu Persiapan Digunakan (menit)",
            min_value=0.0,
            step=1.0
        )

    st.write("### 🕒 Waktu Pemesanan")

    tanggal = st.date_input(
        "Tanggal"
    )

    jam = st.time_input(
        "Jam"
    )

    simpan = st.form_submit_button(
        "💾 Simpan Data"
    )

if simpan:

    waktu_pesan = f"{tanggal} {jam}"

    try:

        insert_data(

            username=username,

            menu_yang_dibeli=menu_yang_dibeli,

            Total_harga=total_harga,

            harga_per_menu=harga_per_menu,

            Jumlah_pesanan=jumlah_pesanan,

            rata_rata_harga=rata_rata_harga,

            waktu_persiapan_yang_diberikan=waktu_persiapan_yang_diberikan,

            waktu_persiapan_digunakan=waktu_persiapan_digunakan,

            waktu_pesan=waktu_pesan

        )

        st.success(
            "✅ Data berhasil ditambahkan."
        )

        st.rerun()

    except Exception as e:

        st.error(e)


# ==========================================
# EDIT DATA
# ==========================================

from utils.database import (
    update_data,
    get_data_by_id
)

st.divider()
st.subheader("✏️ Edit Data")

data_db = get_all_data()

if not data_db.empty:

    selected_id = st.selectbox(
        "Pilih ID yang akan diedit",
        data_db["id"].tolist()
    )

    row = get_data_by_id(selected_id)

    if row:

        with st.form("form_edit"):

            username_edit = st.text_input(
                "Username",
                value=row[1]
            )

            menu_edit = st.text_input(
                "Menu",
                value=row[2]
            )

            total_edit = st.number_input(
                "Total Harga",
                value=float(row[3])
            )

            harga_menu_edit = st.number_input(
                "Harga per Menu",
                value=float(row[4])
            )

            jumlah_edit = st.number_input(
                "Jumlah Pesanan",
                value=int(row[5]),
                step=1
            )

            rata_edit = st.number_input(
                "Rata-rata Harga",
                value=float(row[6])
            )

            wp_diberikan_edit = st.number_input(
                "Waktu Persiapan Diberikan",
                value=float(row[7])
            )

            wp_digunakan_edit = st.number_input(
                "Waktu Persiapan Digunakan",
                value=float(row[8])
            )

            waktu_edit = st.text_input(
                "Waktu Pesan",
                value=row[9]
            )

            submit_edit = st.form_submit_button(
                "💾 Simpan Perubahan"
            )

        if submit_edit:

            update_data(

                selected_id,

                username_edit,

                menu_edit,

                total_edit,

                harga_menu_edit,

                jumlah_edit,

                rata_edit,

                wp_diberikan_edit,

                wp_digunakan_edit,

                waktu_edit

            )

            st.success(
                "Data berhasil diperbarui."
            )

            st.rerun()


# ==========================================
# HAPUS DATA
# ==========================================

st.divider()
st.subheader("🗑️ Hapus Data")

hapus_id = st.selectbox(
    "Pilih ID yang akan dihapus",
    data_db["id"].tolist(),
    key="hapus"
)

konfirmasi = st.checkbox(
    "Saya yakin ingin menghapus data ini."
)

if st.button("🗑️ Hapus"):

    if konfirmasi:

        delete_data(hapus_id)

        st.success(
            "Data berhasil dihapus."
        )

        st.rerun()

    else:

        st.warning(
            "Centang konfirmasi terlebih dahulu."
        )
