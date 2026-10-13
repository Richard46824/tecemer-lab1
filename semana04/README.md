# Semana 4 — Clasificación de lluvia

Práctica de preparación de datos y aprendizaje automático a partir del pronóstico meteorológico de Huancayo.

## Archivos principales

- `preparar_dataset.py`: prepara características, etiqueta los días lluviosos, divide entrenamiento/prueba y guarda el conjunto preparado.
- `clasificador_lluvia.py`: compara regresión logística con una red neuronal MLP de Keras.
- `predecir.py`: carga el modelo guardado y produce predicciones.
- `tests/test_preparacion.py`: pruebas de preparación.
- Archivos de datos, modelo y curvas de entrenamiento generados durante la práctica.

## Nota de ejecución

Los scripts utilizan rutas relativas al directorio de trabajo. Para seguir las rutas definidas en el código, abre una terminal dentro de `semana04/` antes de ejecutarlos. Instala las dependencias que indique la práctica antes de entrenar el modelo.
