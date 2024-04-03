from fastapi import APIRouter, Request, UploadFile, File
from PIL import Image, UnidentifiedImageError
import numpy as np
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model
import io

model = load_model("insect-classif.h5")

class_names = {
    0: "Butterfly",
    1: "Dragonfly",
    2: "Grasshopper",
    3: "Ladybird",
    4: "Mosquito"
}

# Umbral de confianza
confidence_threshold = 0.6

insects_model_router = APIRouter()

@insects_model_router.get("/")
async def hi_model():
    return {"message": "Hello in the model insects router"}
 
@insects_model_router.post("/predict")
async def predict(file: UploadFile = File(None)):
    if file is None:
        return JSONResponse(content={"Error": "No se encontró ninguna imagen en la solicitud."}, status_code=400)
    try:
        # Open the image file
        img = Image.open(io.BytesIO(await file.read())).convert("RGB")

        # Resize the image to the model's input size (300x300)
        img = img.resize((300, 300))

        # Convert the image to a NumPy array
        image_array = np.array(img)

        # Preprocess the image
        image_array = image_array / 255.0

        # Make a prediction
        prediction = model.predict(np.expand_dims(image_array, axis=0))  # Expand dimensions for a single image

        # Get the predicted insect class index
        predicted_class_index = np.argmax(prediction)

        # Get the corresponding insect name from the dictionary
        predicted_insect_name = class_names[predicted_class_index]

        # Get the confidence of the prediction
        confidence = prediction[0][predicted_class_index]

        if confidence >= confidence_threshold:
            return JSONResponse(content={"Clase de Insecto": int(predicted_class_index), "Nombre de la clase de insecto": predicted_insect_name})
        else:
            return JSONResponse(content={"Error": "La imagen no corresponde a ninguna de las clases de insectos disponibles.", "confidence":float(confidence)}, status_code=404)
    except UnidentifiedImageError :
        return JSONResponse(content={"Error": "No se pudo identificar el formato de la imagen. Asegúrese de que la imagen sea válida."}, status_code=400)