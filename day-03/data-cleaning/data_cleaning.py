import pandas as pd
import numpy as np
from pathlib import Path

day3_folder = Path(__file__).resolve().parents[1]

input_file = day3_folder / "dataset" / "facility_hygiene_ml_dataset.xlsx"
output_file = day3_folder / "data-cleaning" / "cleaned_facility_hygiene_dataset.csv"

# Read Excel dataset
df = pd.read_excel(input_file, sheet_name="Facility Hygiene Dataset")

print("Original Dataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Handle missing numeric values
numeric_columns = [
    "cleanliness_score",
    "odor_score",
    "footfall",
    "complaints",
    "hours_since_cleaning"
]

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Handle missing categorical values
categorical_columns = [
    "waste_level",
    "water_availability"
]

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

# Convert inspection date
df["inspection_date"] = pd.to_datetime(df["inspection_date"])

# Check invalid score values
invalid_cleanliness = (
    (df["cleanliness_score"] < 0) |
    (df["cleanliness_score"] > 100)
)

invalid_odor = (
    (df["odor_score"] < 0) |
    (df["odor_score"] > 10)
)

print("\nInvalid Cleanliness Scores:", invalid_cleanliness.sum())
print("Invalid Odor Scores:", invalid_odor.sum())

# Replace invalid values with median
df.loc[invalid_cleanliness, "cleanliness_score"] = np.nan
df.loc[invalid_odor, "odor_score"] = np.nan

df["cleanliness_score"] = df["cleanliness_score"].fillna(
    df["cleanliness_score"].median()
)

df["odor_score"] = df["odor_score"].fillna(
    df["odor_score"].median()
)

# Outlier detection using IQR
print("\nOutlier Detection:")

for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    print(f"{column}: {len(outliers)} outlier(s)")

# Save cleaned dataset
df.to_csv(output_file, index=False)

print("\nCleaning completed successfully.")
print("Cleaned Dataset Shape:", df.shape)
print("Saved as:", output_file)

