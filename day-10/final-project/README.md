# Smart Hygiene Risk Prediction System

## 1. Project Overview

The **Smart Hygiene Risk Prediction System** is an AI/ML-based web application that predicts the hygiene risk level of a facility as **High, Medium, or Low**.

The system uses historical facility inspection data containing parameters such as cleanliness score, odor score, waste level, water availability, footfall, complaints, and hours since cleaning.

The project combines data preprocessing, exploratory data analysis, machine learning, REST API development, and a React-based frontend into an end-to-end prediction system.

The user enters facility information through the web interface, and the system sends the data to a FastAPI backend. The trained machine learning model then predicts the hygiene risk and returns the prediction probabilities to the frontend.

---

## 2. Problem Statement

Maintaining proper hygiene in public and institutional facilities requires monitoring several factors, including cleanliness, waste accumulation, odor, water availability, complaints, and cleaning frequency.

Manual inspection and evaluation can make it difficult to consistently identify facilities that may require attention.

This project uses historical hygiene inspection data and machine learning to classify a facility into three risk categories:

* **High Risk**
* **Medium Risk**
* **Low Risk**

The system provides a data-driven approach for demonstrating automated hygiene risk classification.

---

## 3. Features

### Machine Learning

* Dataset inspection and profiling
* Missing-value detection and handling
* Duplicate record removal
* Categorical feature encoding
* Numerical feature scaling
* Date feature extraction
* Exploratory Data Analysis
* Logistic Regression model
* Random Forest model
* Model evaluation
* Confusion matrix
* Feature importance analysis
* Trained model serialization

### Backend

* FastAPI REST API
* Health check endpoint
* Model information endpoint
* Hygiene risk prediction endpoint
* Pydantic request validation
* Prediction probabilities
* CORS configuration
* Trained ML model integration

### Frontend

* React-based user interface
* Facility information form
* Input validation
* Hygiene risk prediction
* Probability visualization
* Loading state
* Error handling
* Prediction history during the current session
* Responsive layout

---

## 4. Technology Stack

| Category                | Technology         |
| ----------------------- | ------------------ |
| Programming Languages   | Python, JavaScript |
| Frontend                | React              |
| Build Tool              | Vite               |
| Backend                 | FastAPI            |
| API Server              | Uvicorn            |
| Machine Learning        | Scikit-learn       |
| Data Processing         | Pandas, NumPy      |
| Data Visualization      | Matplotlib         |
| Data Validation         | Pydantic           |
| Model Serialization     | Joblib             |
| Dataset                 | Excel / CSV        |
| Development Environment | Visual Studio Code |
| Version Control         | Git & GitHub       |

---

## 5. Machine Learning Pipeline

The machine learning workflow consists of the following stages:

```text
Raw Dataset
    |
    v
Data Inspection
    |
    v
Data Cleaning
    |
    +--> Remove Duplicates
    |
    +--> Handle Missing Values
    |
    +--> Extract Date Features
    |
    +--> Remove Unnecessary Columns
    |
    v
Cleaned Dataset
    |
    v
Exploratory Data Analysis
    |
    v
Feature Preprocessing
    |
    +--> Numerical Features
    |       |
    |       +--> StandardScaler
    |
    +--> Categorical Features
            |
            +--> OneHotEncoder
    |
    v
Train/Test Split
    |
    +----------------------+
    |                      |
    v                      v
Logistic Regression    Random Forest
    |                      |
    +----------+-----------+
               |
               v
        Model Evaluation
               |
               v
       Best Model Selection
               |
               v
       Saved ML Model
               |
               v
        FastAPI Backend
```

---

## 6. Dataset and Data Preprocessing

The original dataset contains **1000 records and 12 columns**.

### Dataset Columns

* `facility_id`
* `location`
* `facility_type`
* `cleanliness_score`
* `odor_score`
* `waste_level`
* `water_availability`
* `footfall`
* `complaints`
* `inspection_date`
* `hours_since_cleaning`
* `hygiene_risk`

### Data Quality

The original dataset contained:

* 1000 records
* 5 duplicate records
* Missing values in `cleanliness_score`
* Missing values in `waste_level`
* Missing values in `water_availability`

After preprocessing:

* 995 records remained
* Numerical missing values were filled using the median
* Missing categorical values were filled using the mode
* `inspection_date` was converted into:

  * inspection month
  * inspection day of week
* `facility_id` was removed
* The original `inspection_date` column was removed

