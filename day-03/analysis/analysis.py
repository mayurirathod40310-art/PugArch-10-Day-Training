import pandas as pd
import numpy as np
from pathlib import Path

# Get the day-03 folder
day3_folder = Path(__file__).resolve().parents[1]

# Load cleaned dataset
input_file = day3_folder / "data-cleaning" / "cleaned_facility_data.csv"

df = pd.read_csv(input_file)

print("\n========== NUMPY OPERATIONS ==========")

cleanliness_array = df["cleanliness_score"].to_numpy()

print("Array:", cleanliness_array)
print("Dimensions:", cleanliness_array.ndim)
print("Shape:", cleanliness_array.shape)
print("First Value:", cleanliness_array[0])
print("First 5 Values:", cleanliness_array[:5])
print("Mean:", np.mean(cleanliness_array))
print("Sum:", np.sum(cleanliness_array))
print("Minimum:", np.min(cleanliness_array))
print("Maximum:", np.max(cleanliness_array))

print("========== DATASET OVERVIEW ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== KEY STATISTICS ==========")

numeric_columns = [
    "cleanliness_score",
    "odor_score",
    "footfall",
    "complaints"
]

print(df[numeric_columns].describe())

print("\n========== LOCATION-WISE AVERAGES ==========")

location_summary = df.groupby("location")[numeric_columns].mean().round(2)

print(location_summary)

print("\n========== WASTE LEVEL DISTRIBUTION ==========")

print(df["waste_level"].value_counts())

print("\n========== WATER AVAILABILITY ==========")

print(df["water_availability"].value_counts())

print("\n========== CORRELATION MATRIX ==========")

correlation = df[numeric_columns].corr().round(2)

print(correlation)

print("\n========== HIGHEST COMPLAINT FACILITIES ==========")

highest_complaints = df.nlargest(5, "complaints")[
    ["facility_id", "location", "cleanliness_score", "odor_score", "complaints"]
]

print(highest_complaints)

print("\n========== LOWEST CLEANLINESS FACILITIES ==========")

lowest_cleanliness = df.nsmallest(5, "cleanliness_score")[
    ["facility_id", "location", "cleanliness_score", "odor_score", "complaints"]
]

print(lowest_cleanliness)

print("\n========== USEFUL INSIGHTS ==========")

# Insight 1
location_cleanliness = df.groupby("location")["cleanliness_score"].mean()
lowest_location = location_cleanliness.idxmin()
lowest_location_score = location_cleanliness.min()

print(
    f"1. {lowest_location} has the lowest average cleanliness score "
    f"({lowest_location_score:.2f})."
)

# Insight 2
complaint_correlation = df["complaints"].corr(df["cleanliness_score"])

print(
    f"2. Cleanliness score and complaints have a correlation of "
    f"{complaint_correlation:.2f}."
)

# Insight 3
high_waste = df[df["waste_level"] == "High"]

print(
    f"3. {len(high_waste)} facilities have a high waste level."
)

# Additional insight
no_water = df[df["water_availability"] == "No"]

print(
    f"4. {len(no_water)} facilities report no water availability."
)

