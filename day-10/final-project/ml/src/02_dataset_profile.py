import pandas as pd
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "facility_hygiene_ml_dataset.xlsx"


def main():
    df = pd.read_excel(DATA_PATH)

    print("=" * 70)
    print("SMART HYGIENE RISK PREDICTION SYSTEM")
    print("DATASET PROFILE")
    print("=" * 70)

    print("\nSHAPE")
    print(df.shape)

    print("\nCOLUMNS")
    for i, column in enumerate(df.columns, start=1):
        print(f"{i}. {column}")

    print("\nDATA TYPES")
    print(df.dtypes)

    print("\nMISSING VALUES")
    print(df.isnull().sum())

    print("\nDUPLICATES")
    print(df.duplicated().sum())

    print("\nNUMERICAL COLUMNS")
    numerical_columns = df.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    print(numerical_columns)

    if numerical_columns:
        print("\nNUMERICAL SUMMARY")
        print(df[numerical_columns].describe().round(2))

    print("\nTARGET DISTRIBUTION")
    if "hygiene_risk" in df.columns:
        print(df["hygiene_risk"].value_counts())

    print("\nSAMPLE DATA")
    print(df.head(10).to_string(index=False))

    print("\n" + "=" * 70)
    print("PROFILE COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    main()

    