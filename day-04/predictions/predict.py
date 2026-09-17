import pandas as pd
import joblib

from pathlib import Path


# Paths
BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_DIR = BASE_DIR / "day-04" / "models"


# Load trained model and preprocessing objects
model = joblib.load(
    MODEL_DIR / "logistic_regression.pkl"
)

scaler = joblib.load(
    MODEL_DIR / "scaler.pkl"
)

label_encoder = joblib.load(
    MODEL_DIR / "label_encoder.pkl"
)


# New facility data
new_facility = pd.DataFrame([
    {
        "cleanliness_score": 45,
        "odor_score": 70,
        "waste_level": 80,
        "complaints": 15,
        "footfall": 500,
        "hours_since_cleaning": 12
    }
])


# Features used by the model
features = [
    "cleanliness_score",
    "odor_score",
    "waste_level",
    "complaints",
    "footfall",
    "hours_since_cleaning"
]


# Scale input data
new_facility_scaled = scaler.transform(
    new_facility[features]
)


# Make prediction
prediction = model.predict(
    new_facility_scaled
)


# Convert encoded prediction back to label
risk_level = label_encoder.inverse_transform(
    prediction
)[0]


print("\nNew Facility Data")
print("=" * 30)
print(new_facility)


print("\nPredicted Hygiene Risk:", risk_level)

