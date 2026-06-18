import pandas as pd

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# =====================================================
# ELBOW METHOD
# =====================================================

def calculate_elbow(data, max_k=5):
    """
    Menghitung nilai WCSS (Within Cluster Sum of Squares)
    untuk metode Elbow.
    """

    inertia = []

    for k in range(2, max_k + 1):

        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        model.fit(data)

        inertia.append(model.inertia_)

    return inertia


# =====================================================
# SILHOUETTE SCORE
# =====================================================

def calculate_silhouette(data, k=3):
    """
    Menghitung Silhouette Score.
    """

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(data)

    score = silhouette_score(
        data,
        labels
    )

    return score


# =====================================================
# PROSES K-MEANS
# =====================================================

def run_kmeans(data, k=3):
    """
    Menjalankan proses clustering.
    """

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(data)

    centroid = model.cluster_centers_

    return labels, centroid, model


# =====================================================
# TAMBAHKAN LABEL CLUSTER
# =====================================================

def add_cluster_to_dataframe(df, labels):
    """
    Menambahkan hasil cluster ke dataframe.
    """

    hasil = df.copy()

    # Agar cluster menjadi 1, 2, 3
    hasil["Cluster"] = labels + 1

    return hasil


# =====================================================
# INTERPRETASI CLUSTER
# =====================================================

def interpret_cluster(df):
    """
    Memberikan nama cluster berdasarkan
    rata-rata Total_harga dan Jumlah_pesanan.
    """

    centroid_summary = (

        df.groupby("Cluster")[
            [
                "Total_harga",
                "Jumlah_pesanan"
            ]
        ]

        .mean()

        .sort_values(
            by=[
                "Total_harga",
                "Jumlah_pesanan"
            ]
        )

    )

    urutan = centroid_summary.index.tolist()

    if len(urutan) != 3:

        raise ValueError(
            "Interpretasi ini dirancang khusus untuk 3 cluster."
        )

    mapping = {

        urutan[0]:
            "Pola Pemesanan Personal",

        urutan[1]:
            "Pola Pemesanan Reguler",

        urutan[2]:
            "Pola Pemesanan Kelompok"

    }

    hasil = df.copy()

    hasil["Interpretasi"] = hasil["Cluster"].map(mapping)

    return hasil, mapping


# =====================================================
# RINGKASAN CLUSTER
# =====================================================

def cluster_summary(df):
    """
    Menampilkan jumlah data pada tiap cluster.
    """

    summary = (

        df

        .groupby(
            [
                "Cluster",
                "Interpretasi"
            ]
        )

        .size()

        .reset_index(
            name="Jumlah Data"
        )

        .sort_values(
            by="Cluster"
        )

    )

    return summary


# =====================================================
# STATISTIK CLUSTER
# =====================================================

def cluster_statistics(df):
    """
    Menampilkan rata-rata tiap variabel
    pada masing-masing cluster.
    """

    statistik = (

        df

        .groupby(
            [
                "Cluster",
                "Interpretasi"
            ]
        )[

            [
                "Total_harga",
                "Jumlah_pesanan",
                "rata_rata_harga",
                "waktu_persiapan_digunakan"
            ]

        ]

        .mean()

        .round(2)

        .reset_index()

    )

    return statistik
