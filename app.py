from pathlib import Path
from typing import Literal
import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

BASE = Path(__file__).parent
price_model = joblib.load(BASE / "house_price_model.pkl")
category_model = joblib.load(BASE / "house_category_model.pkl")

app = FastAPI(title="House Price API")
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])

class House(BaseModel):
    city: Literal["Karachi", "Lahore", "Islamabad", "Peshawar", "Karak", "Bannu", "Kohat"]
    area_type: Literal["Urban", "Suburban", "Rural"]
    bedrooms: int
    bathrooms: int
    area_marla: float
    age_years: float
    condition: Literal["Poor", "Fair", "Good", "Excellent"]
    furnished: Literal["Yes", "No"]
    has_garage: Literal["Yes", "No"]
    floor_type: Literal["Tiles", "Marble", "Cement", "Wood"]
    near_main_road: Literal["Yes", "No"]

@app.get("/", response_class=HTMLResponse)
def home():
    return (BASE / "index.html").read_text(encoding="utf-8")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(house: House):
    df = pd.DataFrame([dict(house)])
    return {
        "predicted_price_million_pkr": round(float(price_model.predict(df)[0]), 2),
        "price_category": str(category_model.predict(df)[0]),
    }
