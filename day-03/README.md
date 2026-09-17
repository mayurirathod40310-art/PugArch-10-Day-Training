# Day 3 - Data Analysis & Visualization

## Objective

Analyze, clean, and visualize a facility inspection dataset using Python, NumPy, Pandas, and Matplotlib.

## Dataset

The dataset contains 41 facility inspection records with information about:

- Cleanliness
- Odor
- Waste level
- Water availability
- Footfall
- Complaints
- Inspection date

After cleaning, 40 records remained.

## Data Cleaning

The following steps were performed:

- Checked missing values and data types
- Removed 1 duplicate row
- Handled 5 missing values
- Corrected 3 invalid score values
- Filled missing numeric values using median
- Filled missing categorical values using mode
- Detected potential outliers using the IQR method
- Converted inspection dates to date format

## Analysis

Key statistics:

| Metric | Average |
|---|---:|
| Cleanliness Score | 77.30 |
| Odor Score | 3.25 |
| Footfall | 608.25 |
| Complaints | 6.73 |

### Key Insights

1. Yavatmal has the lowest average cleanliness score (68.00).
2. Cleanliness and complaints have a strong negative correlation (-0.93).
3. 11 facilities have a high waste level.
4. 11 facilities report no water availability.

## NumPy

NumPy was used for:

- Arrays and dimensions
- Shape, indexing, and slicing
- Mean, sum, minimum, and maximum calculations

## Visualizations

Created 5 visualizations using Matplotlib:

- Average cleanliness by location
- Average complaints by location
- Cleanliness score distribution
- Cleanliness vs complaints
- Facilities by waste level

## Project Structure

day-03/
├── dataset/
│   └── facility_data.csv
├── data-cleaning/
│   ├── data_cleaning.py
│   └── cleaned_facility_data.csv
├── analysis/
│   └── analysis.py
├── visualizations/
│   ├── visualizations.py
│   ├── bar_chart_1.png
│   ├── bar_chart_2.png
│   ├── histogram.png
│   ├── scatter_plot.png
│   └── additional_visualization.png
└── README.md

## Technologies Used

Python | NumPy | Pandas | Matplotlib

## HOw to Run 
.\venv\Scripts\python.exe day-03\data-cleaning\data_cleaning.py
.\venv\Scripts\python.exe day-03\analysis\analysis.py
.\venv\Scripts\python.exe day-03\visualizations\visualizations.py

