# app/app.py

import streamlit as st
import pandas as pd
import joblib
from preprocesamiento import preparar_input

# Cargar modelo
model = joblib.load('models/modelo_random_forest_mortalidad.pkl')

# Título
st.title("Predicción del Nivel de Mortalidad por Provincia")
st.markdown("Esta aplicación estima el nivel de mortalidad (`baja`, `media`, `alta`) a partir de datos ambientales, políticos y sociales.")

# Inputs del usuario
valor_ica = st.slider("Valor ICA", 0, 300, 50)
altitud = st.number_input("Altitud (m)", value=200)
poblacion = st.number_input("Población", value=10000)
partido = st.selectbox("Partido político", ['PP', 'PSOE', 'PSC', 'PNV', 'CiU', 'UPN', 'DO', 'CC', 'IU'])
sexo = st.selectbox("Sexo", ['Hombres', 'Mujeres'])
tipo_area = st.selectbox("Tipo de zona", ['URBANA', 'SUBURBANA', 'RURAL'])
causa = st.selectbox("Causa de muerte", [
    '062-067  X.Enfermedades del sistema respiratorio',
    '009-041  II.Tumores',
    '053-061 IX.Enfermedades del sistema circulatorio',
    '044-045  IV.Enfermedades endocrinas, nutricionales y metabólicas'
    # Añadir más si es necesario
])

# Crear DataFrame con los inputs
input_dict = {
    'valor_ica': [valor_ica],
    'altitud': [altitud],
    'poblacion': [poblacion],
    'partido': [partido],
    'sexo': [sexo],
    'tipo_area': [tipo_area],
    'causa_de_muerte': [causa]
}
df_input = pd.DataFrame(input_dict)
st.write("🔍 Entrada del usuario (antes del preprocesamiento):")
st.dataframe(df_input)

# Cargar columnas del modelo y preprocesar
columnas_modelo = pd.read_csv("../data/df_procesado.csv", nrows=1).drop(columns=["clase_mortalidad"]).columns.tolist()
df_final = preparar_input(df_input, columnas_modelo)

# Predicción
if st.button("Predecir"):
    prediction = model.predict(df_final)[0]
    proba = model.predict_proba(df_final)[0]

    st.success(f"🔍 Predicción: **{prediction.upper()}**")
    st.write("📊 Probabilidades por clase:")
    st.write(dict(zip(model.classes_, proba)))