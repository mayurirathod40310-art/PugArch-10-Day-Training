from pathlib import Path

import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib


# --------------------------------------------------
# 1. Load the trained ML model
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = PROJECT_ROOT / "ml" / "models" / "hygiene_risk_model.pkl"

model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# 2. Create FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="Smart Hygiene Risk Prediction API",
    description="API for predicting facility hygiene risk using a trained ML model.",
    version="1.0.0",
)


# --------------------------------------------------
# 3. Enable CORS for frontend
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# 4. Input data model
# --------------------------------------------------

class PredictionInput(BaseModel):
    location: str
    facility_type: str
    cleanliness_score: float
    odor_score: float
    waste_level: float
    water_availability: str
    footfall: int
    complaints: int
    hours_since_cleaning: float
    inspection_month: int
    inspection_day_of_week: int


# --------------------------------------------------
# 5. Health check endpoint
# --------------------------------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": True
    }


# --------------------------------------------------
# 6. Model information endpoint
# --------------------------------------------------

@app.get("/model-info")
def model_info():
    return {
        "model": "Logistic Regression",
        "classes": model.classes_.tolist(),
        "features": [
            "location",
            "facility_type",
            "cleanliness_score",
            "odor_score",
            "waste_level",
            "water_availability",
            "footfall",
            "complaints",
            "hours_since_cleaning",
            "inspection_month",
            "inspection_day_of_week"
        ]
    }


# --------------------------------------------------
# 7. Prediction endpoint
# --------------------------------------------------

@app.post("/predict")
def predict_risk(data: PredictionInput):

    input_data = pd.DataFrame([data.model_dump()])

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    probability_dict = {
        class_name: round(float(probability), 4)
        for class_name, probability in zip(model.classes_, probabilities)
    }

    return {
        "prediction": prediction,
        "probabilities": probability_dict
    }
