import streamlit as st
import pandas as pd

from utils.database import (
    get_all_data,
    count_data,
    import_csv,
    truncate_table,
    insert_data,
    update_data,
    delete_data,
    get_data_by_id
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
    "Tambah, ubah, hapus, dan impor data transaksi Shopee Food."
)

st.divider()

# =====================================================
# STATISTIK
# =====================================================

try:
    total_data = count_data()
except:
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
    "Upload File CSV",
    type=["csv"]
)

if uploaded_file is not None:

    try:

        preview = pd.read_csv(uploaded_file)

        st.success(
            "File berhasil dibaca."
        )

        st.dataframe(
            preview.head(),
            use_container_width=True,
            hide_index=True
        )

        c1, c2 = st.columns(2)

        with c1:

            if st.button(
                "➕ Tambahkan ke Database",
                use_container_width=True
            ):

                import_csv(preview)

                st.success(
                    "Data berhasil ditambahkan."
                )

                st.rerun()

        with c2:

            if st.button(
                "♻️ Ganti Seluruh Data",
                use_container_width=True
            ):

                truncate_table()

                import_csv(preview)

                st.success(
                    "Database berhasil diganti."
                )

                st.rerun()

    except Exception as e:

        st.error(e)

st.divider()

# =====================================================
# FORM TAMBAH DATA
# =====================================================

st.subheader("➕ Tambah Data Baru")

with st.form(
    "form_tambah_data",
    clear_on_submit=True
):

    col1, col2 = st.columns(2)

    with col1:

        username = st.text_input(
            "Username"
        )

        menu_yang_dibeli = st.text_input(
            "Menu yang Dibeli"
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

    st.markdown("### 🕒 Waktu Pemesanan")

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

    if username.strip() == "" or menu_yang_dibeli.strip() == "":

        st.warning(
            "Username dan Menu yang Dibeli wajib diisi."
        )

    else:

        waktu_pesan = f"{tanggal} {jam}"

        try:

            insert_data(

                username,

                menu_yang_dibeli,

                total_harga,

                harga_per_menu,

                jumlah_pesanan,

                rata_rata_harga,

                waktu_persiapan_yang_diberikan,

                waktu_persiapan_digunakan,

                waktu_pesan

            )

            st.success(
                "✅ Data berhasil ditambahkan."
            )

            st.rerun()

        except Exception as e:

            st.error(
                f"Gagal menyimpan data: {e}"
            )

st.divider()

# =====================================================
# PENCARIAN DATA
# =====================================================

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
        .str.contains(keyword, na=False)

        |

        df["menu_yang_dibeli"]
        .astype(str)
        .str.lower()
        .str.contains(keyword, na=False)
    ]

st.write(f"**Jumlah data ditemukan:** {len(df)}")

st.divider()

# =====================================================
# TABEL DATA
# =====================================================

st.subheader("📋 Data Transaksi")

if df.empty:

    st.info("Belum ada data yang tersedia.")

else:

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

st.divider()

# =====================================================
# EDIT DATA
# =====================================================

st.subheader("✏️ Edit Data")

data_edit = get_all_data()

if not data_edit.empty:

    id_pilih = st.selectbox(
        "Pilih ID Data yang Akan Diedit",
        data_edit["id"].tolist()
    )

    row = get_data_by_id(id_pilih)

    if row is not None:

        with st.form("form_edit_data"):

            username_edit = st.text_input(
                "Username",
                value=row["username"]
            )

            menu_edit = st.text_input(
                "Menu yang Dibeli",
                value=row["menu_yang_dibeli"]
            )

            total_edit = st.number_input(
                "Total Harga",
                min_value=0.0,
                value=float(row["Total_harga"])
            )

            harga_menu_edit = st.number_input(
                "Harga per Menu",
                min_value=0.0,
                value=float(row["harga_per_menu"])
            )

            jumlah_edit = st.number_input(
                "Jumlah Pesanan",
                min_value=1,
                value=int(row["Jumlah_pesanan"])
            )

            rata_edit = st.number_input(
                "Rata-rata Harga",
                min_value=0.0,
                value=float(row["rata_rata_harga"])
            )

            wp_diberikan_edit = st.number_input(
                "Waktu Persiapan yang Diberikan",
                min_value=0.0,
                value=float(row["waktu_persiapan_yang_diberikan"])
            )

            wp_digunakan_edit = st.number_input(
                "Waktu Persiapan Digunakan",
                min_value=0.0,
                value=float(row["waktu_persiapan_digunakan"])
            )

            waktu_edit = st.text_input(
                "Waktu Pemesanan",
                value=row["waktu_pesan"]
            )

            tombol_edit = st.form_submit_button(
                "💾 Simpan Perubahan"
            )

        if tombol_edit:

            try:

                update_data(

                    id_pilih,

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
                    "✅ Data berhasil diperbarui."
                )

                st.rerun()

            except Exception as e:

                st.error(
                    f"Gagal memperbarui data: {e}"
                )

else:

    st.info("Belum ada data untuk diedit.")

st.divider()

# =====================================================
# HAPUS DATA
# =====================================================

st.subheader("🗑️ Hapus Data")

data_hapus = get_all_data()

if not data_hapus.empty:

    id_hapus = st.selectbox(
        "Pilih ID yang akan dihapus",
        data_hapus["id"].tolist(),
        key="hapus_data"
    )

    konfirmasi = st.checkbox(
        "Saya yakin ingin menghapus data ini."
    )

    if st.button(
        "🗑️ Hapus Data",
        use_container_width=True
    ):

        if not konfirmasi:

            st.warning(
                "Silakan centang konfirmasi terlebih dahulu."
            )

        else:

            try:

                delete_data(id_hapus)

                st.success(
                    "✅ Data berhasil dihapus."
                )

                st.rerun()

            except Exception as e:

                st.error(
                    f"Gagal menghapus data: {e}"
                )

else:

    st.info(
        "Belum ada data yang dapat dihapus."
    )

st.divider()

# =====================================================
# INFORMASI
# =====================================================

st.info("""
### 📌 Informasi

Halaman ini mendukung fitur CRUD (Create, Read, Update, Delete):

- ➕ Menambahkan data transaksi baru.
- 📤 Mengimpor dataset dari file CSV.
- 🔍 Mencari data berdasarkan username atau menu.
- ✏️ Mengedit data transaksi yang sudah ada.
- 🗑️ Menghapus data transaksi.
- 💾 Semua perubahan disimpan secara permanen di database SQLite.
""")
