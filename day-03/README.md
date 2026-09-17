# Day 3 - Data Analysis & Visualization

## Objective

Analyze, clean, and visualize facility hygiene data using Python, NumPy, Pandas, and Matplotlib.

## Dataset

The official Facility Hygiene dataset provided for the training task was used.

- Original records: 1000
- Columns: 12
- Cleaned records: 995
- Dataset contains facility information, hygiene scores, complaints, cleaning time, and hygiene risk.

## Data Cleaning

The following cleaning operations were performed:

- Checked for missing values
- Removed duplicate rows
- Filled missing numeric values using median
- Filled missing water availability using mode
- Checked invalid cleanliness and odor scores
- Converted inspection dates to datetime format
- Detected numerical outliers using the IQR method

### Cleaning Results

- Missing cleanliness scores: 5
- Missing waste level values: 3
- Missing water availability values: 2
- Duplicate rows removed: 5
- Invalid cleanliness scores: 0
- Invalid odor scores: 0

### Detected Outliers

- Cleanliness score: 2
- Footfall: 3
- Complaints: 13
- Hours since cleaning: 62

## Data Analysis

The analysis included:

- NumPy arrays, dimensions, shape, indexing, slicing, and aggregation
- Pandas DataFrame operations
- Descriptive statistics
- Location-wise analysis
- Facility type distribution
- Water availability analysis
- Hygiene risk distribution
- Correlation analysis
- Highest complaint facilities
- Lowest cleanliness facilities

## Key Statistics

- Average cleanliness score: 6.42
- Average waste-bin fullness: 43.86%
- Highest cleanliness location average: Manish Nagar (6.62)
- Lowest cleanliness location average: Sitabuldi (6.09)

## Key Insights

1. Sitabuldi has the lowest average cleanliness score at 6.09.
2. Cleanliness score and complaints have a correlation of -0.66, indicating a moderate negative association.
3. 105 facilities have waste-bin fullness of 70% or higher.
4. 118 facilities report no water availability.
5. 272 facilities are classified as High hygiene risk.
6. The five facilities with the lowest cleanliness scores are all classified as High hygiene risk.

## Visualizations

The following visualizations were created using Matplotlib:

1. Average cleanliness score by location
2. Average complaints by location
3. Cleanliness score distribution histogram
4. Cleanliness score vs complaints scatter plot
5. Hygiene risk distribution

## Tools Used

- Python
- NumPy
- Pandas
- Matplotlib
- VS Code

## Folder Structure

day-03/
│
├── dataset/
│   └── facility_hygiene_ml_dataset.xlsx
│
├── data-cleaning/
│   ├── data_cleaning.py
│   └── cleaned_facility_hygiene_dataset.csv
│
├── analysis/
│   └── analysis.py
│
├── visualizations/
│   ├── visualizations.py
│   ├── bar_chart_cleanliness_by_location.png
│   ├── bar_chart_complaints_by_location.png
│   ├── histogram_cleanliness_scores.png
│   ├── scatter_cleanliness_vs_complaints.png
│   └── hygiene_risk_distribution.png
│
└── README.md


## Conclusion

The facility hygiene dataset was successfully cleaned, analyzed, and visualized. The analysis identified missing values, duplicates, outliers, statistical patterns, and relationships between hygiene-related variables.