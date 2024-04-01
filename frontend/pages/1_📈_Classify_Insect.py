import streamlit as st
#from rembg import remove
from PIL import Image
from io import BytesIO
import numpy as np
import controller as ct


st.set_page_config(layout="wide", page_title="Classify Insect")

st.write("## Classify insect")
st.write(
    ''':ant: Upload the image you want to generate the prediction and then press the Classify button. 
    \n Please note that, if you want to register the finding with the geographical coordinates entered, you must select the register option before clicking on the classify button. :technologist:'''
)
st.sidebar.write("## Upload image :gear:")
is_clicked_clasificar = st.button('Classify')


MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

class_names = {
    0: "Butterfly",
    1: "Dragonfly",
    2: "Grasshopper",
    3: "Ladybird",
    4: "Mosquito"
}

def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

def predic(predecir):
    col2.write("**Prediction** :wrench:")
    statusButton =True    
    if predecir == 1:
        #call_api(sepal_length, sepal_width, petal_length, petal_width)
        numeroRandom = np.random.randint(6) ###
        if numeroRandom == 5:
            especie = "No reconocida"
        else:
            especie = str(class_names[numeroRandom])
        respuestaModelo = [numeroRandom, especie]
        if respuestaModelo[0]<= 4:
            st.balloons()
            infoInsect = ct.searchInsects(especie)
            Message = "**Nombre común:** "+infoInsect[0][0]+"\n\n **Nombre científico:** "+infoInsect[0][1]+"\n\n **División taxonómica:** "+infoInsect[0][2]
            color = infoInsect[0][3]
            if Register:
                ct.insertRowInferencia(especie, location, longitud, color)
        else:
            Message = especie
    else:
        Message = "Por favor cargue la imagen y oprima en clasificar para hacer la validación"
    col2.write(Message)

    #is_clicked_register = col2.button('Registrar', disabled=statusButton)
    

    #if is_clicked_register:
    #    st.snow()
        #ct.insertRowInferencia(especie, location, longitud, color)
    #    print(location, longitud, color)

Register = st.checkbox("Register")
if Register:
    statusLocation = False
else:
    statusLocation = True
col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
location = st.number_input('Ingrese latitud: ', min_value=-90.000, max_value=90.000, value=3.3638927, disabled=statusLocation)
longitud = st.number_input('Ingrese longitud: ', min_value=-180.000, max_value=180.000, value=-76.5255511, disabled=statusLocation)

if is_clicked_clasificar:
    predic(1)
else:
    predic(0)

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=my_upload)
else:
    fix_image("./Ladybird2.jpg")
