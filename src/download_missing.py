import os
from extract_aemet import download_aemet
from station_map import station_map

def download_missing_years():
    data_path = "data/processed"
    expected_years = [str(y) for y in range(2013, 2024)]

    for city, code in station_map.items():
        missing_years = []
        for year in expected_years:
            filename = f"{city}_{year}.csv"
            filepath = os.path.join(data_path, filename)
            if not os.path.exists(filepath):
                missing_years.append(year)

        if missing_years:
            print(f"📌 {city} - años faltantes: {missing_years}")
            for year in missing_years:
                try:
                    download_aemet(city, code, year)
                except Exception as e:
                    print(f"❌ Error al descargar {city}-{year}: {e}")
