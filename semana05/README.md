# Semana 5 — Ejercicios de redes neuronales

Esta carpeta reúne notebooks prácticos de aprendizaje automático y redes neuronales. Están diseñados principalmente para ejecutarse en **Google Colab** o Jupyter Notebook.

## Orden recomendado

| Orden | Notebook | Tema principal | Framework |
|---|---|---|---|
| 1 | [Ejercicio 01 — Preprocesamiento y exploración](Ejercicio_01_Preprocesamiento_Exploracion_Datos.ipynb) | Valores faltantes, visualización, codificación y escalado | Pandas / scikit-learn |
| 2 | [Ejercicio 02 — Perceptrón y MLP](Ejercicio_02_Perceptron_MLP.ipynb) | AND, XOR, funciones de activación y clasificación no lineal | TensorFlow / Keras |
| 3 | [Ejercicio 03a — CNN para clasificación de imágenes](Ejercicio_03a_CNN_Clasificacion_Imagenes_completado.ipynb) | Fashion-MNIST, convoluciones y matriz de confusión | TensorFlow / Keras |
| 4 | [Ejercicio 03b — CNN para detección de objetos](Ejercicio_03b_CNN_Deteccion_Objetos_completado.ipynb) | Cajas delimitadoras y modelo Faster R-CNN preentrenado | PyTorch / torchvision |
| 5 | [Ejercicio 04a — RNN y análisis de sentimientos](Ejercicio_04a_RNN_NLP_Analisis_Sentimientos_completado.ipynb) | Tokenización, embeddings y clasificación de reseñas | PyTorch |
| 6 | [Ejercicio 04b — RNN para series temporales](Ejercicio_04b_RNN_Series_Temporales_completado.ipynb) | Ventanas temporales y pronóstico con LSTM | TensorFlow / Keras |
| 7 | [Ejercicio 04c — Descripción de imágenes](Ejercicio_04c_RNN_Descripcion_Imagenes%20_completado.ipynb) | Generación de descripciones a partir de imágenes | Revisar el notebook |
| 8 | [Ejercicio 04d — NLP para triaje clínico](Ejercicio_04d_RNN_NLP_Salud_Triaje_Clinico_completado.ipynb) | Procesamiento de texto aplicado a un ejemplo educativo | Revisar el notebook |
| 9 | [Ejercicio 05 — Entrenamiento e hiperparámetros](Ejercicio_05_Entrenamiento_Ajuste_Hiperparametros_completado.ipynb) | Tasa de aprendizaje, tamaño de lote, dropout y parada temprana | TensorFlow / Keras |
| 10 | [Ejercicio 06 — Evaluación y despliegue](Ejercicio_06_Evaluacion_Despliegue_Modelos_completado.ipynb) | Métricas, curvas ROC, guardado y conversión a TensorFlow Lite | TensorFlow / Keras |

## Cómo ejecutarlos en Google Colab

1. Abre el notebook desde el enlace de la tabla.
2. Si GitHub muestra el archivo como texto, descárgalo o súbelo a [Google Colab](https://colab.research.google.com/).
3. En Colab, selecciona **Entorno de ejecución → Cambiar tipo de entorno de ejecución**. Para los ejercicios de redes neuronales, una GPU puede acelerar el entrenamiento si está disponible.
4. Ejecuta las celdas en orden, desde la primera hasta la última.
5. Si modificas una celda anterior, vuelve a ejecutar las celdas posteriores que dependan de ella.

## Dependencias y recursos

- Los ejercicios de preprocesamiento utilizan NumPy, Pandas, Matplotlib, Seaborn y scikit-learn.
- Los ejercicios de MLP, CNN y LSTM utilizan TensorFlow/Keras.
- Los ejercicios de detección de objetos y análisis de sentimientos utilizan PyTorch; el notebook de sentimientos también instala `datasets`.
- Algunos notebooks descargan datasets o imágenes de internet. Necesitan conexión y pueden tardar en la primera ejecución.
- No instales todas las bibliotecas en un único entorno local si no las necesitas. En Colab, instala solo las dependencias que solicite cada notebook.

## Buenas prácticas

- Ejecuta las celdas en orden y verifica que no haya errores antes de continuar.
- Conserva las salidas importantes, gráficas y métricas que solicita el docente.
- Los resultados de entrenamiento pueden variar según la versión de las bibliotecas, la disponibilidad de GPU y la aleatoriedad.
- Los modelos preentrenados y las redes neuronales pueden consumir bastante memoria y tiempo.
- El ejercicio de triaje clínico es material académico: sus resultados no deben utilizarse para tomar decisiones médicas reales.
- Antes de entregar, reinicia el entorno y ejecuta todas las celdas para comprobar que el notebook no dependa de variables creadas manualmente en sesiones anteriores.
