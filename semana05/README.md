# Semana 5 — Redes neuronales

En esta carpeta reuní los notebooks de los ejercicios de la semana. Con ellos practico el preprocesamiento de datos, las redes neuronales y la evaluación de modelos. La forma más sencilla de ejecutarlos es usar Google Colab.

## Orden de los ejercicios

| N.º | Notebook | ¿Qué se trabaja? |
|---|---|---|
| 1 | [Preprocesamiento y exploración](Ejercicio_01_Preprocesamiento_Exploracion_Datos.ipynb) | Datos faltantes, gráficas, codificación y escalado. |
| 2 | [Perceptrón y MLP](Ejercicio_02_Perceptron_MLP.ipynb) | Compuertas AND y XOR y clasificación. |
| 3a | [CNN para clasificar imágenes](Ejercicio_03a_CNN_Clasificacion_Imagenes_completado.ipynb) | Clasificación de imágenes con Fashion-MNIST. |
| 3b | [CNN para detectar objetos](Ejercicio_03b_CNN_Deteccion_Objetos_completado.ipynb) | Detección de objetos con Faster R-CNN. |
| 4a | [RNN y análisis de sentimientos](Ejercicio_04a_RNN_NLP_Analisis_Sentimientos_completado.ipynb) | Clasificación de reseñas de texto. |
| 4b | [RNN para series temporales](Ejercicio_04b_RNN_Series_Temporales_completado.ipynb) | Pronóstico de datos ordenados en el tiempo. |
| 4c | [Descripción de imágenes](Ejercicio_04c_RNN_Descripcion_Imagenes%20_completado.ipynb) | Generación de texto a partir de imágenes. |
| 4d | [NLP para triaje clínico](Ejercicio_04d_RNN_NLP_Salud_Triaje_Clinico_completado.ipynb) | Ejemplo educativo de clasificación de texto. |
| 5 | [Entrenamiento e hiperparámetros](Ejercicio_05_Entrenamiento_Ajuste_Hiperparametros_completado.ipynb) | Pruebas con parámetros del entrenamiento. |
| 6 | [Evaluación y despliegue](Ejercicio_06_Evaluacion_Despliegue_Modelos_completado.ipynb) | Métricas y guardado de modelos. |

## Cómo abrir los notebooks en Google Colab

1. Entra a [Google Colab](https://colab.research.google.com/).
2. Descarga el notebook desde GitHub o súbelo a Colab.
3. Abre el archivo y ejecuta las celdas en orden, desde el inicio.
4. Si una celda da error, revisa el mensaje y comprueba que las celdas anteriores se hayan ejecutado correctamente.
5. Guarda las gráficas y resultados que necesites para la entrega.

## Bibliotecas y conexión

Cada notebook puede usar bibliotecas distintas, como NumPy, Pandas, Matplotlib, scikit-learn, TensorFlow o PyTorch. Revisa las primeras celdas para ver si hay que instalar algo antes de empezar.

Algunos ejercicios descargan datos o imágenes de internet, por eso necesitan conexión. El entrenamiento puede tardar y los resultados pueden variar según las versiones de las bibliotecas y los recursos disponibles.

## Antes de entregar

Conviene ejecutar cada notebook desde el principio para comprobar que funciona sin depender de variables que quedaron guardadas de una ejecución anterior. El ejercicio de triaje clínico es solo académico y no debe usarse para tomar decisiones médicas reales.
