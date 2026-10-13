"""Prepara el dataset meteorológico para clasificar días lluviosos."""

import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def calcular_dia_lluvioso(precipitacion):
    """Devuelve 1 si hubo precipitación, y 0 en caso contrario."""
    return int(precipitacion > 0)


def main():
    """Carga, prepara y guarda los datos para el entrenamiento."""
    # 1. Cargar el dataset construido en la Semana 2.
    df = pd.read_csv("pronostico_huancayo.csv")

    print("Dimensiones del dataset:", df.shape)
    print("\nColumnas disponibles:")
    print(df.columns.tolist())
    print("\nPrimeras filas:")
    print(df.head())
    print("\nValores nulos por columna:")
    print(df.isnull().sum())

    # 2. Construir la variable objetivo binaria.
    df["dia_lluvioso"] = df["precipitacion"].apply(calcular_dia_lluvioso)

    # 3. Crear una característica derivada.
    df["amplitud_termica"] = df["temp_max"] - df["temp_min"]

    # 4. Seleccionar las características (X) y el objetivo (y).
    columnas_features = ["temp_max", "temp_min", "amplitud_termica"]
    X = df[columnas_features].copy()
    y = df["dia_lluvioso"].copy()

    print("\nDistribución de la variable objetivo (0 = no lluvioso, 1 = lluvioso):")
    print(y.value_counts())
    print("\nEstadísticas descriptivas de las características:")
    print(X.describe())

    # 5. Eliminar filas con valores nulos.
    antes = len(X)
    datos_completos = pd.concat([X, y], axis=1).dropna()
    X = datos_completos[columnas_features]
    y = datos_completos["dia_lluvioso"]
    print(f"\nFilas eliminadas por valores nulos: {antes - len(X)}")

    # 6. Partición train/test (80 % / 20 %).
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    # 7. Escalar usando solo los datos de entrenamiento para ajustar.
    escalador = StandardScaler()
    X_train_esc = escalador.fit_transform(X_train)
    X_test_esc = escalador.transform(X_test)

    # Guardar el escalador para transformar observaciones nuevas igual que train.
    joblib.dump(escalador, "escalador_lluvia.joblib")
    print("Escalador guardado en escalador_lluvia.joblib")

    print(f"\nTamaño de entrenamiento: {X_train_esc.shape}")
    print(f"Tamaño de prueba: {X_test_esc.shape}")

    # 8. Guardar los arreglos preparados.
    np.savez(
        "dataset_preparado.npz",
        X_train=X_train_esc,
        X_test=X_test_esc,
        y_train=y_train.values,
        y_test=y_test.values,
    )
    print("\nArchivo dataset_preparado.npz guardado correctamente.")


if __name__ == "__main__":
    main()
