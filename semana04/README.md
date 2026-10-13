# Semana 4 — Laboratorio de redes neuronales: clasificación de lluvia

## Descripción

En este laboratorio se construyó un clasificador de lluvia para datos de Huancayo utilizando una red neuronal perceptrón multicapa (MLP) con Keras y TensorFlow.

El trabajo comprende la preparación de los datos, el entrenamiento de una red neuronal sobre datos sintéticos y la construcción de un clasificador binario para determinar si un día será lluvioso.

## Actividades realizadas

- Preparación y limpieza del dataset climático.
- Creación de la variable objetivo `dia_lluvioso`.
- Escalado de variables mediante `StandardScaler`.
- División de los datos en conjuntos de entrenamiento y prueba.
- Construcción, entrenamiento y evaluación de un MLP con Keras.
- Comparación con una regresión logística de referencia.
- Generación de curvas de entrenamiento y guardado del modelo en formato `.keras`.
- Creación de un script de predicción y pruebas automatizadas con pytest.

## Archivos principales

- `ampliar_dataset.py`: amplía el dataset climático.
- `preparar_dataset.py`: prepara y escala los datos.
- `perceptron_sintetico.py`: entrena un MLP con datos sintéticos.
- `clasificador_lluvia.py`: entrena y evalúa el clasificador.
- `predecir.py`: realiza predicciones con el modelo entrenado.
- `dataset_preparado.npz`: datos preparados para entrenamiento.
- `escalador_lluvia.joblib`: escalador ajustado solo con el conjunto de entrenamiento y reutilizado en predicciones.
- `modelo_lluvia.keras`: modelo neuronal entrenado.
- `curvas_entrenamiento_lluvia.png` y `curvas_entrenamiento_sintetico.png`: curvas generadas durante el entrenamiento.
- `tests/test_preparacion.py`: pruebas automatizadas.

## Dependencias adicionales

Además de las dependencias generales del repositorio, los ejercicios de esta semana necesitan scikit-learn, TensorFlow y Matplotlib. Instálalas en el entorno virtual antes de entrenar:

```bash
python -m pip install scikit-learn tensorflow matplotlib
```

## Ejecución y pruebas

Abre la terminal dentro de esta carpeta para respetar las rutas relativas de los scripts:

```bash
cd semana04
python preparar_dataset.py
python clasificador_lluvia.py
python predecir.py
python -m pytest tests/ -v
```

Ejecuta los pasos en ese orden y desde esta carpeta. `predecir.py` requiere que existan `modelo_lluvia.keras` y `escalador_lluvia.joblib`, generados por los pasos anteriores. Para predecir, modifica en `predecir.py` las temperaturas máximas y mínimas de `temperaturas_nuevas`; el programa calcula la amplitud térmica y aplica el mismo escalador usado durante el entrenamiento. El entrenamiento requiere las bibliotecas indicadas arriba.
