import streamlit as st
from PIL import Image
from pathlib import Path

# ---------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------------------------------

st.set_page_config(
    page_title="Proyecto Integrador - Minería de Datos I",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# LOGO
# ---------------------------------------------------

logo_path = Path("assets/logo_itse.png")

if logo_path.exists():
    logo = Image.open(logo_path)
    st.image(logo, width=120)

# ---------------------------------------------------
# TÍTULO
# ---------------------------------------------------

st.title("📊 Proyecto Integrador")

st.subheader("Minería de Datos I")

st.caption(
    "Análisis Exploratorio y Reducción de Dimensionalidad de Usuarios de una Plataforma de Streaming"
)

st.markdown("---")

# ---------------------------------------------------
# INFORMACIÓN DEL PROYECTO
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    st.info("""
### 👩‍💻 Integrantes

- Marcia Lovaiza
- Soledad Ríos
""")

with col2:
    st.success("""
### 🎯 Objetivo

Analizar un conjunto de datos de usuarios de una plataforma de streaming utilizando técnicas de inspección, limpieza, análisis exploratorio (EDA) y reducción de dimensionalidad mediante PCA.
""")

st.markdown("---")

# ---------------------------------------------------
# RESUMEN DEL PROYECTO
# ---------------------------------------------------

st.subheader("📌 Resumen del Proyecto")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("👥 Registros", "8.160")

with c2:
    st.metric("📑 Variables", "8")

with c3:
    st.metric("📓 Cuadernos", "5")

with c4:
    st.metric("📉 PCA", "Aplicado")

st.markdown("---")

st.caption("Proyecto Integrador - Minería de Datos I | ITSE 2026")