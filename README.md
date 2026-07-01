# 📊 Proyecto Integrador - Minería de Datos I

## Información general

Proyecto Integrador de la asignatura **Minería de Datos I** – ITSE 2026.

**Integrantes**
- Marcia Lovaiza
- Soledad Ríos

---

## Objetivo del proyecto

Analizar un conjunto de datos de usuarios de una plataforma de streaming mediante técnicas de inspección, limpieza, análisis exploratorio de datos (EDA) y reducción de dimensionalidad utilizando PCA, comunicando los resultados mediante una aplicación desarrollada en Streamlit.

---

## Dataset

Se trabajó con un conjunto de datos de usuarios de una plataforma de streaming. El dataset contiene variables demográficas, preferencias de contenido y características de uso de la plataforma. Se realizó una inspección inicial para evaluar la calidad de los datos antes de comenzar el análisis.

---

## Estructura del repositorio

```
PI_Mineria_Datos_1/
├── app/
├── assets/
├── data/
├── logs/
├── notebooks/
├── reports/
├── README.md
└── requirements.txt
```

---

## Preparación y calidad de datos

Se realizó la inspección inicial del conjunto de datos, identificando valores faltantes, registros duplicados y tipos de datos. Posteriormente se efectuaron las tareas de limpieza, transformación y preparación necesarias para obtener un dataset consistente para el análisis.

---

## Resumen del análisis exploratorio (EDA)

Se desarrolló un análisis univariado, bivariado y multivariado para identificar patrones, distribuciones y relaciones entre las variables del dataset. Los resultados permitieron comprender mejor el comportamiento de los usuarios y apoyar las conclusiones del proyecto.

---

## Reducción de dimensionalidad (PCA)

Se aplicó escalamiento de variables y posteriormente el algoritmo PCA para reducir la dimensionalidad del conjunto de datos, analizando la varianza explicada por los componentes principales y facilitando la interpretación de la información.

---

## Visualización interactiva

Aplicación desarrollada con Streamlit:

**https://pi-mineria-marcia.streamlit.app**

Repositorio GitHub:

**https://github.com/mlmarch2015-stack/PI_Mineria_Datos_1**

---

## Cómo ejecutar el proyecto localmente

```bash
pip install -r requirements.txt
streamlit run app/Home.py
```

---

## Conclusiones

El proyecto permitió aplicar las principales etapas del proceso de minería de datos: inspección, limpieza, análisis exploratorio y reducción de dimensionalidad. La aplicación desarrollada en Streamlit facilita la comunicación de los resultados obtenidos de forma clara e interactiva.
