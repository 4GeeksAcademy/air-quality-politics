import pandas as pd

def preparar_input(df_input, columnas_modelo):
    """
    Prepara el DataFrame de entrada del usuario con el mismo preprocesamiento usado para el modelo.
    - df_input: DataFrame con columnas como 'partido', 'sexo', etc.
    - columnas_modelo: lista de columnas que el modelo espera (en orden).
    """
    # One-hot encoding (igual que en entrenamiento)
    df_processed = pd.get_dummies(df_input, columns=['partido', 'tipo_area', 'causa_de_muerte', 'sexo'], drop_first=True)

    # Añadir columnas faltantes con 0 (por si el usuario no elige ciertas categorías)
    for col in columnas_modelo:
        if col not in df_processed.columns:
            df_processed[col] = 0

    # Reordenar columnas
    df_processed = df_processed[columnas_modelo]

    return df_processed
