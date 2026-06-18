import sqlite3
import pandas as pd
from pathlib import Path

# =====================================================
# KONFIGURASI DATABASE
# =====================================================

DATABASE_FOLDER = Path("database")
DATABASE_FOLDER.mkdir(exist_ok=True)

DB_PATH = DATABASE_FOLDER / "shopee_food.db"


# =====================================================
# KONEKSI DATABASE
# =====================================================

def get_connection():
    return sqlite3.connect(DB_PATH)


# =====================================================
# MEMBUAT TABEL
# =====================================================

def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transaksi (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT,

            menu_yang_dibeli TEXT,

            Total_harga REAL,

            harga_per_menu REAL,

            Jumlah_pesanan INTEGER,

            rata_rata_harga REAL,

            waktu_persiapan_yang_diberikan REAL,

            waktu_persiapan_digunakan REAL,

            waktu_pesan TEXT

        )
    """)

    conn.commit()
    conn.close()


# =====================================================
# AMBIL SEMUA DATA
# =====================================================

def get_all_data():

    conn = get_connection()

    df = pd.read_sql_query(

        """
        SELECT *
        FROM transaksi
        ORDER BY id ASC
        """,

        conn

    )

    conn.close()

    return df


# =====================================================
# AMBIL DATA BERDASARKAN ID
# =====================================================

def get_data_by_id(id_data):

    df = get_all_data()

    hasil = df[df["id"] == id_data]

    if hasil.empty:

        return None

    return hasil.iloc[0]


# =====================================================
# HITUNG JUMLAH DATA
# =====================================================

def count_data():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT COUNT(*)

        FROM transaksi

    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =====================================================
# INSERT DATA
# =====================================================

def insert_data(

    username,

    menu_yang_dibeli,

    Total_harga,

    harga_per_menu,

    Jumlah_pesanan,

    rata_rata_harga,

    waktu_persiapan_yang_diberikan,

    waktu_persiapan_digunakan,

    waktu_pesan

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO transaksi (

            username,

            menu_yang_dibeli,

            Total_harga,

            harga_per_menu,

            Jumlah_pesanan,

            rata_rata_harga,

            waktu_persiapan_yang_diberikan,

            waktu_persiapan_digunakan,

            waktu_pesan

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        username,

        menu_yang_dibeli,

        Total_harga,

        harga_per_menu,

        Jumlah_pesanan,

        rata_rata_harga,

        waktu_persiapan_yang_diberikan,

        waktu_persiapan_digunakan,

        waktu_pesan

    ))

    conn.commit()
    conn.close()


# =====================================================
# UPDATE DATA
# =====================================================

def update_data(

    id_data,

    username,

    menu_yang_dibeli,

    Total_harga,

    harga_per_menu,

    Jumlah_pesanan,

    rata_rata_harga,

    waktu_persiapan_yang_diberikan,

    waktu_persiapan_digunakan,

    waktu_pesan

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        UPDATE transaksi

        SET

            username = ?,

            menu_yang_dibeli = ?,

            Total_harga = ?,

            harga_per_menu = ?,

            Jumlah_pesanan = ?,

            rata_rata_harga = ?,

            waktu_persiapan_yang_diberikan = ?,

            waktu_persiapan_digunakan = ?,

            waktu_pesan = ?

        WHERE id = ?

    """, (

        username,

        menu_yang_dibeli,

        Total_harga,

        harga_per_menu,

        Jumlah_pesanan,

        rata_rata_harga,

        waktu_persiapan_yang_diberikan,

        waktu_persiapan_digunakan,

        waktu_pesan,

        id_data

    ))

    conn.commit()
    conn.close()


# =====================================================
# HAPUS DATA
# =====================================================

def delete_data(id_data):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        DELETE FROM transaksi

        WHERE id = ?

        """,

        (id_data,)

    )

    conn.commit()
    conn.close()


# =====================================================
# IMPORT CSV
# =====================================================

def import_csv(df):

    conn = get_connection()

    df.to_sql(

        "transaksi",

        conn,

        if_exists="append",

        index=False

    )

    conn.close()


# =====================================================
# HAPUS SEMUA DATA
# =====================================================

def truncate_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        DELETE FROM transaksi

        """

    )

    conn.commit()
    conn.close()


# =====================================================
# GANTI SELURUH DATA
# =====================================================

def replace_all_data(df):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        DELETE FROM transaksi

        """

    )

    conn.commit()

    df.to_sql(

        "transaksi",

        conn,

        if_exists="append",

        index=False

    )

    conn.close()


# =====================================================
# SIMPAN DATAFRAME
# =====================================================

def save_dataframe(df):

    replace_all_data(df)


# =====================================================
# EXPORT DATAFRAME
# =====================================================

def export_dataframe():

    return get_all_data()


# =====================================================
# INISIALISASI DATABASE
# =====================================================

create_table()
