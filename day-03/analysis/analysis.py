import pandas as pd
import numpy as np
from pathlib import Path

day3_folder = Path(__file__).resolve().parents[1]

input_file = (
    day3_folder
    / "data-cleaning"
    / "cleaned_facility_hygiene_dataset.csv"
)

df = pd.read_csv(input_file)

# Convert date column
df["inspection_date"] = pd.to_datetime(
    df["inspection_date"]
)


# ==================== NUMPY OPERATIONS ====================

print("\n========== NUMPY OPERATIONS ==========")

cleanliness_array = df[
    "cleanliness_score"
].to_numpy()

print("Dimensions:", cleanliness_array.ndim)
print("Shape:", cleanliness_array.shape)
print("First Value:", cleanliness_array[0])
print(
    "First 5 Values:",
    cleanliness_array[:5]
)
print(
    "Mean:",
    np.mean(cleanliness_array)
)
print(
    "Minimum:",
    np.min(cleanliness_array)
)
print(
    "Maximum:",
    np.max(cleanliness_array)
)


# ==================== DATASET OVERVIEW ====================

print("\n========== DATASET OVERVIEW ==========")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())


# ==================== DATA TYPES ====================

print("\n========== DATA TYPES ==========")

print(df.dtypes)


# ==================== KEY STATISTICS ====================

print("\n========== KEY STATISTICS ==========")

numeric_columns = [
    "cleanliness_score",
    "odor_score",
    "waste_level",
    "footfall",
    "complaints",
    "hours_since_cleaning"
]

print(
    df[numeric_columns]
    .describe()
    .round(2)
)


# ==================== LOCATION ANALYSIS ====================

print("\n========== LOCATION-WISE AVERAGES ==========")

location_summary = (
    df.groupby("location")[numeric_columns]
    .mean()
    .round(2)
)

print(location_summary)


# ==================== FACILITY TYPE ====================

print(
    "\n========== FACILITY TYPE DISTRIBUTION =========="
)

print(
    df["facility_type"].value_counts()
)


# ==================== WASTE LEVEL ====================

print(
    "\n========== WASTE LEVEL STATISTICS =========="
)

print(
    df["waste_level"]
    .describe()
    .round(2)
)


# ==================== WATER AVAILABILITY ====================

print("\n========== WATER AVAILABILITY ==========")

print(
    df["water_availability"].value_counts()
)


# ==================== HYGIENE RISK ====================

print(
    "\n========== HYGIENE RISK DISTRIBUTION =========="
)

print(
    df["hygiene_risk"].value_counts()
)


# ==================== CORRELATION ====================

print("\n========== CORRELATION MATRIX ==========")

correlation = (
    df[numeric_columns]
    .corr()
    .round(2)
)

print(correlation)


# ==================== HIGHEST COMPLAINTS ====================

print(
    "\n========== HIGHEST COMPLAINT FACILITIES =========="
)

highest_complaints = df.nlargest(
    5,
    "complaints"
)[
    [
        "facility_id",
        "location",
        "facility_type",
        "cleanliness_score",
        "complaints",
        "hygiene_risk"
    ]
]

print(highest_complaints)


# ==================== LOWEST CLEANLINESS ====================

print(
    "\n========== LOWEST CLEANLINESS FACILITIES =========="
)

lowest_cleanliness = df.nsmallest(
    5,
    "cleanliness_score"
)[
    [
        "facility_id",
        "location",
        "facility_type",
        "cleanliness_score",
        "complaints",
        "hygiene_risk"
    ]
]

print(lowest_cleanliness)


# ==================== USEFUL INSIGHTS ====================

print("\n========== USEFUL INSIGHTS ==========")

location_cleanliness = (
    df.groupby("location")["cleanliness_score"]
    .mean()
)

lowest_location = location_cleanliness.idxmin()
lowest_score = location_cleanliness.min()

print(
    f"1. {lowest_location} has the lowest average "
    f"cleanliness score ({lowest_score:.2f})."
)

complaint_correlation = (
    df["cleanliness_score"]
    .corr(df["complaints"])
)

print(
    f"2. Cleanliness score and complaints have a "
    f"correlation of {complaint_correlation:.2f}."
)

high_waste = (
    df["waste_level"] >= 70
).sum()

print(
    f"3. {high_waste} facilities have waste-bin "
    f"fullness of 70% or higher."
)

no_water = (
    df["water_availability"] == "No"
).sum()

print(
    f"4. {no_water} facilities report no water "
    f"availability."
)

high_risk = (
    df["hygiene_risk"] == "High"
).sum()

print(
    f"5. {high_risk} facilities are classified "
    f"as high hygiene risk."
)

