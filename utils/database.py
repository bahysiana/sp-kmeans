import sqlite3

DB_PATH = "database/shopee_food.db"

def get_connection():
    return sqlite3.connect(DB_PATH)
