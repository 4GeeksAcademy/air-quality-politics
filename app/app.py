import streamlit as st
import os
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import gdown
from preprocesamiento import preparar_datos  # Ajusta según ruta real

st.set_page_config(page_title="Predicción de Mortalidad", layout="centered")

provincias_codigos = {
    "Álava": "01", "Albacete": "02", "Alicante": "03", "Almería": "04", "Ávila": "05",
    "Badajoz": "06", "Islas Baleares": "07", "Barcelona": "08", "Burgos": "09", "Cáceres": "10",
    "Cádiz": "11", "Castellón": "12", "Ciudad Real": "13", "Córdoba": "14", "A Coruña": "15",
    "Cuenca": "16", "Girona": "17", "Granada": "18", "Guadalajara": "19", "Guipúzcoa": "20",
    "Huelva": "21", "Huesca": "22", "Jaén": "23", "León": "24", "Lleida": "25", "La Rioja": "26",
    "Lugo": "27", "Madrid": "28", "Málaga": "29", "Murcia": "30", "Navarra": "31", "Ourense": "32",
    "Asturias": "33", "Palencia": "34", "Las Palmas": "35", "Pontevedra": "36", "Salamanca": "37",
    "Santa Cruz de Tenerife": "38", "Cantabria": "39", "Segovia": "40", "Sevilla": "41", "Soria": "42",
    "Tarragona": "43", "Teruel": "44", "Toledo": "45", "Valencia": "46", "Valladolid": "47",
    "Vizcaya": "48", "Zamora": "49", "Zaragoza": "50", "Ceuta": "51", "Melilla": "52"
}

url_modelo_drive = "https://drive.google.com/uc?id=1L3H0PgtyXa5hIaZHjpuPjXUGoggrRg6s"
ruta_modelo_local = "models/rf_pre_covid.pkl"

def descargar_modelo_si_no_existe(url, path):
    if not os.path.exists(path):
        st.info("Descargando modelo, por favor espera...")
        gdown.download(url, path, quiet=False)
    else:
        st.info("Modelo cargado desde disco local.")

descargar_modelo_si_no_existe(url_modelo_drive, ruta_modelo_local)

@st.cache_resource
def cargar_modelo(ruta):
    return joblib.load(ruta)

modelo = cargar_modelo(ruta_modelo_local)

st.title("Análisis y Predicción del Nivel de Mortalidad por Calidad del Aire")

st.markdown("""
Esta aplicación estima el nivel de mortalidad (**baja**, **media**, **alta**) según datos **ambientales**, **políticos** y **sociales**.
""")

partidos = [
    'PP - Partido Popular',
    'PSOE - Partido Socialista Obrero Español',
    'PSC - Partit dels Socialistes de Catalunya',
    'PNV - Partido Nacionalista Vasco',
    'CiU - Convergència i Unió',
    'UPN - Unión del Pueblo Navarro',
    'DO - Democracia Ourensana',
    'CC - Coalición Canaria',
    'IU - Izquierda Unida'
]
tipos_area = ['SUBURBANA', 'URBANA', 'RURAL']
sexos = ['Hombres', 'Mujeres']
causas_de_muerte = [
    '001-008  I.Enfermedades infecciosas y parasitarias',
    '009-041  II.Tumores',
    '042-043  III.Enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan al mecanismo de la inmunidad',
    '044-045  IV.Enfermedades endocrinas, nutricionales y metabólicas',
    '046-049  V.Trastornos mentales y del comportamiento',
    '050-052  VI-VIII.Enfermedades del sistema nervioso y de los órganos de los sentidos',
    '053-061 IX.Enfermedades del sistema circulatorio',
    '062-067  X.Enfermedades del sistema respiratorio',
    '068-072  XI.Enfermedades del sistema digestivo',
    '073  XII.Enfermedades de la piel y del tejido subcutáneo',
    '074-076  XIII.Enfermedades del sistema osteomuscular y del tejido conjuntivo',
    '077-080  XIV.Enfermedades del sistema genitourinario',
    '081  XV.Embarazo, parto y puerperio',
    '082  XVI.Afecciones originadas en el periodo perinatal',
    '083-085  XVII.Malformaciones congénitas, deformidades y anomalías cromosómicas',
    '086-089  XVIII.Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte',
    '090-102  XX.Causas externas de mortalidad'
]

valor_ica = st.slider("Valor ICA (calidad del aire)", min_value=0.0, max_value=150.0, value=50.0)

with st.form("formulario_prediccion"):
    provincia = st.selectbox("Provincia", list(provincias_codigos.keys()))
    codigo_provincia = provincias_codigos[provincia]
    altitud = st.number_input("Altitud (metros)", min_value=0, max_value=2100, value=50)
    sexo = st.selectbox("Sexo", sexos)
    tipo_area = st.selectbox("Tipo de área", tipos_area)
    poblacion = st.number_input("Población", min_value=0, max_value=4000000, value=100000)
    partido = st.selectbox("Partido político", partidos)
    causa_de_muerte = st.selectbox("Causa de muerte", causas_de_muerte)

    submitted = st.form_submit_button("Predecir")

if submitted:
    df_input = pd.DataFrame([{
        'provincias': provincia,
        'codigo_provincia': codigo_provincia,
        'valor_ica': valor_ica,
        'altitud': altitud,
        'sexo': sexo,
        'tipo_area': tipo_area,
        'poblacion': poblacion,
        'partido': partido.split(' - ')[0],
        'causa_de_muerte': causa_de_muerte
    }])

    X_input = preparar_datos(df_input)
    pred = modelo.predict(X_input)[0]
    proba = modelo.predict_proba(X_input)[0]

    colores_pred = {'baja': '#28a745', 'media': '#ffc107', 'alta': '#dc3545'}
    color_pred = colores_pred.get(pred, '#007bff')

    st.markdown(f"<h3 style='color:{color_pred}'>Predicción: {pred.upper()}</h3>", unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x=modelo.classes_, y=proba, palette=[colores_pred.get(c, '#007bff') for c in modelo.classes_], ax=ax)
    ax.set_ylim(0,1)
    ax.set_ylabel("Probabilidad")
    ax.set_xlabel("Nivel de mortalidad")
    ax.set_title("Probabilidades de Predicción")
    for i, v in enumerate(proba):
        ax.text(i, v + 0.02, f"{v:.2f}", ha='center', fontsize=10)
    st.pyplot(fig)
