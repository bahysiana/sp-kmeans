import pandas as pd
from sklearn.preprocessing import StandardScaler


# ==========================================
# FITUR YANG DIGUNAKAN
# ==========================================

FEATURE_COLUMNS = [
    "Total_harga",
    "Jumlah_pesanan",
    "rata_rata_harga",
    "waktu_persiapan_digunakan"
]


# ==========================================
# AMBIL FITUR NUMERIK
# ==========================================

def get_feature_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Mengambil kolom yang digunakan
    untuk proses clustering.
    """

    return df[FEATURE_COLUMNS].copy()


# ==========================================
# NORMALISASI STANDARD SCALER
# ==========================================

def standardize_data(df: pd.DataFrame):

    scaler = StandardScaler()

    scaled = scaler.fit_transform(df)

    scaled_df = pd.DataFrame(
        scaled,
        columns=df.columns
    )

    return scaled_df, scaler


# ==========================================
# PREPROCESSING LENGKAP
# ==========================================

def preprocessing_pipeline(df: pd.DataFrame):

    fitur = get_feature_data(df)

    fitur = fitur.astype(float)

    hasil_normalisasi, scaler = standardize_data(
        fitur
    )

    return hasil_normalisasi, scaler


# ==========================================
# CEK NILAI KOSONG
# ==========================================

def check_missing(df: pd.DataFrame):

    return df.isnull().sum()


# ==========================================
# CEK DUPLIKAT
# ==========================================

def check_duplicate(df: pd.DataFrame):

    return df.duplicated().sum()


# ==========================================
# RINGKASAN DATA
# ==========================================

def summary(df: pd.DataFrame):

    return {
        "Jumlah Data": len(df),
        "Jumlah Kolom": len(df.columns),
        "Missing Value": int(
            df.isnull().sum().sum()
        ),
        "Duplikat": int(
            df.duplicated().sum()
        )
    }
