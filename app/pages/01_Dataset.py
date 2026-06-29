import streamlit as st
import pandas as pd

# ---------------------------------------------
# Configuración de la página
# ---------------------------------------------

st.set_page_config(
    page_title="Dataset",
    page_icon="📂",
    layout="wide"
)

# ---------------------------------------------
# Título
# ---------------------------------------------


st.title("📂 Exploración del Dataset")

st.info("""
En esta sección se presenta el conjunto de datos utilizado en el proyecto.
Se muestran sus características principales, la estructura de las variables,
la cantidad de registros y estadísticas descriptivas.
""")

st.markdown("---")


# ---------------------------------------------
# Cargar dataset
# ---------------------------------------------

df = pd.read_json("data/processed/streaming_users_clean.json")


# ---------------------------------------------
# Métricas del Dataset
# ---------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👥 Registros", len(df))

with col2:
    st.metric("📑 Variables", df.shape[1])

with col3:
    st.metric("❗ Valores faltantes", int(df.isnull().sum().sum()))


    st.markdown("---")

st.subheader("👀 Vista previa del Dataset")

st.dataframe(df.head(10), use_container_width=True)


st.markdown("---")

st.subheader("📋 Información de las columnas")

tipos = pd.DataFrame({
    "Columna": df.columns,
    "Tipo de dato": df.dtypes.astype(str)
})

st.dataframe(tipos, use_container_width=True)


st.markdown("---")

st.subheader("📊 Estadísticas descriptivas")

st.dataframe(df.describe(), use_container_width=True)



csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Descargar Dataset en CSV",
    csv,
    "dataset_streaming.csv",
    "text/csv"
)