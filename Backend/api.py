from fastapi import FastAPI
from insects_model_router import insects_model_router
app = FastAPI()

app.include_router(insects_model_router, prefix="/insects-model")

