import sqlite3
import pandas as pd
from pathlib import Path

# ==========================
# KONFIGURASI DATABASE
# ==========================
DB_PATH = "database/shopee_food.db"

# Membuat folder database jika belum ada
Path("database").mkdir(parents=True, exist_ok=True)


# ==========================
# KONEKSI DATABASE
# ==========================
def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


# ==========================
# MEMBUAT TABEL
# ==========================
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transaksi (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        menu_dibeli TEXT,

        total_harga REAL,

        harga_per_menu REAL,

        jumlah_pesanan INTEGER,

        rata_rata_harga REAL,

        waktu_persiapan_diberikan REAL,

        waktu_persiapan_digunakan REAL,

        waktu_pesan TEXT

    )
    """)

    conn.commit()
    conn.close()


# ==========================
# AMBIL SEMUA DATA
# ==========================
def get_all_data():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM transaksi",
        conn
    )

    conn.close()

    return df


# ==========================
# TAMBAH DATA
# ==========================
def insert_data(
    username,
    menu_dibeli,
    total_harga,
    harga_per_menu,
    jumlah_pesanan,
    rata_rata_harga,
    waktu_persiapan_diberikan,
    waktu_persiapan_digunakan,
    waktu_pesan
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO transaksi(

        username,
        menu_dibeli,
        total_harga,
        harga_per_menu,
        jumlah_pesanan,
        rata_rata_harga,
        waktu_persiapan_diberikan,
        waktu_persiapan_digunakan,
        waktu_pesan

    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        username,
        menu_dibeli,
        total_harga,
        harga_per_menu,
        jumlah_pesanan,
        rata_rata_harga,
        waktu_persiapan_diberikan,
        waktu_persiapan_digunakan,
        waktu_pesan

    ))

    conn.commit()
    conn.close()


# ==========================
# UPDATE DATA
# ==========================
def update_data(
    id_data,
    username,
    menu_dibeli,
    total_harga,
    harga_per_menu,
    jumlah_pesanan,
    rata_rata_harga,
    waktu_persiapan_diberikan,
    waktu_persiapan_digunakan,
    waktu_pesan
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    UPDATE transaksi

    SET

        username=?,
        menu_dibeli=?,
        total_harga=?,
        harga_per_menu=?,
        jumlah_pesanan=?,
        rata_rata_harga=?,
        waktu_persiapan_diberikan=?,
        waktu_persiapan_digunakan=?,
        waktu_pesan=?

    WHERE id=?

    """, (

        username,
        menu_dibeli,
        total_harga,
        harga_per_menu,
        jumlah_pesanan,
        rata_rata_harga,
        waktu_persiapan_diberikan,
        waktu_persiapan_digunakan,
        waktu_pesan,
        id_data

    ))

    conn.commit()
    conn.close()


# ==========================
# HAPUS DATA
# ==========================
def delete_data(id_data):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM transaksi WHERE id=?",
        (id_data,)
    )

    conn.commit()
    conn.close()


# ==========================
# IMPORT CSV
# ==========================
def import_csv(df):

    conn = get_connection()

    df.to_sql(
        "transaksi",
        conn,
        if_exists="append",
        index=False
    )

    conn.close()

# ==========================
# AMBIL DATA BERDASARKAN ID
# ==========================
def get_data_by_id(id_data):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM transaksi WHERE id=?",
        (id_data,)
    )

    data = cursor.fetchone()

    conn.close()

    return data
