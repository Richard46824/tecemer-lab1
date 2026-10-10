\# Laboratorio 04 — Redes Neuronales



\## Descripción



En este laboratorio se construyó un clasificador de lluvia para datos de Huancayo utilizando una red neuronal perceptrón multicapa (MLP) con Keras y TensorFlow.



El trabajo parte del dataset climático `pronostico\_huancayo.csv` y comprende la preparación de los datos, el entrenamiento de una red neuronal sobre datos sintéticos y la construcción de un clasificador binario para determinar si un día será lluvioso.



\## Actividades realizadas



\- Preparación y limpieza del dataset climático.

\- Creación de la variable objetivo `dia\_lluvioso`.

\- Escalado de las variables mediante `StandardScaler`.

\- División de los datos en conjuntos de entrenamiento y prueba.

\- Construcción de un MLP con Keras.

\- Entrenamiento y evaluación del modelo.

\- Comparación con un baseline de regresión logística.

\- Generación de curvas de entrenamiento.

\- Guardado del modelo en formato `.keras`.

\- Creación de un script para realizar predicciones.

\- Creación de pruebas automatizadas con `pytest`.



\## Archivos principales



\- `ampliar\_dataset.py`: amplía el dataset climático.

\- `preparar\_dataset.py`: prepara y escala los datos.

\- `perceptron\_sintetico.py`: entrena un MLP con datos sintéticos.

\- `clasificador\_lluvia.py`: entrena y evalúa el clasificador de lluvia.

\- `predecir.py`: realiza predicciones con el modelo entrenado.

\- `dataset\_preparado.npz`: datos preparados para el entrenamiento.

\- `modelo\_lluvia.keras`: modelo neuronal entrenado.

\- `curvas\_entrenamiento\_lluvia.png`: curvas de entrenamiento del clasificador.

\- `curvas\_entrenamiento\_sintetico.png`: curvas del modelo sintético.

\- `tests/test\_preparacion.py`: pruebas automatizadas.



\## Pruebas



Las pruebas automatizadas se ejecutaron con:



```bash

python -m pytest tests/ -v

