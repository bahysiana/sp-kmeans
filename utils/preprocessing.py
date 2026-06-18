import pandas as pd
from sklearn.preprocessing import StandardScaler

# =====================================================
# FITUR YANG DIGUNAKAN UNTUK K-MEANS
# =====================================================

FEATURE_COLUMNS = [
    "Total_harga",
    "Jumlah_pesanan",
    "rata_rata_harga",
    "waktu_persiapan_digunakan"
]

# =====================================================
# MENGAMBIL FITUR
# =====================================================

def get_feature_data(df):

    fitur = df[FEATURE_COLUMNS].copy()

    return fitur


# =====================================================
# KONVERSI KE NUMERIK
# =====================================================

def convert_numeric(df):

    hasil = df.copy()

    for kolom in FEATURE_COLUMNS:

        hasil[kolom] = pd.to_numeric(

            hasil[kolom],

            errors="coerce"

        )

    return hasil


# =====================================================
# MENANGANI NILAI KOSONG
# =====================================================

def handle_missing(df):

    hasil = df.copy()

    hasil = hasil.fillna(0)

    return hasil


# =====================================================
# STANDARD SCALER
# =====================================================

def standardize_data(df):

    scaler = StandardScaler()

    scaled = scaler.fit_transform(df)

    scaled_df = pd.DataFrame(

        scaled,

        columns=df.columns,

        index=df.index

    )

    return scaled_df, scaler


# =====================================================
# PREPROCESSING PIPELINE
# =====================================================

def preprocessing_pipeline(df):

    fitur = get_feature_data(df)

    fitur = convert_numeric(fitur)

    fitur = handle_missing(fitur)

    hasil, scaler = standardize_data(fitur)

    return hasil, scaler


# =====================================================
# CEK MISSING VALUE
# =====================================================

def check_missing(df):

    return df.isnull().sum()


# =====================================================
# CEK DUPLIKAT
# =====================================================

def check_duplicate(df):

    return df.duplicated().sum()


# =====================================================
# RINGKASAN DATA
# =====================================================

def summary(df):

    return {

        "Jumlah Data":

            len(df),

        "Jumlah Kolom":

            len(df.columns),

        "Missing Value":

            int(df.isnull().sum().sum()),

        "Duplikat":

            int(df.duplicated().sum())

    }
