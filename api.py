# Bring in lightweight dependencies
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.model import predict_pipeline
from app.model import __version__ as model_version

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


@app.get("/")
async def home():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionOut)
async def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}
