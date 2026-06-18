import pandas as pd

def format_rupiah(nilai):
    return f"Rp {nilai:,.0f}"

def safe_dataframe(df):
    if isinstance(df, pd.DataFrame):
        return df.copy()
    return pd.DataFrame()
