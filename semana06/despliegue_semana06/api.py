
from pathlib import Path

import joblib
import numpy as np
from flask import Flask, jsonify, request
from tensorflow import keras

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
MODELO_PATH = BASE_DIR / "modelo_produccion.keras"
ESCALADOR_PATH = BASE_DIR / "escalador_produccion.pkl"

modelo = keras.models.load_model(MODELO_PATH)
escalador = joblib.load(ESCALADOR_PATH)


def calcular_prediccion(temp_max, temp_min):
    amplitud_termica = temp_max - temp_min

    X = np.array(
        [[temp_max, temp_min, amplitud_termica]],
        dtype=float,
    )

    X_escalado = escalador.transform(X)
    probabilidad = float(modelo.predict(X_escalado, verbose=0)[0][0])

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
    return jsonify({
        "estado": "ok",
        "modelo_cargado": True,
    }), 200


@app.post("/predecir")
def predecir():
    datos = request.get_json(silent=True)

    if not isinstance(datos, dict) or not datos:
        return jsonify({"error": "Se requiere un objeto JSON."}), 400

    requeridos = ["temp_max", "temp_min", "viento_max"]
    faltantes = [campo for campo in requeridos if campo not in datos]

    if faltantes:
        return jsonify({
            "error": "Faltan campos obligatorios.",
            "campos_faltantes": faltantes,
        }), 400

    for campo in requeridos:
        valor = datos[campo]
        if (
            isinstance(valor, bool)
            or not isinstance(valor, (int, float))
            or not np.isfinite(valor)
        ):
            return jsonify({
                "error": f"El campo '{campo}' debe ser numérico y finito."
            }), 400

    if datos["temp_min"] > datos["temp_max"]:
        return jsonify({
            "error": "temp_min no puede superar temp_max."
        }), 400

    return jsonify(
        calcular_prediccion(datos["temp_max"], datos["temp_min"])
    ), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
