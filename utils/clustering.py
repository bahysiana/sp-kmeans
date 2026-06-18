import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# =====================================================
# ELBOW METHOD
# =====================================================

def calculate_elbow(data, max_k=10):

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

def calculate_silhouette(data, k):

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
# PROSES KMEANS
# =====================================================

def run_kmeans(data, k):

    model = KMeans(

        n_clusters=k,

        random_state=42,

        n_init=10

    )

    labels = model.fit_predict(data)

    centroid = model.cluster_centers_

    return labels, centroid, model


# =====================================================
# MENAMBAHKAN LABEL KE DATAFRAME
# =====================================================

def add_cluster_to_dataframe(df, labels):

    hasil = df.copy()

    hasil["Cluster"] = labels

    return hasil


# =====================================================
# INTERPRETASI CLUSTER
# =====================================================

def interpret_cluster(df):

    centroid_summary = (

        df.groupby("Cluster")[

            [

                "Total_harga",

                "Jumlah_pesanan"

            ]

        ]

        .mean()

    )

    centroid_summary = centroid_summary.sort_values(

        by=["Total_harga", "Jumlah_pesanan"]

    )

    urutan_cluster = centroid_summary.index.tolist()

    mapping = {

        urutan_cluster[0]:

            "Pola Pemesanan Personal",

        urutan_cluster[1]:

            "Pola Pemesanan Reguler",

        urutan_cluster[2]:

            "Pola Pemesanan Kelompok"

    }

    df["Interpretasi"] = df["Cluster"].map(mapping)

    return df, mapping


# =====================================================
# RINGKASAN CLUSTER
# =====================================================

def cluster_summary(df):

    hasil = (

        df

        .groupby("Interpretasi")

        .size()

        .reset_index(name="Jumlah Data")

    )

    return hasil
