import pandas as pd
import numpy as np

from pathlib import Path

# Get the day-03 folder
day3_folder = Path(__file__).resolve().parents[1]

input_file = day3_folder / "dataset" / "facility_data.csv"
output_file = day3_folder / "data-cleaning" / "cleaned_facility_data.csv"

df = pd.read_csv(input_file)

print("Original Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

# --------------------------------------------------
# 1. Check missing values
# --------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# --------------------------------------------------
# 2. Check duplicate rows
# --------------------------------------------------

print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# --------------------------------------------------
# 3. Check invalid values
# --------------------------------------------------

# Cleanliness score should be between 0 and 100
invalid_cleanliness = (df["cleanliness_score"] < 0) | (
    df["cleanliness_score"] > 100
)

print("\nInvalid Cleanliness Scores:")
print(df[invalid_cleanliness])

# Replace invalid values with NaN
df.loc[invalid_cleanliness, "cleanliness_score"] = np.nan

# Odor score should be between 0 and 10
invalid_odor = (df["odor_score"] < 0) | (df["odor_score"] > 10)

print("\nInvalid Odor Scores:")
print(df[invalid_odor])

# Replace invalid values with NaN
df.loc[invalid_odor, "odor_score"] = np.nan

# --------------------------------------------------
# 4. Handle missing values
# --------------------------------------------------

# Numeric columns
numeric_columns = [
    "cleanliness_score",
    "odor_score",
    "footfall",
    "complaints"
]

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Categorical column
df["waste_level"] = df["waste_level"].fillna(df["waste_level"].mode()[0])

# --------------------------------------------------
# 5. Convert date column
# --------------------------------------------------

df["inspection_date"] = pd.to_datetime(df["inspection_date"])

# --------------------------------------------------
# 6. Detect outliers using IQR
# --------------------------------------------------

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

# --------------------------------------------------
# 7. Save cleaned dataset
# --------------------------------------------------

df.to_csv(output_file, index=False)

print("\nCleaning completed successfully.")
print("Cleaned Dataset Shape:", df.shape)