The final cleaned dataset contained **995 records with no missing values**.

---

## 7. Exploratory Data Analysis

EDA was performed to understand the distribution of hygiene risk and important patterns in the dataset.

The following visualizations were generated:

1. Hygiene Risk Distribution
2. Cleanliness Score by Risk
3. Waste Level by Risk
4. Complaints by Risk
5. Hours Since Cleaning by Risk
6. Facility Type Distribution
7. Feature Importance

### Hygiene Risk Distribution

| Risk Level | Records |
| ---------- | ------: |
| High       |     272 |
| Medium     |     410 |
| Low        |     313 |

### Average Values by Risk

| Feature              |  High | Medium |   Low |
| -------------------- | ----: | -----: | ----: |
| Cleanliness Score    |  4.61 |   6.25 |  8.22 |
| Waste Level          | 62.64 |  45.87 | 25.32 |
| Complaints           |  7.11 |   4.43 |  2.27 |
| Hours Since Cleaning | 10.06 |   7.34 |  5.81 |

These values describe patterns observed in the dataset. They should not be interpreted as proof that an individual feature directly causes hygiene risk.

---

## 8. Model Training and Evaluation

Two classification models were trained:

1. Logistic Regression
2. Random Forest Classifier

The dataset was divided into:

* **80% training data**
* **20% testing data**

A stratified train-test split with `random_state=42` was used.

### Logistic Regression

| Metric             |  Score |
| ------------------ | -----: |
| Accuracy           | 93.97% |
| Weighted Precision | 94.09% |
| Weighted Recall    | 93.97% |
| Weighted F1-Score  | 93.99% |

### Random Forest

| Metric             |  Score |
| ------------------ | -----: |
| Accuracy           | 89.95% |
| Weighted Precision | 90.57% |
| Weighted Recall    | 89.95% |
| Weighted F1-Score  | 90.02% |

The **Logistic Regression model was selected** because it achieved the higher weighted F1-score on the test set.

The trained model is stored at:

```text
ml/models/hygiene_risk_model.pkl
```

### Logistic Regression Confusion Matrix

```text
                Predicted
              High  Low  Medium

Actual High     50    0      4
Actual Low       0   59      4
Actual Medium    2    2     78
```

---

## 9. Feature Importance

Feature importance was analyzed using the coefficients of the trained Logistic Regression model.

Important predictive features identified by the model included:

* Cleanliness Score
* Odor Score
* Water Availability
* Complaints
* Hours Since Cleaning
* Waste Level
* Footfall
* Location-related features

The generated feature importance visualization is stored at:

```text
ml/visualizations/07_feature_importance.png
```

The coefficients represent relationships learned by the model and should not be interpreted as causal effects.

---

## 10. System Architecture

The system consists of three main layers:

```text
+-----------------------------+
|       React Frontend        |
|                             |
|  Input Form                 |
|  Validation                 |
|  Prediction Result          |
|  Probability Visualization  |
|  Prediction History         |
+--------------+--------------+
               |
               | HTTP POST /predict
               v
+-----------------------------+
|       FastAPI Backend       |
|                             |
|  Request Validation         |
|  Model Loading              |
|  Prediction                 |
|  Probability Calculation    |
+--------------+--------------+
               |
               v
+-----------------------------+
|       ML Model Pipeline     |
|                             |
|  OneHotEncoder              |
|  StandardScaler             |
|  Logistic Regression        |
+--------------+--------------+
               |
               v
+-----------------------------+
|      Trained Model (.pkl)   |
+-----------------------------+
```

### Data Flow

```text
User
 |
 v
React Frontend
 |
 | Facility Information
 v
FastAPI /predict
 |
 v
ML Preprocessing Pipeline
 |
 v
Logistic Regression
 |
 +----> Risk Prediction
 |
 +----> Prediction Probabilities
 |
 v
React Frontend
 |
 +----> Risk Result
 |
 +----> Probability Bars
 |
 +----> Prediction History
```

---

## 11. Database Design

The current version of the project does **not require a persistent database**.

Prediction history is maintained temporarily in React state during the current browser session.

Therefore:

```text
Database: Not applicable in the current version
```

The `database/` directory is included in the project structure and documents the current database decision.

A future version can use PostgreSQL or MySQL to store:

* Facility information
* Prediction history
* Prediction timestamps
* Risk results
* User information

---

## 12. API Documentation

The backend is implemented using **FastAPI**.

