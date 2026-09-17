# Day 4 — Machine Learning Fundamentals

## Objective

Build a machine learning pipeline to predict facility hygiene risk using facility hygiene data.

## Dataset

The project uses the `facility_hygiene_ml_dataset.xlsx` dataset from Day 3.

The dataset contains **1000 records and 12 columns**. After preprocessing, **995 records** remained.

### Target

* `hygiene_risk` — High, Medium, Low

### Features Used

* `cleanliness_score`
* `odor_score`
* `waste_level`
* `complaints`
* `footfall`
* `hours_since_cleaning`

## Preprocessing

The preprocessing script:

* Loads the Excel dataset
* Removes duplicate records
* Converts numeric columns to numeric values
* Handles missing values
* Converts inspection dates
* Removes invalid numeric values
* Saves the cleaned dataset as CSV

Output:

`day-04/preprocessing/cleaned_dataset.csv`

## Machine Learning Models

Two classification algorithms were trained:

1. Logistic Regression
2. Random Forest Classifier

The data was divided into:

* 80% training data
* 20% testing data

Feature scaling using `StandardScaler` was applied to Logistic Regression.

## Model Results

| Model               | Accuracy | Precision | Recall | F1 Score |
| ------------------- | -------: | --------: | -----: | -------: |
| Logistic Regression |   90.45% |    90.65% | 90.45% |   90.49% |
| Random Forest       |   86.43% |    87.14% | 86.43% |   86.52% |

## Evaluation

The Logistic Regression model was evaluated using:

* Classification Report
* Confusion Matrix

The model achieved approximately **90% accuracy** on the test set.

## Prediction

A separate prediction script accepts new facility measurements and predicts the hygiene risk level.

Example prediction:

`High`

## Project Structure

```text
day-04/
├── dataset/
├── preprocessing/
│   ├── preprocess.py
│   └── cleaned_dataset.csv
├── models/
│   ├── train_model.py
│   ├── logistic_regression.pkl
│   ├── random_forest.pkl
│   ├── label_encoder.pkl
│   └── scaler.pkl
├── evaluation/
│   └── evaluate_model.py
├── predictions/
│   └── predict.py
└── README.md
```

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* Excel/CSV
* VS Code

## Conclusion

A complete machine learning workflow was implemented for facility hygiene-risk classification, including preprocessing, model training, evaluation, and prediction.

