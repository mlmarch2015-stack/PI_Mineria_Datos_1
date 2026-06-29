import streamlit as st

# ---------------------------------------------------
# CONFIGURACIÓN
# ---------------------------------------------------

st.set_page_config(
    page_title="Conclusiones",
    page_icon="✅",
    layout="wide"
)

# ---------------------------------------------------
# TÍTULO
# ---------------------------------------------------

st.title("✅ Conclusiones del Proyecto")

st.info(
    """
En esta sección se presentan las principales conclusiones obtenidas
a partir del análisis exploratorio de datos (EDA) y la aplicación
del algoritmo de Análisis de Componentes Principales (PCA).
"""
)

st.markdown("---")

# ---------------------------------------------------
# CONCLUSIONES
# ---------------------------------------------------

st.subheader("📌 Principales resultados")

st.success("""
**• Se analizaron correctamente los datos de usuarios de una plataforma de streaming.**

**• Se identificaron valores faltantes y valores atípicos durante la exploración del dataset.**

**• La distribución de edades mostró una concentración en usuarios adultos jóvenes.**

**• Los planes Básico, Estándar y Premium fueron los más utilizados.**

**• Los países presentaron una distribución relativamente uniforme de usuarios.**

**• Los géneros favoritos se distribuyeron de forma equilibrada entre las distintas categorías disponibles.**

**• La matriz de correlación mostró relaciones lineales muy bajas entre las variables numéricas.**

**• La aplicación de PCA permitió reducir la dimensionalidad del conjunto de datos conservando una parte importante de la información.**
""")

st.markdown("---")

st.subheader("📈 Conclusión General")

st.write("""
El proyecto permitió aplicar de manera práctica técnicas de inspección,
limpieza, análisis exploratorio de datos (EDA) y reducción de
dimensionalidad mediante PCA.

Las visualizaciones facilitaron la comprensión del comportamiento del
conjunto de datos y permitieron detectar patrones, distribuciones,
valores faltantes y posibles valores atípicos.

Finalmente, la utilización de PCA permitió representar la información
en un espacio reducido, facilitando su interpretación y demostrando la
utilidad de esta técnica para el análisis de grandes volúmenes de datos.
""")

st.markdown("---")

st.success("🎉 Proyecto Integrador finalizado correctamente.")

st.caption("Proyecto Integrador - Minería de Datos I | ITSE 2026")