### Base URL

```text
http://127.0.0.1:8000
```

FastAPI interactive documentation:

```text
http://127.0.0.1:8000/docs
```

### 12.1 Health Check

**Endpoint:**

```http
GET /health
```

**Purpose:**

Checks whether the API and trained model are available.

**Response:**

```json
{
  "status": "healthy",
  "model_loaded": true
}
```

---

### 12.2 Model Information

**Endpoint:**

```http
GET /model-info
```

**Purpose:**

Returns information about the loaded ML model.

**Response:**

```json
{
  "model": "Logistic Regression",
  "classes": [
    "High",
    "Low",
    "Medium"
  ],
  "features": 11
}
```

---

### 12.3 Predict Hygiene Risk

**Endpoint:**

```http
POST /predict
```

**Purpose:**

Predicts the hygiene risk category of a facility.

**Request Body:**

```json
{
  "location": "Dharampeth",
  "facility_type": "Public Washroom",
  "cleanliness_score": 5.5,
  "odor_score": 6.0,
  "waste_level": 60,
  "water_availability": "Yes",
  "footfall": 500,
  "complaints": 6,
  "hours_since_cleaning": 10,
  "inspection_month": 9,
  "inspection_day_of_week": 5
}
```

**Example Response:**

```json
{
  "prediction": "High",
  "probabilities": {
    "High": 0.6229,
    "Low": 0,
    "Medium": 0.3771
  }
}
```

---

## 13. Project Structure

```text
day-10/
└── final-project/
    |
    ├── backend/
    |   ├── app/
    |   |   └── main.py
    |   └── requirements.txt
    |
    ├── database/
    |   └── README.md
    |
    ├── frontend/
    |   ├── src/
    |   ├── public/
    |   ├── package.json
    |   └── ...
    |
    ├── ml/
    |   ├── data/
    |   |   ├── facility_hygiene_ml_dataset.xlsx
    |   |   └── cleaned_hygiene_dataset.csv
    |   |
    |   ├── models/
    |   |   └── hygiene_risk_model.pkl
    |   |
    |   ├── src/
    |   |   ├── 01_data_inspection.py
    |   |   ├── 02_dataset_profile.py
    |   |   ├── 03_preprocess.py
    |   |   ├── 04_eda.py
    |   |   ├── 05_train_model.py
    |   |   └── 06_feature_importance.py
    |   |
    |   └── visualizations/
    |       ├── 01_hygiene_risk_distribution.png
    |       ├── 02_cleanliness_by_risk.png
    |       ├── 03_waste_by_risk.png
    |       ├── 04_complaints_by_risk.png
    |       ├── 05_cleaning_time_by_risk.png
    |       ├── 06_facility_type_distribution.png
    |       └── 07_feature_importance.png
    |
    └── README.md
```

---

## 14. Installation

### Prerequisites

Install the following:

* Python 3.10 or higher
* Node.js
* npm
* Git
* Visual Studio Code

### Backend and ML Dependencies

From the project directory:

```powershell
cd "day-10\final-project"
```

Activate the Python virtual environment if required:

```powershell
..\..\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r backend\requirements.txt
```

### Frontend Dependencies

Navigate to the frontend:

```powershell
cd frontend
```

Install dependencies:

```powershell
npm install
```

---

## 15. Environment Variables

The current local version does not require external API keys or secret environment variables.

The frontend currently communicates with the local FastAPI backend at:

```text
http://127.0.0.1:8000
```

For a future production version, the API URL can be moved to an environment variable such as:

```text
VITE_API_URL=http://127.0.0.1:8000
```

This would allow the backend URL to be changed without modifying frontend source code.

---

## 16. How to Run

The backend and frontend should be run in separate terminals.

### Step 1 — Start the Backend

From:

```text
day-10/final-project
```

run:

