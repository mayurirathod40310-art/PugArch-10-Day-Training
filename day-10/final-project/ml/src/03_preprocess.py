import pandas as pd
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = PROJECT_ROOT / "data" / "facility_hygiene_ml_dataset.xlsx"
OUTPUT_PATH = PROJECT_ROOT / "data" / "cleaned_hygiene_dataset.csv"


def load_dataset():
    """Load the raw Excel dataset."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    return pd.read_excel(DATA_PATH)


def clean_dataset(df):
    """Clean and prepare the dataset for machine learning."""

    print("\n" + "=" * 70)
    print("DATA PREPROCESSING")
    print("=" * 70)

    print("\nOriginal shape:")
    print(df.shape)

    # ---------------------------------------------------------
    # 1. Remove duplicate rows
    # ---------------------------------------------------------
    duplicate_count = df.duplicated().sum()

    print(f"\nDuplicate rows found: {duplicate_count}")

    df = df.drop_duplicates().copy()

    print(f"Shape after removing duplicates: {df.shape}")

    # ---------------------------------------------------------
    # 2. Handle missing numerical values
    # ---------------------------------------------------------
    numerical_columns = [
        "cleanliness_score",
        "odor_score",
        "waste_level",
        "footfall",
        "complaints",
        "hours_since_cleaning",
    ]

    for column in numerical_columns:
        if df[column].isnull().sum() > 0:
            median_value = df[column].median()
            df[column] = df[column].fillna(median_value)

            print(
                f"Filled missing values in {column} "
                f"using median: {median_value:.2f}"
            )

    # ---------------------------------------------------------
    # 3. Handle missing categorical values
    # ---------------------------------------------------------
    categorical_columns = [
        "location",
        "facility_type",
        "water_availability",
    ]

    for column in categorical_columns:
        if df[column].isnull().sum() > 0:
            mode_value = df[column].mode()[0]
            df[column] = df[column].fillna(mode_value)

            print(
                f"Filled missing values in {column} "
                f"using mode: {mode_value}"
            )

    # ---------------------------------------------------------
    # 4. Convert inspection date
    # ---------------------------------------------------------
    df["inspection_date"] = pd.to_datetime(
        df["inspection_date"],
        errors="coerce"
    )

    df["inspection_month"] = df["inspection_date"].dt.month
    df["inspection_day_of_week"] = df["inspection_date"].dt.dayofweek

    # Remove original date because the model uses extracted features
    df = df.drop(columns=["inspection_date"])

    # ---------------------------------------------------------
    # 5. Remove facility ID
    # ---------------------------------------------------------
    df = df.drop(columns=["facility_id"])

    # ---------------------------------------------------------
    # 6. Final missing-value check
    # ---------------------------------------------------------
    print("\nRemaining missing values:")
    print(df.isnull().sum())

    # ---------------------------------------------------------
    # 7. Save cleaned dataset
    # ---------------------------------------------------------
    df.to_csv(OUTPUT_PATH, index=False)

    print("\nFinal cleaned shape:")
    print(df.shape)

    print(f"\nCleaned dataset saved to:")
    print(OUTPUT_PATH)

    print("\n" + "=" * 70)
    print("PREPROCESSING COMPLETED")
    print("=" * 70)

    return df


def main():
    try:
        df = load_dataset()
        clean_dataset(df)

    except Exception as error:
        print(f"\nERROR: {error}")


if __name__ == "__main__":
    main()

    