import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Get day-03 folder
day3_folder = Path(__file__).resolve().parents[1]

# Load cleaned dataset
input_file = day3_folder / "data-cleaning" / "cleaned_facility_data.csv"

df = pd.read_csv(input_file)

# --------------------------------------------------
# 1. Bar Chart - Average Cleanliness by Location
# --------------------------------------------------

cleanliness_by_location = (
    df.groupby("location")["cleanliness_score"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(8, 5))
cleanliness_by_location.plot(kind="bar")
plt.title("Average Cleanliness Score by Location")
plt.xlabel("Location")
plt.ylabel("Average Cleanliness Score")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(day3_folder / "visualizations" / "bar_chart_1.png")
plt.close()


# --------------------------------------------------
# 2. Bar Chart - Average Complaints by Location
# --------------------------------------------------

complaints_by_location = (
    df.groupby("location")["complaints"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
complaints_by_location.plot(kind="bar")
plt.title("Average Complaints by Location")
plt.xlabel("Location")
plt.ylabel("Average Complaints")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(day3_folder / "visualizations" / "bar_chart_2.png")
plt.close()


# --------------------------------------------------
# 3. Histogram - Cleanliness Score Distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))
plt.hist(df["cleanliness_score"], bins=8, edgecolor="black")
plt.title("Distribution of Cleanliness Scores")
plt.xlabel("Cleanliness Score")
plt.ylabel("Number of Facilities")
plt.tight_layout()

plt.savefig(day3_folder / "visualizations" / "histogram.png")
plt.close()


# --------------------------------------------------
# 4. Scatter Plot - Cleanliness vs Complaints
# --------------------------------------------------

plt.figure(figsize=(8, 5))
plt.scatter(df["cleanliness_score"], df["complaints"])
plt.title("Cleanliness Score vs Complaints")
plt.xlabel("Cleanliness Score")
plt.ylabel("Complaints")
plt.tight_layout()

plt.savefig(day3_folder / "visualizations" / "scatter_plot.png")
plt.close()


# --------------------------------------------------
# 5. Additional Visualization - Waste Level
# --------------------------------------------------

waste_counts = df["waste_level"].value_counts()

plt.figure(figsize=(8, 5))
waste_counts.plot(kind="bar")
plt.title("Facilities by Waste Level")
plt.xlabel("Waste Level")
plt.ylabel("Number of Facilities")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    day3_folder / "visualizations" / "additional_visualization.png"
)
plt.close()


print("All 5 visualizations created successfully.")

