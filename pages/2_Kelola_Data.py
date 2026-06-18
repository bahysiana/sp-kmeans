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
    st.metric("📦 Total Data", total_data)

with col2:
    st.metric("💾 Database", "SQLite")

with col3:
    st.metric("🤖 Status", "Aktif")

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

        # File Anda menggunakan delimiter ";"
        preview = pd.read_csv(
            uploaded_file,
            sep=";"
        )

        # Normalisasi nama kolom
        preview.columns = (
            preview.columns
            .str.strip()
            .str.replace(" ", "_")
        )

        # Hapus kolom nomor jika ada
        if "no" in preview.columns:
            preview.drop(columns=["no"], inplace=True)

        # Bersihkan kolom waktu
        for col in [
            "waktu_persiapan_yang_diberikan",
            "waktu_persiapan_digunakan"
        ]:

            preview[col] = (
                preview[col]
                .astype(str)
                .str.replace(" menit", "", regex=False)
            )

            preview[col] = pd.to_numeric(
                preview[col],
                errors="coerce"
            )

        # Konversi numerik
        preview["Total_harga"] = pd.to_numeric(
            preview["Total_harga"],
            errors="coerce"
        )

        preview["Jumlah_pesanan"] = pd.to_numeric(
            preview["Jumlah_pesanan"],
            errors="coerce"
        )

        preview["rata_rata_harga"] = pd.to_numeric(
            preview["rata_rata_harga"],
            errors="coerce"
        )

        # harga_per_menu disimpan sebagai teks
        preview["harga_per_menu"] = (
            preview["harga_per_menu"]
            .astype(str)
        )

        st.success("✅ File berhasil dibaca.")

        st.dataframe(
            preview.head(),
            use_container_width=True,
            hide_index=True
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "➕ Tambahkan ke Database",
                use_container_width=True
            ):

                import_csv(preview)

                st.success(
                    "✅ Data berhasil ditambahkan."
                )

                st.rerun()

        with col2:

            if st.button(
                "♻️ Ganti Seluruh Data",
                use_container_width=True
            ):

                truncate_table()

                import_csv(preview)

                st.success(
                    "✅ Database berhasil diganti."
                )

                st.rerun()

    except Exception as e:

        st.error(
            f"❌ Gagal membaca CSV: {e}"
        )

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
            value=0.0,
            step=1000.0
        )

        harga_per_menu = st.text_input(
            "Harga per Menu (contoh: 10000 atau 10000,15000)"
        )

    with col2:

        jumlah_pesanan = st.number_input(
            "Jumlah Pesanan",
            min_value=1,
            value=1,
            step=1
        )

        rata_rata_harga = st.number_input(
            "Rata-rata Harga",
            min_value=0.0,
            value=0.0,
            step=1000.0
        )

        waktu_persiapan_yang_diberikan = st.number_input(
            "Waktu Persiapan yang Diberikan (menit)",
            min_value=0.0,
            value=0.0,
            step=1.0
        )

        waktu_persiapan_digunakan = st.number_input(
            "Waktu Persiapan Digunakan (menit)",
            min_value=0.0,
            value=0.0,
            step=1.0
        )

    st.markdown("### 🕒 Waktu Pemesanan")

    tanggal = st.date_input(
        "Tanggal Pemesanan"
    )

    jam = st.time_input(
        "Jam Pemesanan"
    )

    tombol_simpan = st.form_submit_button(
        "💾 Simpan Data"
    )

