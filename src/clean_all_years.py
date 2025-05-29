import pandas as pd
import os
import glob

def clean_all_years(input_dir="data/processed", output_path="data/clean/clima_todos.csv"):
    os.makedirs("data/clean", exist_ok=True)

    archivos = glob.glob(os.path.join(input_dir, "*.csv"))
    dfs = []

    for archivo in archivos:
        nombre = os.path.basename(archivo).replace(".csv", "")
        partes = nombre.split("_")
        if len(partes) != 2:
            print(f"❌ Nombre inesperado: {nombre}")
            continue

        ciudad, anio = partes[0], partes[1]
        try:
            df = pd.read_csv(archivo)

            # Fecha a datetime
            df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

            # Convertir columnas numéricas (coma -> punto)
            columnas_numericas = ["tmed", "prec", "tmin", "tmax", "hrMedia", "hrMax", "hrMin"]
            for col in columnas_numericas:
                if col in df.columns:
                    df[col] = df[col].astype(str).str.replace(",", ".", regex=False)
                    df[col] = pd.to_numeric(df[col], errors="coerce")

            # Añadir columnas útiles
            df["ciudad"] = ciudad.capitalize()
            df["anio"] = int(anio)

            dfs.append(df)
        except Exception as e:
            print(f"❌ Error limpiando {archivo}: {e}")

    if dfs:
        df_final = pd.concat(dfs, ignore_index=True)
        df_final.to_csv(output_path, index=False)
        print(f"✅ Datos consolidados guardados en: {output_path}")
        return df_final
    else:
        print("⚠️ No se encontraron archivos válidos para limpiar.")
        return None
s