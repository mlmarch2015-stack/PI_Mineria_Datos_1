import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# --------------------------------------------------

st.set_page_config(
    page_title="EDA",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# CARGAR DATASET
# --------------------------------------------------

df = pd.read_json("data/processed/streaming_users_clean.json")

# --------------------------------------------------
# TÍTULO
# --------------------------------------------------

st.title("📊 Análisis Exploratorio de Datos (EDA)")

st.info("""
En esta sección se analizan las principales características del conjunto de datos mediante gráficos y estadísticas descriptivas.
""")

st.markdown("---")


# --------------------------------------------------
# DISTRIBUCIÓN DE EDADES
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(10,5))

ax.hist(
    df["age"].dropna(),
    bins=20,
    edgecolor="black"
)

ax.set_title("Distribución de edades de los usuarios")

ax.set_xlabel("Edad")

ax.set_ylabel("Cantidad de usuarios")

ax.grid(alpha=0.3)

st.pyplot(fig)


st.success("""
### 📌 Interpretación

El histograma muestra que la mayor concentración de usuarios se encuentra entre los 20 y los 50 años.

Además, se observan algunos valores atípicos, como edades negativas (-5 años) y edades extremadamente altas (150 años), que representan errores de calidad en los datos y deberán considerarse durante el proceso de limpieza y análisis.

La distribución presenta una mayor concentración en edades adultas, lo que indica que la mayoría de los usuarios pertenecen a ese grupo etario.
""")


st.markdown("---")

st.subheader("📺 Distribución de los Planes de Suscripción")

planes = df["subscription_plan"].value_counts()

fig, ax = plt.subplots(figsize=(8,5))

ax.bar(
    planes.index,
    planes.values,
    edgecolor="black"
)

ax.set_title("Cantidad de usuarios por plan de suscripción")
ax.set_xlabel("Plan")
ax.set_ylabel("Cantidad de usuarios")

ax.grid(axis="y", alpha=0.3)

st.pyplot(fig)


st.success("""
### 📌 Interpretación

El gráfico muestra la distribución de los usuarios según su plan de suscripción.

Durante el análisis se detectó una inconsistencia en los datos, ya que algunos planes aparecen en español ("básico", "estándar") y otros en inglés ("basic", "standard"), representando la misma categoría.

Este tipo de inconsistencias es común en bases de datos reales y constituye un aspecto importante a corregir durante la etapa de limpieza de datos para evitar interpretaciones erróneas.
""")


st.markdown("---")

st.subheader("🌎 Distribución de Usuarios por País")

df["country"] = df["country"].replace({
    "Arg": "Argentina",
    "Bra": "Brasil",
    "Chl": "Chile",
    "Col": "Colombia",
    "Mex": "México",
    "Mexico": "México",
    "Per": "Perú",
    "Peru": "Perú",
    "Ury": "Uruguay"
})

paises = df["country"].value_counts()

fig, ax = plt.subplots(figsize=(10,5))

ax.bar(
    paises.index,
    paises.values,
    edgecolor="black"
)

ax.set_title("Cantidad de usuarios por país")
ax.set_xlabel("País")
ax.set_ylabel("Cantidad de usuarios")

plt.xticks(rotation=45)

ax.grid(axis="y", alpha=0.3)

st.pyplot(fig)


st.success("""
### 📌 Interpretación

Este gráfico presenta la distribución de usuarios según su país de origen.

Permite identificar los países con mayor cantidad de usuarios registrados y observar si la población del dataset se encuentra distribuida de manera equilibrada o si existen países con una mayor representación.

Esta información resulta útil para comprender el alcance geográfico del servicio y detectar posibles mercados predominantes.
""")


# =====================================================
# GRÁFICO 4 - GÉNERO FAVORITO
# =====================================================

st.markdown("---")
st.subheader("🎬 Género favorito de los usuarios")

# Limpieza de nombres
df["favorite_genre"] = (
    df["favorite_genre"]
    .astype(str)
    .str.strip()
    .replace({
        "Action": "Acción",
        "Crime": "Crimen",
        "Documentary": "Documental",
        "Doc": "Documental",
        "Comedy": "Comedia",
        "Thriler": "Thriller",
        "None": "Sin dato",
        "nan": "Sin dato"
    })
)


# Contar géneros
generos = df["favorite_genre"].value_counts()

# Crear gráfico
fig, ax = plt.subplots(figsize=(10,5))

generos.plot(
    kind="bar",
    color="mediumpurple",
    edgecolor="black",
    ax=ax
)

ax.set_title("Cantidad de usuarios por género favorito")
ax.set_xlabel("Género")
ax.set_ylabel("Cantidad de usuarios")

plt.xticks(rotation=30)

st.pyplot(fig)


# Interpretación
st.info("""
**Interpretación**

Se observa la distribución de preferencias de los usuarios según su género favorito.
Esta información permite conocer qué tipo de contenido es más consumido dentro de la plataforma y puede utilizarse para mejorar los sistemas de recomendación.
""")


st.markdown("---")
st.subheader("⏱️ Tiempo mensual de visualización")

fig, ax = plt.subplots(figsize=(10,5))

ax.hist(
    df["monthly_watch_time_mins"].dropna(),
    bins=25,
    color="skyblue",
    edgecolor="black"
)

ax.set_title("Distribución del tiempo mensual de visualización")
ax.set_xlabel("Minutos")
ax.set_ylabel("Cantidad de usuarios")

st.pyplot(fig)


st.info("""
**Interpretación**

La mayor parte de los usuarios presenta un tiempo de visualización mensual concentrado en un rango determinado, mientras que existen algunos valores extremos que representan usuarios con un consumo significativamente mayor al promedio.
""")


st.markdown("---")
st.subheader("📦 Boxplot del tiempo de visualización")

fig, ax = plt.subplots(figsize=(8,2))

ax.boxplot(
    df["monthly_watch_time_mins"].dropna(),
    vert=False
)

ax.set_xlabel("Minutos")

st.pyplot(fig)


st.info("""
**Interpretación**

El boxplot permite identificar la mediana, la dispersión de los datos y la presencia de valores atípicos dentro del tiempo mensual de visualización.
""")


st.markdown("---")
st.subheader("📈 Matriz de correlación")

import seaborn as sns

# Variables numéricas
corr = df.select_dtypes(include=["int64", "float64"]).corr()

fig, ax = plt.subplots(figsize=(8,6))

sns.heatmap(
    corr,
    annot=True,
    cmap="Blues",
    linewidths=0.5,
    ax=ax
)

ax.set_title("Correlación entre variables numéricas")

st.pyplot(fig)


st.info("""
**Interpretación**

La matriz de correlación permite identificar el grado de relación entre las variables numéricas del conjunto de datos.

• Valores cercanos a 1 indican una correlación positiva fuerte.
        
• Valores cercanos a -1 indican una correlación negativa fuerte.
        
• Valores cercanos a 0 indican poca o ninguna relación lineal entre las variables.
""")
