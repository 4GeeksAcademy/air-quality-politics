# 🌍 Air Quality & Politics

**Análisis y predicción de la calidad del aire en ciudades españolas en relación con las tendencias políticas locales.**

## 🎯 Objetivo

Este proyecto forma parte del trabajo final del bootcamp de Data Science en 4Geeks Academy. El objetivo es analizar y predecir la calidad del aire en las capitales de provincia de España, explorando su relación con variables meteorológicas y el signo político del gobierno local.

## 📦 Datos

- Calidad del aire: [MITECO](https://www.miteco.gob.es/es/calidad-y-evaluacion-ambiental/temas/atmosfera-y-calidad-del-aire/) y [OpenAQ](https://openaq.org/)
- Meteorología: [AEMET](https://www.aemet.es/es/datos_abiertos/AEMET_OpenData)
- Datos políticos: PHW/IFES, INE, Wikipedia
- Población: INE
- Contaminantes: PM2.5, PM10, NO2, SO2, CO, O3

## 🧱 Estructura

- `src/`: scripts de extracción, limpieza y modelado
- `data/`: datos crudos y procesados
- `models/`: modelos entrenados
- `notebooks/`: análisis exploratorio y modelado
- `app/`: demo interactiva en Streamlit

## 🧠 Modelos

- Modelos de clasificación:
  - Árboles de decisión
  - Random Forest
  - XGBoost
- Modelos de regresión:
  - Regresión lineal
  - Random Forest Regressor
- Modelos base para comparación:
  - DummyClassifier / DummyRegressor

## 🚀 Próximos pasos

- Automatizar ETL de AEMET
- Limpiar y unificar datasets
- Modelar clasificación y predicción de calidad del aire

*Este proyecto está en desarrollo como parte del bootcamp de Data Science de 4Geeks Academy.*
