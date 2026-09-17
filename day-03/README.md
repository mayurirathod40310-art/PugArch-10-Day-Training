# Day 3 — Data Analysis & Visualization

## Objective

Analyze, clean, and visualize facility hygiene data using Python, NumPy, Pandas, and Matplotlib.

## Problem Statement

The objective of this task is to inspect and analyze a real-world facility hygiene dataset, identify data quality issues, calculate useful statistics, discover patterns, and communicate findings through visualizations.

## Dataset

The official Facility Hygiene dataset provided for the training task was used.

* Original records: 1000
* Columns: 12
* Cleaned records: 995
* Dataset contains facility information, hygiene scores, complaints, cleaning time, and hygiene risk.

## Features

The project includes:

* Data quality inspection
* Missing-value analysis and handling
* Duplicate detection and removal
* Invalid-value validation
* Date conversion
* Numerical outlier detection using the IQR method
* Descriptive statistics
* Location-wise analysis
* Correlation analysis
* Hygiene risk analysis
* Multiple Matplotlib visualizations

## Data Cleaning

The following cleaning operations were performed:

* Checked for missing values
* Removed duplicate rows
* Filled missing numeric values using median
* Filled missing water availability using mode
* Checked invalid cleanliness and odor scores
* Converted inspection dates to datetime format
* Detected numerical outliers using the IQR method

### Cleaning Results

* Missing cleanliness scores: 5
* Missing waste level values: 3
* Missing water availability values: 2
* Duplicate rows removed: 5
* Invalid cleanliness scores: 0
* Invalid odor scores: 0

### Detected Outliers

* Cleanliness score: 2
* Footfall: 3
* Complaints: 13
* Hours since cleaning: 62

## Data Analysis

The analysis included:

* NumPy arrays, dimensions, shape, indexing, slicing, and aggregation
* Pandas DataFrame operations
* Descriptive statistics
* Location-wise analysis
* Facility type distribution
* Water availability analysis
* Hygiene risk distribution
* Correlation analysis
* Highest complaint facilities
* Lowest cleanliness facilities

## Key Statistics

* Average cleanliness score: 6.42
* Average waste-bin fullness: 43.86%
* Highest cleanliness location average: Manish Nagar (6.62)
* Lowest cleanliness location average: Sitabuldi (6.09)

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

## Technology Stack

* Python
* NumPy
* Pandas
* Matplotlib
* VS Code

## Architecture

The project follows a simple data-analysis pipeline:

```text
Raw Dataset
    ↓
Data Cleaning
    ↓
Cleaned Dataset
    ↓
Data Analysis
    ↓
Statistics & Insights
    ↓
Visualizations
```

## Installation

### Prerequisites

* Python 3.x
* pip
* VS Code

### Required Libraries

Install the required Python libraries:

```bash
pip install numpy pandas matplotlib openpyxl
```

## How to Run

### 1. Data Cleaning

Navigate to the data-cleaning directory:

```bash
cd data-cleaning
python data_cleaning.py
```

### 2. Analysis

Navigate to the analysis directory:

```bash
cd ../analysis
python analysis.py
```

### 3. Visualizations

Navigate to the visualizations directory:

```bash
cd ../visualizations
python visualizations.py
```

The generated visualization files are saved in the `visualizations/` directory.

## Challenges Faced

* Handling missing values in different columns.
* Detecting duplicate and invalid records.
* Identifying numerical outliers.
* Converting and processing inspection dates.
* Extracting meaningful insights from multiple hygiene-related variables.
* Presenting analysis results through appropriate visualizations.

## Solutions

* Used median imputation for missing numeric values.
* Used mode imputation for missing water availability values.
* Removed duplicate records.
* Validated cleanliness and odor score ranges.
* Converted inspection dates to datetime format.
* Used the IQR method for numerical outlier detection.
* Used Pandas, NumPy, and Matplotlib for analysis and visualization.

## Future Improvements

* Add an interactive dashboard using Streamlit.
* Perform more advanced statistical analysis.
* Add automated data-quality checks.
* Explore predictive machine learning models using the cleaned dataset.
* Add more interactive visualizations.

## Folder Structure

```text
day-03/
├── dataset/
│   └── facility_hygiene_ml_dataset.xlsx
├── data-cleaning/
│   ├── data_cleaning.py
│   └── cleaned_facility_hygiene_dataset.csv
├── analysis/
│   └── analysis.py
├── visualizations/
│   ├── visualizations.py
│   ├── bar_chart_cleanliness_by_location.png
│   ├── bar_chart_complaints_by_location.png
│   ├── histogram_cleanliness_scores.png
│   ├── scatter_cleanliness_vs_complaints.png
│   └── hygiene_risk_distribution.png
└── README.md
```

## Conclusion

The facility hygiene dataset was successfully cleaned, analyzed, and visualized. The analysis identified missing values, duplicates, outliers, statistical patterns, and relationships between hygiene-related variables.
