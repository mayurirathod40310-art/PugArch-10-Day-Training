import pandas as pd
from pathlib import Path

# File paths
BASE_DIR = Path(__file__).resolve().parents[2]

INPUT_FILE = BASE_DIR / "day-03" / "dataset" / "facility_hygiene_ml_dataset.xlsx"
OUTPUT_DIR = BASE_DIR / "day-04" / "preprocessing"
OUTPUT_FILE = OUTPUT_DIR / "cleaned_dataset.csv"


# Load dataset
df = pd.read_excel(INPUT_FILE)

print("Original dataset shape:", df.shape)
print("\nOriginal columns:")
print(df.columns.tolist())


# Remove duplicate rows
df = df.drop_duplicates()

# Convert inspection date
if "inspection_date" in df.columns:
    df["inspection_date"] = pd.to_datetime(
        df["inspection_date"],
        errors="coerce"
    )


# Convert numeric columns
numeric_columns = [
    "cleanliness_score",
    "odor_score",
    "waste_level",
    "water_availability",
    "footfall",
    "complaints"
]

for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")


# Fill missing numeric values with median
for column in numeric_columns:
    if column in df.columns:
        df[column] = df[column].fillna(df[column].median())


# Fill missing categorical values
categorical_columns = ["facility_id", "location"]

for column in categorical_columns:
    if column in df.columns:
        df[column] = df[column].fillna("Unknown")


# Remove invalid values
if "cleanliness_score" in df.columns:
    df = df[df["cleanliness_score"].between(0, 100)]

if "odor_score" in df.columns:
    df = df[df["odor_score"].between(0, 100)]

if "waste_level" in df.columns:
    df = df[df["waste_level"] >= 0]

if "footfall" in df.columns:
    df = df[df["footfall"] >= 0]

if "complaints" in df.columns:
    df = df[df["complaints"] >= 0]


# Save cleaned dataset
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)


print("\nCleaning completed successfully.")
print("Cleaned dataset shape:", df.shape)
print("Saved to:", OUTPUT_FILE)

