"""Consulta el pronóstico de Huancayo y guarda los resultados en JSON y CSV."""

import csv
import json
from pathlib import Path

import requests

URL = "https://api.open-meteo.com/v1/forecast"
PARAMETROS = {
    "latitude": -12.07,
    "longitude": -75.21,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "America/Lima",
    "forecast_days": 7,
}
CARPETA = Path(__file__).resolve().parent


def obtener_pronostico():
    """Consulta la API y devuelve los datos diarios del pronóstico."""
    respuesta = requests.get(URL, params=PARAMETROS, timeout=10)
    respuesta.raise_for_status()
    datos = respuesta.json()
    if "daily" not in datos:
        raise ValueError("La respuesta de Open-Meteo no contiene datos diarios.")
    return datos


def guardar_pronostico(datos):
    """Guarda la respuesta completa en JSON y los datos diarios en CSV."""
    diario = datos["daily"]
    (CARPETA / "pronostico_huancayo.json").write_text(
        json.dumps(datos, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    filas = zip(
        diario["time"],
        diario["temperature_2m_max"],
        diario["temperature_2m_min"],
        diario["precipitation_sum"],
    )
    with (CARPETA / "pronostico_huancayo.csv").open(
        "w", newline="", encoding="utf-8"
    ) as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["fecha", "temp_max", "temp_min", "precipitacion"])
        escritor.writerows(filas)


def main():
    """Ejecuta la consulta y guarda los archivos generados."""
    try:
        datos = obtener_pronostico()
    except requests.exceptions.RequestException as error:
        raise SystemExit(f"No se pudo obtener el pronóstico: {error}") from error
    except ValueError as error:
        raise SystemExit(f"Respuesta de pronóstico no válida: {error}") from error

    print(json.dumps(datos["daily"], indent=2, ensure_ascii=False))
    print("Claves de primer nivel:", list(datos.keys()))
    print('Claves de "daily":', list(datos["daily"].keys()))
    print("Pronóstico guardado en semana02/pronostico_huancayo.json y .csv")


if __name__ == "__main__":
    main()
