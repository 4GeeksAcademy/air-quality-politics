# 🌍 # Beyond the AQI: Factors Influencing Mortality by Province

> “What is essential is invisible to the eye.” — Antoine de Saint-Exupéry

---

## 🎯 Project Objective

This project aims to predict the level of mortality (`low`, `medium`, `high`) across Spanish provinces based on environmental, sociodemographic, and political variables.

Using Machine Learning and a multidisciplinary approach, we explore how air quality, political context, urban/rural classification, and causes of death relate to public health outcomes.

---

## 🧠 Methodology

1. **Data Collection:**
   - Air quality data (OpenAQ, AEMET, Spanish Ministry)
   - Cause-specific mortality data (INE)
   - Political context by province
   - Sociodemographic variables

2. **Data Processing:**
   - Cleaning and normalization
   - Categorical encoding
   - Creation of the target variable `clase_mortalidad`

3. **Modeling:**
   - Random Forest classifier optimized with GridSearchCV
   - Evaluation using standard classification metrics

4. **Deployment:**
   - Interactive Streamlit web app
   - User input interface and real-time prediction

---

## 🚀 How to Run the App

1. Clone the repository:
```bash
git clone https://github.com/your_user/proyecto_mortalidad_aire.git
cd proyecto_mortalidad_aire
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Launch the app:
```bash
streamlit run app/app.py
```

---

## 📂 Project Structure

```
proyecto_mortalidad_aire/
│
├── app/
│   ├── app.py
│   ├── modelo_random_forest.pkl
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
```

---

## 👩‍💻 Authors

- María Pals  
- María Miura
- Ulla Aller

Data Science Bootcamp – 4Geeks Academy · June 2025


*Este proyecto está en desarrollo como parte del bootcamp de Data Science de 4Geeks Academy.*
