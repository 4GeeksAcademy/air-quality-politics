# 🔬 MÁS ALLÁ DEL ICA: Factores que influyen en la mortalidad por provincia

> “Lo esencial es invisible a los ojos.” — Antoine de Saint‑Exupéry

**Accede directamente a la app aquí** 👉 [Abrir aplicación Streamlit](https://air-quality-politics-7zt2ipxuaappvamjddjimw7.streamlit.app/)

---

### 🎯 Objetivo del Proyecto  
Predecir el nivel de mortalidad (baja, media, alta) en las provincias españolas basado en variables ambientales, sociodemográficas y políticas.  
Con aprendizaje automático y un enfoque multidisciplinar, exploramos cómo la calidad del aire, el contexto político, la clasificación urbano/rural y las causas de muerte se relacionan con los resultados de salud pública.

### 🔍 Modelos desarrollados  
- **Pre‑COVID (hasta 2019)**: entrenado con datos “normales”, ofrece mejor rendimiento y menor ruido, será el modelo utilizado en la app.  
- **Completo (2013–2022)**: incluye datos antes, durante y después del COVID‑19; refleja impacto real, pero con más variabilidad. Se usa para análisis comparativos.

### 🧠 Metodología  
- **Recolección de datos**:  
  - Calidad del aire (OpenAQ, MITECO)  
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

---

### 🚀 Cómo ejecutar la aplicación  

```bash
# Clonar el repositorio
git clone https://github.com/ullaom/air-quality-politics.git
cd air-quality-politics

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la app
streamlit run app/app.py
```

---

### 📂 Estructura del proyecto

```
air-quality-politics/
│
├── app/
│   ├── app.py
│   ├── preprocesamiento.py
│   ├── models/
│   │   └── columnas_modelo.pkl
├── data/
│   └── df_procesado.csv
├── notebooks/
│   ├── 01_exploracion.ipynb
├── requirements.txt
└── README.md
```

---

### ⚙️ Requisitos

- Python 3.8+
- streamlit  
- scikit-learn  
- pandas  
- matplotlib  
- seaborn  
- joblib  
- requests

Para instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

### 👩‍💻 Autoras

- María Pais  
- Ulla Aller  
- María Miura