if tombol_simpan:

    if username.strip() == "":

        st.warning("Username tidak boleh kosong.")

    elif menu_yang_dibeli.strip() == "":

        st.warning("Menu yang dibeli tidak boleh kosong.")

    else:

        waktu_pesan = f"{tanggal} {jam}"

        try:

            insert_data(

                username=username,

                menu_yang_dibeli=menu_yang_dibeli,

                Total_harga=float(total_harga),

                harga_per_menu=harga_per_menu,

                Jumlah_pesanan=int(jumlah_pesanan),

                rata_rata_harga=float(rata_rata_harga),

                waktu_persiapan_yang_diberikan=float(
                    waktu_persiapan_yang_diberikan
                ),

                waktu_persiapan_digunakan=float(
                    waktu_persiapan_digunakan
                ),

                waktu_pesan=waktu_pesan

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

# Jika database kosong
if df.empty:

    st.warning("⚠️ Database masih kosong.")

else:

    keyword = st.text_input(
        "Cari berdasarkan Username atau Menu",
        placeholder="Contoh: arda atau mie nyemek"
    )

    if keyword.strip() != "":

        keyword = keyword.lower()

        df = df[
            (
                df["username"]
                .astype(str)
                .str.lower()
                .str.contains(keyword, na=False)
            )
            |
            (
                df["menu_yang_dibeli"]
                .astype(str)
                .str.lower()
                .str.contains(keyword, na=False)
            )
        ]

    st.info(f"Jumlah data ditemukan: **{len(df)}**")

st.divider()

# =====================================================
# TABEL DATA
# =====================================================

st.subheader("📋 Data Transaksi")

if df.empty:

    st.warning("Belum ada data untuk ditampilkan.")

else:

    tampil_df = df.copy()

    # Format tampilan waktu agar lebih rapi
    if "waktu_pesan" in tampil_df.columns:

        tampil_df["waktu_pesan"] = (
            tampil_df["waktu_pesan"]
            .astype(str)
        )

    st.dataframe(

        tampil_df,

        use_container_width=True,

        hide_index=True

    )

    st.success(
        f"Total data yang ditampilkan: {len(tampil_df)} transaksi."
    )

st.divider()

# =====================================================
# EDIT DATA
# =====================================================

st.subheader("✏️ Edit Data")

data_edit = get_all_data()

if data_edit.empty:

    st.info("Belum ada data yang dapat diedit.")

else:

    id_pilih = st.selectbox(
        "Pilih ID Data yang Akan Diedit",
        options=data_edit["id"].tolist()
    )

    row = get_data_by_id(id_pilih)

    if row is not None:

        with st.form("form_edit_data"):

            col1, col2 = st.columns(2)

            with col1:

                username_edit = st.text_input(
                    "Username",
                    value=str(row["username"])
                )

                menu_edit = st.text_input(
                    "Menu yang Dibeli",
                    value=str(row["menu_yang_dibeli"])
                )

                total_edit = st.number_input(
                    "Total Harga",
                    min_value=0.0,
                    value=float(row["Total_harga"]),
                    step=1000.0
                )

                harga_menu_edit = st.text_input(
                    "Harga per Menu",
                    value=str(row["harga_per_menu"])
                )

            with col2:

                jumlah_edit = st.number_input(
                    "Jumlah Pesanan",
                    min_value=1,
                    value=int(row["Jumlah_pesanan"]),
                    step=1
                )

                rata_edit = st.number_input(
                    "Rata-rata Harga",
                    min_value=0.0,
                    value=float(row["rata_rata_harga"]),
                    step=1000.0
                )

                # Aman meskipun sebelumnya tersimpan "13 menit"
                wp_diberikan = str(
                    row["waktu_persiapan_yang_diberikan"]
                ).replace(" menit", "").replace(",", ".")

                wp_digunakan = str(
                    row["waktu_persiapan_digunakan"]
                ).replace(" menit", "").replace(",", ".")

                wp_diberikan_edit = st.number_input(
                    "Waktu Persiapan yang Diberikan (menit)",
                    min_value=0.0,
                    value=float(wp_diberikan),
                    step=1.0
                )

                wp_digunakan_edit = st.number_input(
                    "Waktu Persiapan Digunakan (menit)",
                    min_value=0.0,
                    value=float(wp_digunakan),
                    step=1.0
                )

            waktu_edit = st.text_input(
                "Waktu Pemesanan",
                value=str(row["waktu_pesan"])
            )

            tombol_edit = st.form_submit_button(
                "💾 Simpan Perubahan"
            )

        if tombol_edit:

            try:

                update_data(

                    id_data=id_pilih,

                    username=username_edit,

                    menu_yang_dibeli=menu_edit,

                    Total_harga=float(total_edit),

                    harga_per_menu=harga_menu_edit,

                    Jumlah_pesanan=int(jumlah_edit),

                    rata_rata_harga=float(rata_edit),

                    waktu_persiapan_yang_diberikan=float(
                        wp_diberikan_edit
                    ),

                    waktu_persiapan_digunakan=float(
                        wp_digunakan_edit
                    ),

                    waktu_pesan=waktu_edit

                )

                st.success(
                    "✅ Data berhasil diperbarui."
                )

                st.rerun()

            except Exception as e:

                st.error(
                    f"Gagal memperbarui data: {e}"
                )

st.divider()

# =====================================================
# HAPUS DATA
# =====================================================

st.subheader("🗑️ Hapus Data")

data_hapus = get_all_data()

if data_hapus.empty:

    st.info("Belum ada data yang dapat dihapus.")

else:

    id_hapus = st.selectbox(
        "Pilih ID yang akan dihapus",
        options=data_hapus["id"].tolist(),
        key="hapus_data"
    )

    row_hapus = get_data_by_id(id_hapus)

    if row_hapus is not None:

        st.warning("Data yang akan dihapus:")

        st.write(f"**Username :** {row_hapus['username']}")
        st.write(f"**Menu :** {row_hapus['menu_yang_dibeli']}")
        st.write(f"**Total Harga :** Rp {float(row_hapus['Total_harga']):,.0f}")

    konfirmasi = st.checkbox(
        "Saya yakin ingin menghapus data ini."
    )

    if st.button(
        "❌ Hapus Data",
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

st.divider()

# =====================================================
# INFORMASI
# =====================================================

st.info("""
### 📌 Informasi Halaman Kelola Data

Halaman ini digunakan untuk mengelola data transaksi Shopee Food
yang akan digunakan pada proses K-Means Clustering.

Fitur yang tersedia:

- 📤 Import dataset CSV
- ➕ Tambah data transaksi
- 🔍 Pencarian data
- 📋 Melihat seluruh data
- ✏️ Edit data transaksi
- 🗑️ Hapus data transaksi

Seluruh perubahan akan langsung tersimpan ke database SQLite
dan dapat digunakan pada proses preprocessing maupun clustering.
""")
