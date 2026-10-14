
from pathlib import Path

import joblib
import numpy as np
import streamlit as st
from tensorflow import keras

BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="Predicción de lluvia",
    page_icon="🌧️",
    layout="centered",
)

st.title("🌧️ Predicción de lluvia")
st.write("Semana 6 — Tecnologías Emergentes")

@st.cache_resource
def cargar_modelo():
    modelo = keras.models.load_model(
        BASE_DIR / "modelo_produccion.keras"
    )
    escalador = joblib.load(
        BASE_DIR / "escalador_produccion.pkl"
    )
    return modelo, escalador


try:
    modelo, escalador = cargar_modelo()
    st.success("Modelo y escalador cargados correctamente.")
except Exception as error:
    st.error(f"No se pudieron cargar los archivos del modelo: {error}")
    st.stop()

st.subheader("Datos del clima")

temp_max = st.number_input(
    "Temperatura máxima (°C)",
    min_value=-20.0,
    max_value=60.0,
    value=18.5,
    step=0.5,
)

temp_min = st.number_input(
    "Temperatura mínima (°C)",
    min_value=-30.0,
    max_value=50.0,
    value=4.2,
    step=0.5,
)

viento_max = st.number_input(
    "Viento máximo (km/h)",
    min_value=0.0,
    max_value=300.0,
    value=12.0,
    step=0.5,
)

if st.button("Predecir lluvia de mañana", type="primary"):
    if temp_min > temp_max:
        st.error("La temperatura mínima no puede superar la máxima.")
    else:
        amplitud_termica = temp_max - temp_min
        X = np.array(
            [[temp_max, temp_min, amplitud_termica]],
            dtype=float,
        )

        X_escalado = escalador.transform(X)
        probabilidad = float(
            modelo.predict(X_escalado, verbose=0)[0][0]
        )

        prediccion = (
            "Día lluvioso"
            if probabilidad >= 0.5
            else "Día no lluvioso"
        )

        st.subheader("Resultado de la predicción")
        st.metric("Clasificación", prediccion)
        st.metric("Probabilidad estimada de lluvia", f"{probabilidad:.1%}")

        st.info(
            "Nota: el modelo utiliza temperatura máxima, temperatura "
            "mínima y amplitud térmica. El viento se muestra como dato "
            "de entrada, pero no interviene en esta predicción."
        )

