import sqlite3
import pandas as pd
import os

# =====================================================
# KONFIGURASI DATABASE
# =====================================================

DB_PATH = "shopee_food.db"


# =====================================================
# KONEKSI DATABASE
# =====================================================

def get_connection():

    conn = sqlite3.connect(DB_PATH)

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

    return conn


# =====================================================
# CREATE TABLE
# =====================================================

def create_table():

    conn = get_connection()
    conn.close()


# =====================================================
# AMBIL SEMUA DATA
# =====================================================

def get_all_data():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM transaksi ORDER BY id ASC",
        conn
    )

    conn.close()

    return df


# =====================================================
# HITUNG DATA
# =====================================================

def count_data():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM transaksi"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =====================================================
# AMBIL BERDASARKAN ID
# =====================================================

def get_data_by_id(id_data):

    df = get_all_data()

    hasil = df[df["id"] == id_data]

    if hasil.empty:
        return None

    return hasil.iloc[0]


# =====================================================
# INSERT
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
# UPDATE
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

        username=?,
        menu_yang_dibeli=?,
        Total_harga=?,
        harga_per_menu=?,
        Jumlah_pesanan=?,
        rata_rata_harga=?,
        waktu_persiapan_yang_diberikan=?,
        waktu_persiapan_digunakan=?,
        waktu_pesan=?

    WHERE id=?

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
# DELETE
# =====================================================

def delete_data(id_data):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM transaksi WHERE id=?",
        (id_data,)
    )

    conn.commit()

    conn.close()


# =====================================================
# HAPUS SEMUA
# =====================================================

def truncate_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM transaksi"
    )

    conn.commit()

    conn.close()


# =====================================================
# EXPORT
# =====================================================

def export_dataframe():

    return get_all_data()


# =====================================================
# INISIALISASI
# =====================================================

create_table()
