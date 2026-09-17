import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix


# Paths
BASE_DIR = Path(__file__).resolve().parents[2]

DATA_FILE = (
    BASE_DIR
    / "day-04"
    / "preprocessing"
    / "cleaned_dataset.csv"
)

MODEL_DIR = BASE_DIR / "day-04" / "models"


# Load dataset
df = pd.read_csv(DATA_FILE)


# Features and target
features = [
    "cleanliness_score",
    "odor_score",
    "waste_level",
    "complaints",
    "footfall",
    "hours_since_cleaning"
]

X = df[features]
y = df["hygiene_risk"]


# Load label encoder
label_encoder = joblib.load(
    MODEL_DIR / "label_encoder.pkl"
)

y_encoded = label_encoder.transform(y)


# Same train-test split used during training
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)


# Load scaler and Logistic Regression model
scaler = joblib.load(
    MODEL_DIR / "scaler.pkl"
)

logistic_model = joblib.load(
    MODEL_DIR / "logistic_regression.pkl"
)


# Scale test data
X_test_scaled = scaler.transform(X_test)


# Predictions
predictions = logistic_model.predict(X_test_scaled)


# Classification report
print("\nClassification Report")
print("=" * 50)

print(
    classification_report(
        y_test,
        predictions,
        target_names=label_encoder.classes_
    )
)


# Confusion matrix
print("\nConfusion Matrix")
print("=" * 50)

matrix = confusion_matrix(
    y_test,
    predictions
)

print(matrix)


print("\nEvaluation completed successfully.")

