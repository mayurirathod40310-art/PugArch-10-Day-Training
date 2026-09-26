import pandas as pd
import matplotlib.pyplot as plt
import joblib

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = PROJECT_ROOT / "data" / "cleaned_hygiene_dataset.csv"
MODEL_PATH = PROJECT_ROOT / "models" / "hygiene_risk_model.pkl"
OUTPUT_DIR = PROJECT_ROOT / "visualizations"

OUTPUT_DIR.mkdir(exist_ok=True)


def main():

    print("=" * 70)
    print("SMART HYGIENE RISK PREDICTION SYSTEM")
    print("FEATURE IMPORTANCE")
    print("=" * 70)

    # ---------------------------------------------------------
    # 1. Load dataset
    # ---------------------------------------------------------

    df = pd.read_csv(DATA_PATH)

    X = df.drop(columns=["hygiene_risk"])

    # ---------------------------------------------------------
    # 2. Load trained pipeline
    # ---------------------------------------------------------

    model = joblib.load(MODEL_PATH)

    preprocessor = model.named_steps["preprocessor"]
    classifier = model.named_steps["classifier"]

    # ---------------------------------------------------------
    # 3. Get transformed feature names
    # ---------------------------------------------------------

    feature_names = preprocessor.get_feature_names_out()

    coefficients = classifier.coef_
    classes = classifier.classes_

    print("\nRisk classes:")
    print(list(classes))

    print("\nNumber of transformed features:")
    print(len(feature_names))

    # ---------------------------------------------------------
    # 4. Display strongest features for each class
    # ---------------------------------------------------------

    for index, class_name in enumerate(classes):

        class_coefficients = coefficients[index]

        importance = pd.DataFrame(
            {
                "feature": feature_names,
                "coefficient": class_coefficients,
            }
        )

        importance["absolute_coefficient"] = (
            importance["coefficient"].abs()
        )

        importance = importance.sort_values(
            "absolute_coefficient",
            ascending=False,
        )

        print("\n" + "-" * 70)
        print(f"TOP FEATURES FOR: {class_name}")
        print("-" * 70)

        print(
            importance[
                ["feature", "coefficient"]
            ].head(10).to_string(index=False)
        )

    # ---------------------------------------------------------
    # 5. Create overall coefficient visualization
    # ---------------------------------------------------------

    overall_importance = pd.DataFrame(
        {
            "feature": feature_names,
            "importance": abs(coefficients).mean(axis=0),
        }
    )

    overall_importance = overall_importance.sort_values(
        "importance",
        ascending=False,
    ).head(10)

    print("\n" + "=" * 70)
    print("TOP 10 OVERALL FEATURES")
    print("=" * 70)

    print(
        overall_importance.to_string(index=False)
    )

    # ---------------------------------------------------------
    # 6. Plot
    # ---------------------------------------------------------

    plt.figure(figsize=(10, 6))

    plt.barh(
        overall_importance["feature"],
        overall_importance["importance"],
    )

    plt.title("Top 10 Features Influencing Hygiene Risk Prediction")
    plt.xlabel("Mean Absolute Logistic Regression Coefficient")
    plt.ylabel("Feature")

    plt.gca().invert_yaxis()

    plt.tight_layout()

    output_path = (
        OUTPUT_DIR / "07_feature_importance.png"
    )

    plt.savefig(output_path)
    plt.close()

    print("\nFeature importance visualization saved to:")
    print(output_path)

    print("\n" + "=" * 70)
    print("FEATURE IMPORTANCE COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    main()
    