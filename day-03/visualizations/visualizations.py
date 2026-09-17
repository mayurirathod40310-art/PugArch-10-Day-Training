
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ==================== FILE PATHS ====================

day3_folder = Path(__file__).resolve().parents[1]

input_file = (
    day3_folder
    / "data-cleaning"
    / "cleaned_facility_hygiene_dataset.csv"
)

output_folder = (
    day3_folder
    / "visualizations"
)

output_folder.mkdir(exist_ok=True)

# Read cleaned dataset
df = pd.read_csv(input_file)


# =====================================================
# 1. BAR CHART - AVERAGE CLEANLINESS BY LOCATION
# =====================================================

cleanliness_by_location = (
    df.groupby("location")["cleanliness_score"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(10, 6))

cleanliness_by_location.plot(kind="bar")

plt.title("Average Cleanliness Score by Location")
plt.xlabel("Location")
plt.ylabel("Average Cleanliness Score")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    output_folder / "bar_chart_cleanliness_by_location.png",
    dpi=150
)

plt.close()


# =====================================================
# 2. BAR CHART - AVERAGE COMPLAINTS BY LOCATION
# =====================================================

complaints_by_location = (
    df.groupby("location")["complaints"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

complaints_by_location.plot(kind="bar")

plt.title("Average Complaints by Location")
plt.xlabel("Location")
plt.ylabel("Average Complaints")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    output_folder / "bar_chart_complaints_by_location.png",
    dpi=150
)

plt.close()


# =====================================================
# 3. HISTOGRAM - CLEANLINESS SCORE DISTRIBUTION
# =====================================================

plt.figure(figsize=(8, 6))

plt.hist(
    df["cleanliness_score"],
    bins=10,
    edgecolor="black"
)

plt.title("Distribution of Cleanliness Scores")
plt.xlabel("Cleanliness Score")
plt.ylabel("Number of Facilities")
plt.tight_layout()

plt.savefig(
    output_folder / "histogram_cleanliness_scores.png",
    dpi=150
)

plt.close()


# =====================================================
# 4. SCATTER PLOT - CLEANLINESS VS COMPLAINTS
# =====================================================

plt.figure(figsize=(8, 6))

plt.scatter(
    df["cleanliness_score"],
    df["complaints"],
    alpha=0.6
)

plt.title("Cleanliness Score vs Complaints")
plt.xlabel("Cleanliness Score")
plt.ylabel("Number of Complaints")
plt.tight_layout()

plt.savefig(
    output_folder / "scatter_cleanliness_vs_complaints.png",
    dpi=150
)

plt.close()


# =====================================================
# 5. ADDITIONAL VISUALIZATION - HYGIENE RISK
# =====================================================

risk_counts = (
    df["hygiene_risk"]
    .value_counts()
    .reindex(["Low", "Medium", "High"])
)

plt.figure(figsize=(8, 6))

risk_counts.plot(kind="bar")

plt.title("Hygiene Risk Distribution")
plt.xlabel("Hygiene Risk")
plt.ylabel("Number of Facilities")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    output_folder / "hygiene_risk_distribution.png",
    dpi=150
)

plt.close()


# ==================== COMPLETION MESSAGE ====================

print("All 5 visualizations created successfully.")

print("\nFiles saved in:")
print(output_folder)

