import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# Paths
BASE_DIR = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    BASE_DIR
    / "day-04"
    / "preprocessing"
    / "cleaned_dataset.csv"
)

MODEL_DIR = BASE_DIR / "day-04" / "models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)


# Load cleaned dataset
df = pd.read_csv(INPUT_FILE)

print("Dataset loaded successfully.")
print("Dataset shape:", df.shape)


# Select features and target
features = [
    "cleanliness_score",
    "odor_score",
    "waste_level",
    "complaints",
    "footfall",
    "hours_since_cleaning"
]

target = "hygiene_risk"

X = df[features].copy()
y = df[target].copy()


# Encode target if it contains text labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

print("\nTarget classes:")
print(label_encoder.classes_)


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -------------------------
# Model 1: Logistic Regression
# -------------------------

logistic_model = LogisticRegression(max_iter=1000)

logistic_model.fit(X_train_scaled, y_train)

logistic_predictions = logistic_model.predict(X_test_scaled)


# -------------------------
# Model 2: Random Forest
# -------------------------

random_forest_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

random_forest_model.fit(X_train, y_train)

random_forest_predictions = random_forest_model.predict(X_test)


# -------------------------
# Evaluation function
# -------------------------

def evaluate_model(name, y_true, predictions):
    print(f"\n{name}")
    print("-" * 30)

    print("Accuracy :", accuracy_score(y_true, predictions))
    print("Precision:", precision_score(y_true, predictions, average="weighted"))
    print("Recall   :", recall_score(y_true, predictions, average="weighted"))
    print("F1 Score :", f1_score(y_true, predictions, average="weighted"))


# Evaluate both models
evaluate_model(
    "Logistic Regression",
    y_test,
    logistic_predictions
)

evaluate_model(
    "Random Forest",
    y_test,
    random_forest_predictions
)


# Save models
joblib.dump(
    logistic_model,
    MODEL_DIR / "logistic_regression.pkl"
)

joblib.dump(
    random_forest_model,
    MODEL_DIR / "random_forest.pkl"
)

joblib.dump(
    label_encoder,
    MODEL_DIR / "label_encoder.pkl"
)

joblib.dump(
    scaler,
    MODEL_DIR / "scaler.pkl"
)


print("\nModels saved successfully.")



