import streamlit as st
import requests

# Título de la página
st.title("Clasificación de Sismos")

# Formulario de clasificación
st.subheader("Formulario de Clasificación")
magnitude = st.text_input("Magnitud", value="", help="Ingrese la magnitud del sismo")
intensity = st.text_input("Intensidad", value="", help="Ingrese la intensidad del sismo")

if st.button("Clasificar"):
    # Realizar la clasificación del sismo y mostrar el resultado
    # en lugar de realizar una solicitud a una API externa, aquí puedes
    
    # Construir la URL de la API con los parámetros
    api_url = f"https://mlapi2.onrender.com/clasificar_sismo/{magnitude}/{intensity}"



    if magnitude and intensity:
        # Realizar la solicitud a la API y obtener la respuesta
        response = requests.get(api_url)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            data = response.json()  # Convertir la respuesta en formato JSON a un diccionario de Python
            # Mostrar los datos en Streamlit
            st.write("Clasificación:", data["clasificacion"])
            st.write(data["texto"])
        else:
            st.error("Error al cargar los datos de la API")
            
    else:
        st.warning("Por favor, ingrese la magnitud y la intensidad del sismo.")


