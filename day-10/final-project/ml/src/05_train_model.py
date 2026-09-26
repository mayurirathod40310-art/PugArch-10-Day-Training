import pandas as pd
import joblib

from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = PROJECT_ROOT / "data" / "cleaned_hygiene_dataset.csv"
MODEL_DIR = PROJECT_ROOT / "models"

MODEL_DIR.mkdir(exist_ok=True)


def evaluate_model(model, X_test, y_test, model_name):
    """Evaluate a trained model using multiple classification metrics."""

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    precision = precision_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0,
    )

    recall = recall_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0,
    )

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0,
    )

    print("\n" + "-" * 70)
    print(model_name)
    print("-" * 70)

    print(f"Accuracy  : {accuracy:.4f}")
    print(f"Precision : {precision:.4f}")
    print(f"Recall    : {recall:.4f}")
    print(f"F1 Score  : {f1:.4f}")

    print("\nClassification Report:")
    print(classification_report(y_test, predictions, zero_division=0))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, predictions))

    return f1


def main():

    print("=" * 70)
    print("SMART HYGIENE RISK PREDICTION SYSTEM")
    print("MODEL TRAINING")
    print("=" * 70)

    # ---------------------------------------------------------
    # 1. Load cleaned dataset
    # ---------------------------------------------------------

    df = pd.read_csv(DATA_PATH)

    print("\nDataset shape:")
    print(df.shape)

    # ---------------------------------------------------------
    # 2. Separate features and target
    # ---------------------------------------------------------

    X = df.drop(columns=["hygiene_risk"])
    y = df["hygiene_risk"]

    print("\nFeatures:")
    print(list(X.columns))

    print("\nTarget:")
    print("hygiene_risk")

    # ---------------------------------------------------------
    # 3. Identify feature types
    # ---------------------------------------------------------

    categorical_features = [
        "location",
        "facility_type",
        "water_availability",
    ]

    numerical_features = [
        "cleanliness_score",
        "odor_score",
        "waste_level",
        "footfall",
        "complaints",
        "hours_since_cleaning",
        "inspection_month",
        "inspection_day_of_week",
    ]

    # ---------------------------------------------------------
    # 4. Preprocessing
    # ---------------------------------------------------------

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features,
            ),
            (
                "numerical",
                StandardScaler(),
                numerical_features,
            ),
        ]
    )

    # ---------------------------------------------------------
    # 5. Train-test split
    # ---------------------------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    print("\nTraining samples:", len(X_train))
    print("Testing samples :", len(X_test))

    # ---------------------------------------------------------
    # 6. Logistic Regression
    # ---------------------------------------------------------

    logistic_pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "classifier",
                LogisticRegression(
                    max_iter=1000,
                    random_state=42,
                ),
            ),
        ]
    )

    logistic_pipeline.fit(X_train, y_train)

    logistic_f1 = evaluate_model(
        logistic_pipeline,
        X_test,
        y_test,
        "LOGISTIC REGRESSION",
    )

    # ---------------------------------------------------------
    # 7. Random Forest
    # ---------------------------------------------------------

    random_forest_pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=200,
                    random_state=42,
                    class_weight="balanced",
                ),
            ),
        ]
    )

    random_forest_pipeline.fit(X_train, y_train)

    random_forest_f1 = evaluate_model(
        random_forest_pipeline,
        X_test,
        y_test,
        "RANDOM FOREST",
    )

    # ---------------------------------------------------------
    # 8. Select model based on F1 score
    # ---------------------------------------------------------

    if random_forest_f1 > logistic_f1:
        best_model = random_forest_pipeline
        best_model_name = "Random Forest"
    else:
        best_model = logistic_pipeline
        best_model_name = "Logistic Regression"

    print("\n" + "=" * 70)
    print("MODEL SELECTION")
    print("=" * 70)

    print(f"Selected model: {best_model_name}")

    # ---------------------------------------------------------
    # 9. Save best model
    # ---------------------------------------------------------

    model_path = MODEL_DIR / "hygiene_risk_model.pkl"

    joblib.dump(best_model, model_path)

    print(f"\nModel saved to:")
    print(model_path)

    print("\n" + "=" * 70)
    print("MODEL TRAINING COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    main()

