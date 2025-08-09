import streamlit as st
import pandas as pd

# Ejemplo Controles:
st.title("Mi Primera App con Streamlit")
st.write("¡Hola mundo desde Streamlit!")
st.title("Título grande")
st.header("Encabezado")
st.subheader("Subencabezado")
st.text("Texto plano")
st.markdown("**Texto en negrita** y _cursiva_")

# Variables y entrada de controles:
nombre = st.text_input("Escribe tu nombre")
edad = st.number_input("Tu edad", min_value=0)
color = st.color_picker("Elige un color")
fecha = st.date_input("Selecciona una fecha")

# Botón:
if st.button("Saludar"):
    st.write(f"¡Hola {nombre}!")


# Preparación grafico
df = pd.DataFrame({
    "x": range(10),
    "y": [i**2 for i in range(10)]
})


# Grafico:
st.line_chart(df)
archivo = st.file_uploader("Sube un archivo CSV")
if archivo is not None:
    df = pd.read_csv(archivo)
    st.write(df)
