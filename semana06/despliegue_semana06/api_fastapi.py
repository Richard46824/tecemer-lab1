
from pathlib import Path

import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field
from tensorflow import keras

BASE_DIR = Path(__file__).resolve().parent

modelo = keras.models.load_model(
    BASE_DIR / "modelo_produccion.keras"
)
escalador = joblib.load(
    BASE_DIR / "escalador_produccion.pkl"
)

app = FastAPI(
    title="API de Predicción de Lluvia",
    description="Despliegue académico de la Semana 6.",
    version="1.0.0",
)


class DatosClima(BaseModel):
    model_config = ConfigDict(extra="forbid")

    temp_max: float = Field(allow_inf_nan=False)
    temp_min: float = Field(allow_inf_nan=False)
    viento_max: float = Field(allow_inf_nan=False, ge=0)


def calcular_prediccion(temp_max, temp_min):
    amplitud_termica = temp_max - temp_min
    X = np.array(
        [[temp_max, temp_min, amplitud_termica]],
        dtype=float,
    )
    X_escalado = escalador.transform(X)
    probabilidad = float(
        modelo.predict(X_escalado, verbose=0)[0][0]
    )

    return {
        "prediccion": (
            "día lluvioso" if probabilidad >= 0.5
            else "día no lluvioso"
        ),
        "probabilidad": round(probabilidad, 4),
        "nota": "El modelo no utiliza viento_max como característica.",
    }


@app.get("/salud")
def salud():
    return {"estado": "ok", "modelo_cargado": True}


@app.post("/predecir")
def predecir(datos: DatosClima):
    if datos.temp_min > datos.temp_max:
        from fastapi import HTTPException

        raise HTTPException(
            status_code=422,
            detail="temp_min no puede superar temp_max.",
        )

    return calcular_prediccion(
        datos.temp_max,
        datos.temp_min,
    )

