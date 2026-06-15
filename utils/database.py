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
# MEMBUAT KONEKSI
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
# MENGAMBIL SELURUH DATA
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

    conn = get_connection()

    query = """
        SELECT *
        FROM transaksi
        WHERE id = ?
    """

    df = pd.read_sql_query(
        query,
        conn,
        params=(id_data,)
    )

    conn.close()

    return df


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
# DELETE DATA
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
# IMPORT CSV KE DATABASE
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

    cursor.execute("""

        DELETE FROM transaksi

    """)

    conn.commit()

    conn.close()


# =====================================================
# EXPORT DATABASE KE DATAFRAME
# =====================================================

def export_dataframe():

    return get_all_data()


# =====================================================
# CEK JUMLAH DATA
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


def replace_all_data(df):
    conn = get_connection()

    df.to_sql(
        "transaksi",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()


def save_dataframe(df):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS transaksi
    """)

    conn.commit()

    df.to_sql(
        "transaksi",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()


def get_data_by_id(id_data):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM transaksi
        WHERE id = ?
        """,
        (id_data,)
    )

    row = cursor.fetchone()

    conn.close()

    return row
