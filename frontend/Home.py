import streamlit as st
import controller as ct

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
   st.image("./images/butterfly.jpg")

with col2:
   st.write("A dragonfly")
   st.image("./images/Dragonfly.jpeg")

with col3:
   st.write("A grasshopper")
   st.image("./images/Grasshopper2.jpg")

with col4:
   st.write("A Ladybird")
   st.image("./images/Ladybird1.jpg")

with col5:
   st.write("A mosquito")
   st.image("./images/Mosquito2.jpg")

st.write(
    '''Al navegar por este lugar encontrarás la herramienta de clasificación donde podrás cargar una imagen desde tu galería personal
    y el modelo indicará a cual especie pertenece el insecto, este resultado se puede guardar junto a su ubicación gps para actualizar
    el mapa de hallazgos, el cual podrás visualizar en una de nuestras páginas. Por último tendras acceso a una descripción detallada
    de cada especie disponible por medio de una mini-enciclopedia.
    \n Que esperas para descubrir todo lo que tenemos para ti!'''
)

def LoggedIn_Clicked(userName, password):
    #logStatus, messageLog = dbuser_consultation(userName,password)    
    logStatus, messageLog = ct.searchUsers(userName, password)
    if logStatus:
        st.session_state.userN = userName        
        st.session_state['loggedIn'] = True
    else:
        st.session_state['loggedIn'] = False
        st.error(messageLog)
    
def show_login_page():
    if st.session_state['loggedIn'] == False:
        st.session_state.userN = ""
        userName = st.sidebar.text_input (label="", value="", placeholder="Enter your user name")
        password = st.sidebar.text_input (label="", value="",placeholder="Enter password", type="password")
        st.sidebar.button ("Login", on_click=LoggedIn_Clicked, args= (userName, password))

def LoggedOut_Clicked():
    st.session_state.userN = ""
    st.session_state['loggedIn'] = False

if 'loggedIn' not in st.session_state:
    st.session_state['loggedIn'] = False
    show_login_page() 
else:
    if st.session_state['loggedIn']:
        st.sidebar.write(f"## Welcome {st.session_state.userN}")
        st.sidebar.button ("Logout", on_click=LoggedOut_Clicked) 
    else:        
        show_login_page()