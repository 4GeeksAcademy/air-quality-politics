import requests
import pandas as pd
import os
from time import sleep

API_KEY = os.getenv("AEMET_API_KEY")

BASE_URL = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos"

def get_data_url(start_date, end_date, station_id):
    endpoint = f"{BASE_URL}/fechaini/{start_date}T00:00:00UTC/fechafin/{end_date}T00:00:00UTC/estacion/{station_id}"
    response = requests.get(endpoint, params={"api_key": API_KEY})
    if response.status_code == 200:
        return response.json()["datos"]
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
        return None

def download_data(year, station_id, city_name):
    semestres = [
        (f"{year}-01-01", f"{year}-06-30"),
        (f"{year}-07-01", f"{year}-12-31")
    ]
    all_data = []

    for start_date, end_date in semestres:
        print(f"📆 Descargando {city_name} ({start_date} a {end_date})")
        url = get_data_url(start_date, end_date, station_id)
        if url:
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    all_data.extend(data)
                    sleep(10)
                except Exception as e:
                    print(f"⚠️ Error leyendo JSON: {e}")
            else:
                print(f"❌ Error al descargar: {response.status_code}")
        else:
            print(f"⚠️ No se obtuvo URL para {city_name} ({start_date} a {end_date})")

    if all_data:
        df = pd.DataFrame(all_data)
        os.makedirs("data/processed", exist_ok=True)
        out_path = f"data/processed/{city_name}_{year}.csv"
        df.to_csv(out_path, index=False)
        print(f"✅ Guardado: {out_path}")
        return df
    else:
        print(f"❌ No se obtuvieron datos válidos para {city_name} ({year})")
        return None

def batch_download(station_map, years):
    for city, station_id in station_map.items():
        for year in years:
            print(f"📥 Descargando: {city} - {year}")
            try:
                download_data(year, station_id, city)
            except Exception as e:
                print(f"❌ Error en {city}-{year}: {e}")
import os
import requests
import time
import pandas as pd
from io import StringIO

def download_aemet(city, station_id, year):
    os.makedirs("data/processed", exist_ok=True)

    print(f"📆 Descargando {city} ({year}-01-01 a {year}-12-31)")
    url = f"https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/anio/{year}/estacion/{station_id}"
    headers = {"accept": "application/json", "api_key": os.getenv("AEMET_API_KEY")}  # usa variable de entorno

    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        raise Exception(f"Error al pedir URL de datos: {res.status_code} – {res.text}")

    data_url = res.json().get("datos")
    if not data_url:
        raise Exception("❌ No se obtuvo URL de datos.")

    time.sleep(1)  # para respetar el rate limit
    csv_res = requests.get(data_url)
    if csv_res.status_code != 200:
        raise Exception(f"Error al descargar CSV: {csv_res.status_code} – {csv_res.text}")

    df = pd.read_csv(StringIO(csv_res.content.decode("utf-8")), sep=";", decimal=",")
    df.to_csv(f"data/processed/{city}_{year}.csv", index=False)
    print(f"✅ Guardado: {city}_{year}.csv")
import os
import requests
import time
import pandas as pd
from io import StringIO

def download_aemet(city, station_id, year):
    os.makedirs("data/processed", exist_ok=True)

    print(f"📆 Descargando {city} ({year}-01-01 a {year}-12-31)")
    url = f"https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/anio/{year}/estacion/{station_id}"
    headers = {
        "accept": "application/json",
        "api_key": os.getenv("AEMET_API_KEY")  # Usa la variable del archivo .env
    }

    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        raise Exception(f"Error al pedir URL de datos: {res.status_code} – {res.text}")

    data_url = res.json().get("datos")
    if not data_url:
        raise Exception("❌ No se obtuvo URL de datos.")

    time.sleep(1)  # respetar límites de la API
    csv_res = requests.get(data_url)
    if csv_res.status_code != 200:
        raise Exception(f"Error al descargar CSV: {csv_res.status_code} – {csv_res.text}")

    df = pd.read_csv(StringIO(csv_res.content.decode("utf-8")), sep=";", decimal=",")
    df.to_csv(f"data/processed/{city}_{year}.csv", index=False)
    print(f"✅ Guardado: {city}_{year}.csv")
