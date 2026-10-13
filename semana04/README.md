# Semana 4 — Clasificación de días lluviosos

En esta práctica trabajé con datos del clima de Huancayo para crear un modelo que permita clasificar si un día será lluvioso. Preparé los datos, entrené una red neuronal tipo MLP y comparé sus resultados con una regresión logística.

## Archivos principales

- `ampliar_dataset.py`: genera más datos para trabajar en la práctica.
- `preparar_dataset.py`: prepara los datos antes del entrenamiento.
- `perceptron_sintetico.py`: permite practicar con una red neuronal y datos sintéticos.
- `clasificador_lluvia.py`: entrena y evalúa el clasificador de lluvia.
- `predecir.py`: utiliza el modelo entrenado para realizar predicciones.
- `dataset_preparado.npz`: datos preparados para el entrenamiento.
- `escalador_lluvia.joblib`: escalador ajustado con los datos de entrenamiento.
- `modelo_lluvia.keras`: modelo entrenado.
- `curvas_entrenamiento_lluvia.png` y `curvas_entrenamiento_sintetico.png`: gráficas del entrenamiento.
- `tests/test_preparacion.py`: pruebas de la preparación de datos.

## Instalar las bibliotecas

Además de las dependencias generales del proyecto, esta práctica utiliza scikit-learn, TensorFlow y Matplotlib:

```bash
python -m pip install scikit-learn tensorflow matplotlib
```

## Cómo ejecutar

Abre una terminal y entra a la carpeta de esta semana:

```bash
cd semana04
python preparar_dataset.py
python clasificador_lluvia.py
python predecir.py
```

Ejecuta los archivos en ese orden. El script de predicción necesita que ya existan `modelo_lluvia.keras` y `escalador_lluvia.joblib`. Para cambiar el ejemplo de predicción, modifica los valores de temperatura que aparecen en `predecir.py`.

Para ejecutar las pruebas:

```bash
python -m pytest tests/ -v
```

El entrenamiento puede tardar un poco y necesita las bibliotecas instaladas. El escalador se ajusta con los datos de entrenamiento y luego se reutiliza para transformar los datos nuevos.
