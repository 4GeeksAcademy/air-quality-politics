Más allá del ICA: Factores que influyen en la mortalidad por provincia
    “Lo esencial es invisible a los ojos.” — Antoine de Saint-Exupéry
:dardo: Objetivo del Proyecto
Este proyecto tiene como objetivo predecir el nivel de mortalidad (baja, media, alta) en las provincias españolas basado en variables ambientales, sociodemográficas y políticas.
Mediante aprendizaje automático y un enfoque multidisciplinar, exploramos cómo la calidad del aire, el contexto político, la clasificación urbano/rural y las causas de muerte se relacionan con los resultados de salud pública.
:lupa: Modelos desarrollados:
Se entrenaron y probaron dos modelos principales para abordar el problema:
    Modelo Pre-COVID:
    Entrenado con datos anteriores a 2020 para capturar patrones de mortalidad en condiciones “normales”. Este modelo ofrece mejor desempeño y menos ruido, por lo que será el modelo final usado en la app.
    Modelo Completo (desde 2013 a 2022):
    Incluye datos antes,durante y después de la pandemia COVID-19, lo que introduce un aumento abrupto y atípico en la mortalidad. Aunque refleja el impacto real, es más ruidoso y menos preciso. Se usa principalmente para análisis comparativos y estudios de sensibilidad.
:cerebro: Metodología
    Recolección de datos:
        Calidad del aire (OpenAQ, AEMET, Ministerio de Transición Ecológica)
        Mortalidad por causas específicas (INE, Ministerio de Sanidad)
        Contexto político y variables sociodemográficas
    Procesamiento:
        Agrupacion de tablas de contaminantes, obtención del indicador ICA, limpieza, normalización y codificación categórica
        Creación de la variable objetivo clase_mortalidad (tertiles de mortalidad)
    Modelado:
        Random Forest optimizado con GridSearchCV
        Evaluación con métricas clásicas y validación cruzada
    Despliegue:
        Aplicación Streamlit para predicción en tiempo real
        Interfaz amigable y visualizaciones claras
:cohete: Cómo ejecutar la aplicación
    Clonar el repositorio:
    git clone https://github.com/your_user/proyecto_mortalidad_aire.git
    cd proyecto_mortalidad_aire
    Instalar dependencias:
    pip install -r requirements.txt
    Ejecutar la app:
    streamlit run app/app.py
:carpeta_abierta: Estructura del proyecto
proyecto_mortalidad_aire/
│
├── app/
│   ├── app.py
│   ├── rf_pre_covid.pkl
│   ├── rf_completo.pkl
│   └── preprocesamiento.py
│
├── data/
│   ├── df_procesado.csv
│
├── notebooks/
│   ├── 01_exploracion.ipynb
│   ├── 02_modelado.ipynb
│
├── img/
│   └── mapa_ica_provincias.png
│
├── requirements.txt
└── README.md
:engranaje: Requisitos
    Python 3.8+
    streamlit
    scikit-learn
    pandas
    matplotlib
    seaborn
    joblib
Instalar con:
pip install -r requirements.txt
:tecnóloga: Autoras
    María Pais
    María Miura
    Ulla Aller
Bootcamp de Data Science – 4Geeks Academy · Junio 2025
:página_boca_arriba: Licencia
Este proyecto está en desarrollo como parte del bootcamp de Data Science de 4Geeks Academy.

Bootcamp de Data Science – 4Geeks Academy · Junio 2025

📄 Licencia

Este proyecto está en desarrollo como parte del bootcamp de Data Science de 4Geeks Academy.
