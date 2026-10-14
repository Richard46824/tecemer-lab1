"""Predice si observaciones meteorológicas nuevas serán lluviosas."""

import joblib
import numpy as np
from tensorflow import keras

# Ejecutar desde la carpeta semana04 después de preparar y entrenar el modelo.
modelo = keras.models.load_model("modelo_lluvia.keras")
escalador = joblib.load("escalador_lluvia.joblib")

# Valores en unidades originales: [temperatura máxima, temperatura mínima].
# Cambia estos ejemplos por las observaciones que quieras evaluar.
temperaturas_nuevas = np.array([
    [18.0, 7.0],
    [14.0, 4.0],
])

# Mantener el mismo orden de características utilizado durante el
# entrenamiento.
amplitud_termica = temperaturas_nuevas[:, 0] - temperaturas_nuevas[:, 1]
X_nuevo = np.column_stack(
    [temperaturas_nuevas[:, 0], temperaturas_nuevas[:, 1], amplitud_termica]
)
X_nuevo_escalado = escalador.transform(X_nuevo)

probabilidades = modelo.predict(X_nuevo_escalado, verbose=0).ravel()
predicciones = (probabilidades >= 0.5).astype(int)

for indice, (probabilidad, prediccion) in enumerate(
    zip(probabilidades, predicciones), start=1
):
    etiqueta = "lluvioso" if prediccion == 1 else "no lluvioso"
    print(
        f"Observación {indice}: probabilidad={probabilidad:.3f} "
        f"-> predicción: día {etiqueta}"
    )
