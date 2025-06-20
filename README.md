## 🔬 Más allá del ICA: Factores que influyen en la mortalidad por provincia

> “Lo esencial es invisible a los ojos.” — Antoine de Saint‑Exupéry

### 🎯 Objetivo del Proyecto  
Predecir el nivel de mortalidad (baja, media, alta) en las provincias españolas basado en variables ambientales, sociodemográficas y políticas.  
Con aprendizaje automático y un enfoque multidisciplinar, exploramos cómo la calidad del aire, el contexto político, la clasificación urbano/rural y las causas de muerte se relacionan con los resultados de salud pública.

### 🔍 Modelos desarrollados  
- **Pre‑COVID (hasta 2019)**: entrenado con datos “normales”, ofrece mejor rendimiento y menor ruido, será el modelo utilizado en la app.  
- **Completo (2013–2022)**: incluye datos antes, durante y después del COVID‑19; refleja impacto real, pero con más variabilidad. Se usa para análisis comparativos.

### 🧠 Metodología  
- **Recolección de datos**:  
  - Calidad del aire (OpenAQ, AEMET, MITECO)  
  - Mortalidad por causas específicas (INE, Sanidad)  
  - Variables políticas y demográficas  
- **Procesamiento**:  
  - Agrupación y limpieza de contaminantes, cálculo del ICA  
  - Normalización y codificación categórica  
  - Creación de `clase_mortalidad` por tercios  
- **Modelado**:  
  - Random Forest optimizado con `GridSearchCV`  
  - Evaluación mediante métricas clásicas y validación cruzada  
- **Despliegue**:  
  - App en Streamlit con predicción en tiempo real  
  - Interfaz amigable y visualizaciones claras

### 🚀 Cómo ejecutar la aplicación  
- **Clonar el repositorio:
    git clone https://github.com/your_user/proyecto_mortalidad_aire.git
    cd proyecto_mortalidad_aire
    Instalar dependencias:
    pip install -r requirements.txt
    Ejecutar la app:
    streamlit run app/app.py

📂 Estructura del proyecto

proyecto_mortalidad_aire/
│
├── app/
│   ├── app.py
│   ├── rf_pre_covid.pkl
│   ├── rf_completo.pkl
│   └── preprocesamiento.py
├── data/
│   └── df_procesado.csv
├── notebooks/
│   ├── 01_exploracion.ipynb
│   ├── 02_modelado.ipynb
│
├── img/
│   └── mapa_ica_provincias.png
├── requirements.txt
└── README.md
```
---
### ⚙️ Requisitos
-  Python 3.8+
    streamlit
    scikit-learn
    pandas
    matplotlib
    seaborn
    joblib
Instalar con:
pip install -r requirements.txt
### 👩‍💻 Autoras
María Pais

María Miura

Ulla Aller

Bootcamp Data Science – 4Geeks Academy · Junio 2025
### 📄 Licencia
Este proyecto está en desarrollo como parte del Bootcamp de Data Science de 4Geeks Academy.
