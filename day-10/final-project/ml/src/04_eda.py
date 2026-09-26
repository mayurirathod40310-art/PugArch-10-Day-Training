import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = PROJECT_ROOT / "data" / "cleaned_hygiene_dataset.csv"
OUTPUT_DIR = PROJECT_ROOT / "visualizations"

OUTPUT_DIR.mkdir(exist_ok=True)


def main():
    print("=" * 70)
    print("SMART HYGIENE RISK PREDICTION SYSTEM")
    print("EXPLORATORY DATA ANALYSIS")
    print("=" * 70)

    df = pd.read_csv(DATA_PATH)

    # ---------------------------------------------------------
    # 1. Target distribution
    # ---------------------------------------------------------
    risk_counts = df["hygiene_risk"].value_counts()

    print("\nHygiene Risk Distribution:")
    print(risk_counts)

    plt.figure(figsize=(8, 5))
    risk_counts.plot(kind="bar")
    plt.title("Hygiene Risk Distribution")
    plt.xlabel("Hygiene Risk")
    plt.ylabel("Number of Facilities")
    plt.xticks(rotation=0)
    plt.tight_layout()

    path = OUTPUT_DIR / "01_hygiene_risk_distribution.png"
    plt.savefig(path)
    plt.close()

    # ---------------------------------------------------------
    # 2. Cleanliness score by risk
    # ---------------------------------------------------------
    print("\nAverage Cleanliness Score by Risk:")
    print(
        df.groupby("hygiene_risk")["cleanliness_score"]
        .mean()
        .round(2)
    )

    plt.figure(figsize=(8, 5))
    df.boxplot(
        column="cleanliness_score",
        by="hygiene_risk"
    )
    plt.title("Cleanliness Score by Hygiene Risk")
    plt.suptitle("")
    plt.xlabel("Hygiene Risk")
    plt.ylabel("Cleanliness Score")
    plt.tight_layout()

    path = OUTPUT_DIR / "02_cleanliness_by_risk.png"
    plt.savefig(path)
    plt.close()

    # ---------------------------------------------------------
    # 3. Waste level by risk
    # ---------------------------------------------------------
    print("\nAverage Waste Level by Risk:")
    print(
        df.groupby("hygiene_risk")["waste_level"]
        .mean()
        .round(2)
    )

    plt.figure(figsize=(8, 5))
    df.boxplot(
        column="waste_level",
        by="hygiene_risk"
    )
    plt.title("Waste Level by Hygiene Risk")
    plt.suptitle("")
    plt.xlabel("Hygiene Risk")
    plt.ylabel("Waste Level")
    plt.tight_layout()

    path = OUTPUT_DIR / "03_waste_by_risk.png"
    plt.savefig(path)
    plt.close()

    # ---------------------------------------------------------
    # 4. Complaints by risk
    # ---------------------------------------------------------
    print("\nAverage Complaints by Risk:")
    print(
        df.groupby("hygiene_risk")["complaints"]
        .mean()
        .round(2)
    )

    plt.figure(figsize=(8, 5))
    df.groupby("hygiene_risk")["complaints"].mean().plot(
        kind="bar"
    )
    plt.title("Average Complaints by Hygiene Risk")
    plt.xlabel("Hygiene Risk")
    plt.ylabel("Average Complaints")
    plt.xticks(rotation=0)
    plt.tight_layout()

    path = OUTPUT_DIR / "04_complaints_by_risk.png"
    plt.savefig(path)
    plt.close()

    # ---------------------------------------------------------
    # 5. Hours since cleaning by risk
    # ---------------------------------------------------------
    print("\nAverage Hours Since Cleaning by Risk:")
    print(
        df.groupby("hygiene_risk")["hours_since_cleaning"]
        .mean()
        .round(2)
    )

    plt.figure(figsize=(8, 5))
    df.groupby("hygiene_risk")["hours_since_cleaning"].mean().plot(
        kind="bar"
    )
    plt.title("Average Hours Since Cleaning by Hygiene Risk")
    plt.xlabel("Hygiene Risk")
    plt.ylabel("Hours Since Cleaning")
    plt.xticks(rotation=0)
    plt.tight_layout()

    path = OUTPUT_DIR / "05_cleaning_time_by_risk.png"
    plt.savefig(path)
    plt.close()

    # ---------------------------------------------------------
    # 6. Facility type distribution
    # ---------------------------------------------------------
    facility_counts = df["facility_type"].value_counts()

    print("\nFacility Type Distribution:")
    print(facility_counts)

    plt.figure(figsize=(9, 5))
    facility_counts.plot(kind="bar")
    plt.title("Facility Type Distribution")
    plt.xlabel("Facility Type")
    plt.ylabel("Number of Facilities")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()

    path = OUTPUT_DIR / "06_facility_type_distribution.png"
    plt.savefig(path)
    plt.close()

    print("\n" + "=" * 70)
    print("EDA COMPLETED")
    print(f"Visualizations saved to: {OUTPUT_DIR}")
    print("=" * 70)


if __name__ == "__main__":
    main()
    