import streamlit as st

st.set_page_config(layout="wide",page_title="Insect ID")

st.write("## InsectID: Aplicación de Clasificación de Insectos con IA")
st.write(
    ''':bee:  Bienvenidos, esta aplicación es una herramienta de apoyo a la clasificación y geolocalización de diferentes 
    especies de insectos.
    \n Inicialmente contamos con un modelo entrenado para clasificar 5 especies, pero con tu ayuda crecerá hasta cubrir 
    una gran proporsión de la biodiversidad de insectos presentes en nuestro planeta.
    ''')
st.write("Las especies incluidas actualmente son: ")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
   st.write("A butterfly")
   st.image("./Butterfly.jpg")

with col2:
   st.write("A dragonfly")
   st.image("./Dragonfly.jpeg")

with col3:
   st.write("A grasshopper")
   st.image("./Grasshopper2.jpg")

with col4:
   st.write("A Ladybird")
   st.image("./Ladybird1.jpg")

with col5:
   st.write("A mosquito")
   st.image("./Mosquito2.jpg")

st.write(
    '''Al navegar por este lugar encontrarás la herramienta de clasificación donde podrás cargar una imagen desde tu galería personal
    y el modelo indicará a cual especie pertenece el insecto, este resultado se puede guardar junto a su ubicación gps para actualizar
    el mapa de hallazgos, el cual podrás visualizar en una de nuestras páginas. Por último tendras acceso a una descripción detallada
    de cada especie disponible por medio de una mini-enciclopedia.
    \n Que esperas para descubrir todo lo que tenemos para ti!'''
)