```powershell
uvicorn backend.app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

Check the health endpoint:

```text
http://127.0.0.1:8000/health
```

Open the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### Step 2 — Start the Frontend

Open another terminal:

```powershell
cd "day-10\final-project\frontend"
```

Run:

```powershell
npm run dev
```

Open the URL displayed by Vite, normally:

```text
http://localhost:5173/
```

### Step 3 — Make a Prediction

1. Enter facility information.
2. Click **Predict Hygiene Risk**.
3. The frontend sends the data to the FastAPI `/predict` endpoint.
4. The backend sends the processed data through the trained ML pipeline.
5. The model predicts High, Medium, or Low risk.
6. Prediction probabilities are returned.
7. The frontend displays the result and stores it in the current-session prediction history.

---

## 17. Screenshots

Screenshots should be added to a `screenshots/` directory in the final submission.

Recommended screenshots:

### Main Dashboard

```text
screenshots/dashboard.png
```

Shows the main prediction form.

### High-Risk Prediction

```text
screenshots/high-risk-prediction.png
```

Shows a prediction result and probability values.

### Low-Risk Prediction

```text
screenshots/low-risk-prediction.png
```

Shows a different facility input and its prediction.

### Prediction History

```text
screenshots/prediction-history.png
```

Shows multiple predictions stored during the current session.

### FastAPI Documentation

```text
screenshots/api-docs.png
```

Shows the FastAPI Swagger documentation.

### Feature Importance

```text
screenshots/feature-importance.png
```

Shows the generated ML feature importance visualization.

---

## 18. Challenges Faced

### Challenge 1 — Missing Values

The original dataset contained missing values in numerical and categorical columns.

**Solution:**
Numerical missing values were filled using median imputation, while categorical missing values were filled using the mode.

### Challenge 2 — Duplicate Records

The original dataset contained 5 duplicate records.

**Solution:**
Duplicate records were identified and removed during preprocessing, reducing the dataset from 1000 to 995 records.

### Challenge 3 — Date Feature Processing

The inspection date could not be directly used as a suitable numerical model feature.

**Solution:**
The inspection date was converted into inspection month and day-of-week features.

### Challenge 4 — Categorical Features

Location, facility type, and water availability contained categorical values.

**Solution:**
`OneHotEncoder` was used to convert categorical features into numerical representations.

### Challenge 5 — Logistic Regression Convergence

The initial Logistic Regression training produced a convergence warning.

**Solution:**
`StandardScaler` was added to the numerical preprocessing pipeline and the Logistic Regression iteration limit was increased to 1000.

### Challenge 6 — Frontend and Backend Integration

The React frontend and FastAPI backend run as separate development applications.

**Solution:**
The frontend communicates with the FastAPI `/predict` endpoint using HTTP requests, and CORS was configured on the backend.

### Challenge 7 — Prediction History

Prediction history needed to be displayed without introducing unnecessary database complexity.

**Solution:**
React state was used to maintain prediction history during the current browser session.

---

## 19. Testing

The major application flows were tested successfully.

### Test Case 1 — High-Risk Prediction

A facility with lower cleanliness, higher odor, higher waste, more complaints, and longer time since cleaning produced:

```text
Prediction: High
```

### Test Case 2 — Low-Risk Prediction

The following cleaner facility input was tested:

```text
Cleanliness Score: 9
Odor Score: 2
Waste Level: 10
Water Availability: Yes
Footfall: 100
Complaints: 0
Hours Since Cleaning: 2
```

Result:

```text
Prediction: Low
```

### Test Case 3 — Input Validation

An invalid cleanliness score of `11` was entered.

The frontend rejected the value because the allowed maximum is `10`.

### Test Case 4 — API Health

The backend health endpoint successfully returned:

```json
{
  "status": "healthy",
  "model_loaded": true
}
```

---

## 20. Future Improvements

The following improvements can be implemented in future versions:

1. Integrate PostgreSQL or MySQL for persistent prediction history.
2. Add user authentication and role-based access.
3. Store facility records and prediction timestamps.
4. Add an administrator dashboard.
5. Add facility-wise risk monitoring.
6. Add historical risk trend visualizations.
7. Add automated alerts for high-risk facilities.
8. Add scheduled model retraining.
9. Deploy the application to cloud infrastructure.
10. Add automated frontend, backend, and ML tests.
11. Move the API URL to environment variables.
12. Add model versioning and monitoring.
13. Experiment with additional machine learning algorithms and hyperparameter tuning.
14. Add model explainability features.

---

## 21. Conclusion

The **Smart Hygiene Risk Prediction System** demonstrates an end-to-end AI/ML application that combines data preprocessing, exploratory data analysis, machine learning, REST API development, and a React-based user interface.

The final Logistic Regression model achieved **93.97% test accuracy** and a **93.99% weighted F1-score** on the prepared test dataset.

The completed system allows a user to enter facility information, receive a hygiene risk prediction with probability values, and view predictions generated during the current browser session.

The project demonstrates the complete workflow from **raw data to a working ML-powered web application**.

