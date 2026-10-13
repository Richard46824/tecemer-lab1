"""Entrena y evalúa un clasificador neuronal de lluvia."""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from tensorflow import keras
from tensorflow.keras import layers


def main():
    """Carga los datos preparados, compara modelos y guarda resultados."""
    # 1. Cargar los arreglos preparados.
    datos = np.load("dataset_preparado.npz")
    X_train, X_test = datos["X_train"], datos["X_test"]
    y_train, y_test = datos["y_train"], datos["y_test"]

    print("X_train:", X_train.shape, " X_test:", X_test.shape)
    print("Proporción de días lluviosos en train:", y_train.mean().round(3))

    # 2. Modelo de referencia: regresión logística.
    baseline = LogisticRegression()
    baseline.fit(X_train, y_train)
    pred_baseline = baseline.predict(X_test)
    precision_baseline = accuracy_score(y_test, pred_baseline)
    print(
        f"\nPrecisión del baseline (regresión logística): "
        f"{precision_baseline:.4f}"
    )

    # 3. Definir, compilar y entrenar la red neuronal.
    modelo = keras.Sequential(
        [
            layers.Input(shape=(X_train.shape[1],)),
            layers.Dense(8, activation="relu"),
            layers.Dense(4, activation="relu"),
            layers.Dense(1, activation="sigmoid"),
        ]
    )
    modelo.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )
    historial = modelo.fit(
        X_train,
        y_train,
        epochs=40,
        batch_size=8,
        validation_split=0.2,
        verbose=1,
    )

    # 4. Evaluar una sola vez sobre el conjunto de prueba.
    perdida_test, precision_test = modelo.evaluate(X_test, y_test, verbose=0)
    print(f"\nPérdida del MLP en test: {perdida_test:.4f}")
    print(f"Precisión del MLP en test: {precision_test:.4f}")
    print(f"Precisión del baseline en test: {precision_baseline:.4f}")

    # 5. Graficar la pérdida durante el entrenamiento.
    plt.figure(figsize=(6, 4))
    plt.plot(historial.history["loss"], label="entrenamiento")
    plt.plot(historial.history["val_loss"], label="validación")
    plt.title("Pérdida — clasificador de lluvia (Huancayo)")
    plt.xlabel("Época")
    plt.legend()
    plt.tight_layout()
    plt.savefig("curvas_entrenamiento_lluvia.png", dpi=100)
    plt.close()
    print("\nGráfico guardado en curvas_entrenamiento_lluvia.png")

    # 6. Guardar el modelo entrenado.
    modelo.save("modelo_lluvia.keras")
    print("\nModelo guardado en modelo_lluvia.keras")


if __name__ == "__main__":
    main()
