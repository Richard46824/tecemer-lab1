"""Pruebas del análisis de pronósticos meteorológicos."""

import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from analisis import analizar_pronostico


def test_analizar_pronostico_calcula_amplitud_y_categoria(tmp_path):
    csv_path = tmp_path / "pronostico.csv"
    pd.DataFrame(
        {
            "fecha": ["2026-10-01", "2026-10-02", "2026-10-03"],
            "temp_max": [21.0, 17.0, 12.0],
            "temp_min": [9.0, 8.0, 3.0],
            "precipitacion": [0.0, 1.5, 2.0],
        }
    ).to_csv(csv_path, index=False)

    df, resumen = analizar_pronostico(csv_path)

    assert df["amplitud_termica"].tolist() == [12.0, 9.0, 9.0]
    assert df["categoria"].tolist() == ["cálido", "templado", "frío"]
    assert df["dia_lluvioso"].tolist() == [False, True, True]
    assert resumen["dias"].sum() == 3


def test_analizar_pronostico_informa_columnas_faltantes(tmp_path):
    csv_path = tmp_path / "incompleto.csv"
    pd.DataFrame({"fecha": ["2026-10-01"], "temp_max": [20]}).to_csv(
        csv_path, index=False
    )

    with pytest.raises(ValueError, match="Faltan columnas requeridas"):
        analizar_pronostico(csv_path)
