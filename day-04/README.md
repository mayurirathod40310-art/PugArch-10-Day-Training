# Day 4 — Machine Learning Fundamentals

## Objective

Build a machine learning pipeline to predict facility hygiene risk using facility hygiene data.

## Problem Statement

The objective of this task is to build a basic machine learning classification system that predicts facility hygiene risk based on hygiene-related facility measurements.

The project follows the complete machine learning workflow:

```text
Dataset
  ↓
Preprocessing
  ↓
Feature Engineering
  ↓
Train/Test Split
  ↓
Model Training
  ↓
Prediction
  ↓
Evaluation
```

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

## Features

The project includes:

* Data preprocessing
* Missing-value handling
* Duplicate removal
* Invalid-value handling
* Feature preparation
* Train/test splitting
* Feature scaling
* Classification model training
* Model comparison
* Model evaluation
* Hygiene risk prediction for new facility measurements

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

```text
day-04/preprocessing/cleaned_dataset.csv
```

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

The models were evaluated using classification metrics including:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

Regression error metrics covered in the training evaluation include:

* MAE
* MSE
* RMSE

The classification results were used to compare the performance of the trained models on the test dataset.

## Prediction

A separate prediction script accepts new facility measurements and predicts the hygiene risk level.

Example prediction:

```text
High
```

## Architecture

```text
Raw Facility Dataset
        ↓
Data Preprocessing
        ↓
Cleaned Dataset
        ↓
Feature Selection & Preparation
        ↓
Train/Test Split
        ↓
 ┌─────────────────────┐
 │                     │
Logistic Regression   Random Forest
 │                     │
 └──────────┬──────────┘
            ↓
       Model Evaluation
            ↓
      Hygiene Risk Prediction
```

## Technology Stack

* Python
* Pandas
* Scikit-learn
* Joblib
* Excel/CSV
* VS Code

## Installation

### Prerequisites

* Python 3.x
* pip
* VS Code

### Required Libraries

Install the required libraries:

```bash
pip install pandas scikit-learn joblib openpyxl
```

## How to Run

### 1. Preprocessing

Navigate to the preprocessing directory:

```bash
cd preprocessing
python preprocess.py
```

### 2. Train Models

Navigate to the models directory:

```bash
cd ../models
python train_model.py
```

### 3. Evaluate the Model

Navigate to the evaluation directory:

```bash
cd ../evaluation
python evaluate_model.py
```

### 4. Make a Prediction

Navigate to the predictions directory:

```bash
cd ../predictions
python predict.py
```

## Challenges Faced

* Preparing the dataset for machine learning.
* Handling missing, duplicate, and invalid values.
* Preparing categorical target labels for model training.
* Comparing multiple classification algorithms.
* Applying feature scaling where required.
* Evaluating model performance using multiple metrics.

## Solutions

* Used preprocessing steps to clean and prepare the dataset.
* Handled missing and invalid values before model training.
* Used label encoding for the target variable.
* Trained and compared Logistic Regression and Random Forest models.
* Applied `StandardScaler` to Logistic Regression.
* Used classification metrics and a confusion matrix for evaluation.
* Saved trained models and preprocessing objects using Joblib.

## Future Improvements

* Perform additional feature selection and engineering.
* Test additional machine learning algorithms.
* Tune model hyperparameters.
* Add cross-validation.
* Expose the prediction model through a REST API.
* Add a user interface for entering facility measurements and viewing predictions.

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

## Conclusion

A complete machine learning workflow was implemented for facility hygiene-risk classification, including preprocessing, feature preparation, model training, model comparison, evaluation, and prediction.
