import streamlit as st
import requests
import joblib

def main():
    # Título de la página
    st.title("Clasificación de Sismos")

    # Formulario de clasificación
    st.subheader("Formulario de Clasificación")
    magnitude = st.text_input("Magnitud", value="", help="Ingrese la magnitud del sismo")
    intensity = st.text_input("Intensidad", value="", help="Ingrese la intensidad del sismo")

    # Carga del modelo entrenado
    model = joblib.load("kmeans_model.pkl")

    # Creacion array respuesta
    respuesta = ["""Los sismos en este rango tienen una intensidad perceptible 
    que va desde niveles bajos hasta niveles ampliamente perceptibles en el área afectada. 
    Pueden provocar daños menores en estructuras, 
    como grietas en los muros y caída de revestimientos, 
    y ser percibidos por un número variable de personas, 
    desde unas pocas en reposo y en posición tranquila 
    hasta todas las personas en el área afectada.""",
    """Los sismos en este rango tienen una intensidad que generalmente no se percibe, 
    excepto en condiciones muy favorables, 
    hasta niveles que a menudo se perciben, 
    pero rara vez causan daños. 
    En términos de magnitud, 
    van desde temblores que se sienten como vibraciones menores 
    hasta sismos que pueden causar daños menores en estructuras.""",
    """los sismos en este rango tienen una intensidad que generalmente no se percibe, 
    pero que en condiciones favorables puede ser percibida por unas pocas personas en reposo 
    y en posición tranquila. 
    Además, la magnitud de estos sismos va desde temblores de vibración menor 
    hasta la capacidad de causar una gran cantidad de daños en áreas habitadas.""",
    """los sismos en este rango tienen una intensidad que a menudo se percibe 
    y puede causar una gran cantidad de daños en áreas habitadas, 
    junto con una magnitud que va desde temblores menores 
    hasta la capacidad de causar daños significativos en estructuras.""",
    """los sismos en este rango tienen una intensidad 
    que puede causar daños significativos en áreas más grandes 
    y una magnitud que va desde la capacidad de causar daños significativos
    en estructuras hasta la posibilidad de ocasionar daños extensos 
    e incluso colapso total de edificios."""]

    if st.button("Clasificar"):
   
        if magnitude and intensity:
            
            # Realizar la clasificación utilizando el modelo entrenado
            clasificacion = model.predict([[magnitude, intensity]])

            # Convertir el resultado en un tipo de datos nativo de Python
            #clasificacion = np.asscalar(clasificacion)
            clasificacion = clasificacion.item()
    
            # Mostrar la clasificación y el texto correspondiente
            st.write(f"Clasificación: {clasificacion}")
            st.write(f"Texto: {respuesta[clasificacion]}")
            
        else:
            st.warning("Por favor, ingrese la magnitud y la intensidad del sismo.")


if __name__ == "__main__":
    main()
