## 🔬 Más allá del ICA: Factores que influyen en la mortalidad por provincia

> “Lo esencial es invisible a los ojos.” — Antoine de Saint‑Exupéry

### 🎯 Objetivo del Proyecto  
Predecir el nivel de mortalidad (baja, media, alta) en las provincias españolas según variables ambientales, sociodemográficas y políticas. Con aprendizaje automático, examinamos cómo la calidad del aire, el entorno político, el carácter urbano/rural y las causas de muerte afectan la salud pública.

### 🧠 Modelos desarrollados  
- **Pre‑COVID (≤2019)**: entrenado con datos “normales”, ofrece mejor rendimiento y será el modelo utilizado en la app.  
- **Completo (2013‑2022)**: incorpora el impacto de la pandemia—mayor ruido, menos precisión—pero útil para análisis comparativos y sensibilidad.

### ⚙️ Metodología  
- **Recolección de datos**: aire (OpenAQ, AEMET, MITECO), mortalidad (INE, Sanidad), políticos y demográficos.  
- **Procesamiento**: cálculo del ICA, limpieza, codificación y creación de `clase_mortalidad` por tercios.  
- **Modelado**: Random Forest optimizado con `GridSearchCV`, validado con técnicas cruzadas.  
- **Despliegue**: app en Streamlit con visualizaciones y predicción en tiempo real.

---

### 📊 Resumen EDA (Exploratorio de Datos)

- **Datos**: 142 164 registros; `Muertes_por_causa` está muy sesgada (media ≈129, máximo ≈6 345).  
- **Predictoras examinadas**: ICA, geografía, partido político, sexo, población.  
- **Correlaciones lineales débiles**:  
  - ICA (r ≈ 0.085)  
  - Población (r ≈ 0.125)  
  - Altitud (r ≈ –0.115)  
- **Desbalance en ICA**: “Buena” domina; “Razonablemente buena” y “Desfavorable” se concentran más en áreas urbanas/suburbanas.  
- **Normalización necesaria**:  
  - Uso de logaritmos o cálculo de tasas por 100 000 habitantes por la gran disparidad poblacional.  
- **Patrones significativos**:  
  - Meses con ICA > 30 coinciden con incrementos locales de mortalidad (ej. Barcelona).  
  - Aumento notable en 2020 debido al COVID.  
- **Análisis estadístico final**:  
  - Creamos `muertes_por_100k` y categorizamos `Riesgo_ICA` (bajo/medio/alto).  
  - Test de Kruskal–Wallis muestra diferencias estadísticamente significativas entre grupos (p < 0.05), vinculado peores niveles de ICA con mayor mortalidad.

------

### 🚀 Cómo ejecutar la aplicación  
- **Clonar el repositorio**  
  ```bash
  git clone https://github.com/your_user/proyecto_mortalidad_aire.git  
  cd proyecto_mortalidad_aire
Instalar dependencias

bash
Copiar
Editar
pip install -r requirements.txt
Ejecutar la app

bash
Copiar
Editar
streamlit run app/app.py
📂 Estructura del proyecto
css
Copiar
Editar
proyecto_mortalidad_aire/
├── app/
│   ├── app.py
│   ├── rf_pre_covid.pkl
│   ├── rf_completo.pkl
│   └── preprocesamiento.py
├── data/
│   └── df_procesado.csv
├── notebooks/
│   ├── 01_exploracion.ipynb
│   └── 02_modelado.ipynb
├── img/
│   └── mapa_ica_provincias.png
├── requirements.txt
└── README.md
⚙️ Requisitos
Python ≥ 3.8

Librerías necesarias:

streamlit

scikit‑learn

pandas

matplotlib

seaborn

joblib

Instalación:

bash
Copiar
Editar
pip install -r requirements.txt
👩‍💻 Autoras
María Pais

María Miura

Ulla Aller
Bootcamp de Data Science – 4Geeks Academy · Junio 2025

📄 Licencia
Este proyecto está en desarrollo como parte del Bootcamp de Data Science de 4Geeks Academy.
