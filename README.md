# 🌍 Análisis del Impacto de la Contaminación Atmosférica en la Mortalidad

## 🎯 Objetivo General

El objetivo de este proyecto es **analizar cómo influyen los niveles de contaminación atmosférica (ICA)** en la **tasa de mortalidad** por municipio o región, considerando también **factores sociodemográficos y políticos**. Se busca comprender si existen patrones o correlaciones relevantes que puedan orientar políticas públicas hacia una mejor calidad del aire y salud ciudadana.

## 📦 Variables Utilizadas

### ✅ Variables Independientes (features)
- **ICA promedio anual** (por municipio, provincia o comunidad autónoma)
- **Población total**
- **Edad media** o distribución por edad
- **Porcentaje de mayores de 65 años**
- **Sexo** (si se dispone de mortalidad desagregada por sexo)
- **Altitud del municipio**
- **Tipo de zona**: urbana / rural
- **Color político** del gobierno local o autonómico
- *(Opcional)* **Nivel educativo medio** o **renta media**

### 🎯 Variable Dependiente (target)
- **Tasa de mortalidad general anual**
- *(Alternativamente)* **Tasa de mortalidad por enfermedades respiratorias o cardiovasculares**, si se dispone de estos datos.

## 🛠️ Técnicas Aplicadas

- Análisis exploratorio de datos (**EDA**) con mapas, comparativas y series temporales.
- **Test estadísticos** de correlación y diferencias significativas: Pearson, ANOVA, t-test, etc.
- Modelos de **regresión lineal** y/o **regresión logística** (clasificación por rangos de mortalidad).
- Visualizaciones interactivas mediante **Streamlit** o dashboards.
- *(Opcional)* **Clustering** de municipios por perfiles de riesgo.


*Este proyecto está en desarrollo como parte del bootcamp de Data Science de 4Geeks Academy.*
