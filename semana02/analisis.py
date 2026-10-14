
"""Analiza el pronóstico guardado y genera resúmenes en CSV."""

from pathlib import Path

import pandas as pd

CARPETA = Path(__file__).resolve().parent


def analizar_pronostico(ruta_csv=CARPETA / "pronostico_huancayo.csv"):
    """Carga y analiza el CSV.

    Devuelve el DataFrame y el resumen por categoría.
    """
    df = pd.read_csv(ruta_csv)

    columnas_requeridas = {
        "fecha",
        "temp_max",
        "temp_min",
        "precipitacion",
    }
    faltantes = columnas_requeridas.difference(df.columns)

    if faltantes:
        raise ValueError(
            f"Faltan columnas requeridas: {sorted(faltantes)}"
        )

    df["fecha"] = pd.to_datetime(df["fecha"], errors="raise")
    df["amplitud_termica"] = df["temp_max"] - df["temp_min"]
    df["dia_lluvioso"] = df["precipitacion"] > 0

    df["categoria"] = df["temp_max"].apply(
        lambda temperatura: (
            "cálido"
            if temperatura >= 20
            else "templado"
            if temperatura >= 15
            else "frío"
        )
    )

    resumen = df.groupby("categoria").agg(
        dias=("categoria", "count"),
        temp_max_promedio=("temp_max", "mean"),
        precipitacion_total=("precipitacion", "sum"),
    )

    return df, resumen


def main():
    """Genera los archivos procesados a partir del CSV de pronóstico."""
    try:
        df, resumen = analizar_pronostico()
    except (OSError, ValueError, pd.errors.ParserError) as error:
        raise SystemExit(
            f"No se pudo analizar el pronóstico: {error}"
        ) from error

    print(df.head())
    print(df.info())
    print(df)
    print(df.describe())
    print(resumen)

    df.to_csv(
        CARPETA / "pronostico_huancayo_procesado.csv",
        index=False,
    )
    resumen.to_csv(CARPETA / "resumen_por_categoria.csv")

    print("Archivos procesados guardados en la carpeta semana02.")


if __name__ == "__main__":
    main()
