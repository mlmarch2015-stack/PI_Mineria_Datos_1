from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

df = pd.read_json("data/processed/streaming_users_clean.json")

st.title("📉 Reducción de Dimensionalidad (PCA)")

st.info("""
En esta sección se aplica el Análisis de Componentes Principales (PCA)
para reducir la dimensionalidad del conjunto de datos y visualizar su
estructura en un espacio de dos dimensiones.
""")

variables = [
    "age",
    "monthly_watch_time_mins",
    "customer_support_tickets"
]

X = df[variables].copy()

X = X.dropna()

# Estandarización
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Aplicación de PCA
pca = PCA(n_components=2)
componentes = pca.fit_transform(X_scaled)

pca_df = pd.DataFrame(
    componentes,
    columns=["PC1", "PC2"]
)

st.subheader("📊 Varianza explicada")

varianza = pd.DataFrame({
    "Componente": ["PC1", "PC2"],
    "Varianza explicada": pca.explained_variance_ratio_
})

st.dataframe(varianza, use_container_width=True)

fig, ax = plt.subplots(figsize=(6,4))

ax.bar(
    ["PC1", "PC2"],
    pca.explained_variance_ratio_
)

ax.set_ylabel("Proporción de varianza")
ax.set_title("Varianza explicada por componente")

st.pyplot(fig)


st.subheader("📍 Componentes principales")

fig, ax = plt.subplots(figsize=(7,5))

ax.scatter(
    pca_df["PC1"],
    pca_df["PC2"],
    alpha=0.6
)

ax.set_xlabel("Componente Principal 1")
ax.set_ylabel("Componente Principal 2")
ax.set_title("Distribución de usuarios en el espacio PCA")

st.pyplot(fig)


st.info("""
**Interpretación**

El gráfico representa los usuarios proyectados sobre los dos primeros componentes principales.

Cada punto corresponde a un usuario del conjunto de datos.

La dispersión observada permite identificar posibles agrupamientos, similitudes o diferencias entre los registros después de reducir la dimensionalidad de las variables originales.

Los dos primeros componentes explican aproximadamente el 67 % de la variabilidad del conjunto de datos, conservando gran parte de la información original.
""")
