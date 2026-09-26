import pandas as pd
from pathlib import Path


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "facility_hygiene_ml_dataset.xlsx"


def load_dataset():
    """Load the raw hygiene dataset."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at: {DATA_PATH}"
        )

    return pd.read_excel(DATA_PATH)


def inspect_dataset(df):
    """Display important information about the dataset."""
    print("\n" + "=" * 60)
    print("SMART HYGIENE RISK PREDICTION SYSTEM")
    print("DATASET INSPECTION")
    print("=" * 60)

    print("\n1. Dataset Shape")
    print("-" * 60)
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\n2. Column Names")
    print("-" * 60)
    for column in df.columns:
        print(f"- {column}")

    print("\n3. First 5 Records")
    print("-" * 60)
    print(df.head().to_string(index=False))

    print("\n4. Data Types")
    print("-" * 60)
    print(df.dtypes.to_string())

    print("\n5. Missing Values")
    print("-" * 60)
    missing = df.isnull().sum()
    print(missing.to_string())

    print("\n6. Duplicate Rows")
    print("-" * 60)
    print(f"Duplicates: {df.duplicated().sum()}")

    print("\n7. Numerical Summary")
    print("-" * 60)
    print(df.describe().to_string())

    print("\n8. Categorical Columns")
    print("-" * 60)

    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns

    for column in categorical_columns:
        print(f"\n{column}:")
        print(df[column].value_counts(dropna=False).to_string())

    print("\n" + "=" * 60)
    print("INSPECTION COMPLETED")
    print("=" * 60)


def main():
    """Main execution function."""
    try:
        df = load_dataset()
        inspect_dataset(df)

    except Exception as error:
        print(f"\nERROR: {error}")


if __name__ == "__main__":
    main()

