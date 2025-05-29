import pandas as pd
import os
import glob

def clean_and_combine_data(input_dir="data/processed", output_path="data/clean/clima_2023.csv"):
    os.makedirs("data/clean", exist_ok=True)

    # Solo archivos de 2023
    archivos = glob.glob(os.path.join(input_dir, "*_2023.csv"))
    dfs = []

    for archivo in archivos:
        ciudad = os.path.basename(archivo).split("_")[0]
        try:
            df = pd.read_csv(archivo)

            # Convertir fecha
            df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

            # Columnas numéricas
            columnas_numericas = ["tmed", "prec", "tmin", "tmax", "hrMedia", "hrMax", "hrMin"]
            for col in columnas_numericas:
                if col in df.columns:
                    df[col] = df[col].astype(str).str.replace(",", ".", regex=False)
                    df[col] = pd.to_numeric(df[col], errors="coerce")

            df["ciudad"] = ciudad.capitalize()
            dfs.append(df)
        except Exception as e:
            print(f"❌ Error procesando {archivo}: {e}")

    if dfs:
        df_final = pd.concat(dfs, ignore_index=True)
        df_final.to_csv(output_path, index=False)
        print(f"✅ Datos limpios guardados en: {output_path}")
        return df_final
    else:
        print("⚠️ No se encontraron archivos de 2023.")
        return None
