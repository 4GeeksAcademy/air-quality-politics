import pandas as pd
import numpy as np
import joblib
import os

# Ruta relativa para cargar las columnas que usa el modelo
path_columnas = os.path.join(os.path.dirname(__file__), '../models/columnas_modelo.pkl')
columnas_modelo = joblib.load(path_columnas)

def preparar_datos(df_input):
    df = df_input.copy()

    # Categorías fijas para que coincidan con entrenamiento
    df['tipo_area'] = pd.Categorical(df['tipo_area'], categories=['SUBURBANA', 'URBANA', 'RURAL'])
    df['causa_de_muerte'] = pd.Categorical(df['causa_de_muerte'], categories=[
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
    ])
    df['sexo'] = pd.Categorical(df['sexo'], categories=['Hombres', 'Mujeres'])
    df['partido'] = pd.Categorical(df['partido'], categories=['PP', 'PSOE', 'PSC', 'PNV', 'CiU', 'UPN', 'DO', 'CC', 'IU'])

    # One-hot encoding de variables categóricas
    df = pd.get_dummies(df, columns=['partido', 'tipo_area', 'causa_de_muerte', 'sexo'], drop_first=True)

    # Normalización acorde al entrenamiento
    df['valor_ica'] = df['valor_ica'] / 300  # máximo ICA esperado
    df['poblacion'] = np.log1p(df['poblacion'])
    df['altitud'] = df['altitud'] / 3000  # máximo altitud esperado

    # Añadir columnas que faltan para alinear con modelo
    for col in columnas_modelo:
        if col not in df.columns:
            df[col] = 0

    # Reordenar columnas según el orden usado en el modelo
    X = df[columnas_modelo]

    return X

