# Ford Car Dataset Price Prediction

## Overview
This notebook contains a complete machine learning pipeline for predicting Ford car prices using Logistic Regression. The project demonstrates essential data preprocessing, feature engineering, model training, evaluation, and prediction tasks.

## Dataset
- **Source**: Ford Car Dataset
- **Size**: 17,966 records with 9 features
- **Features**: 
  - `model`: Car model (23 different models)
  - `year`: Year of manufacture
  - `price`: Price of the car (Target variable)
  - `transmission`: Type of transmission (Automatic, Manual, Semi-Auto)
  - `mileage`: Mileage of the car
  - `fuelType`: Type of fuel (Petrol, Diesel, Hybrid, Electric, Other)
  - `tax`: Tax amount
  - `mpg`: Miles per gallon (fuel efficiency)
  - `engineSize`: Engine size in liters

## Data Quality
- **Missing Values**: 0 (No missing values)
- **Duplicates**: 154 duplicate records removed during preprocessing

## Preprocessing & Feature Engineering

### 1. **Categorical Encoding**
   - Applied One-Hot Encoding on categorical features:
     - `model`: 23 categories
     - `transmission`: 3 categories
     - `fuelType`: 5 categories

### 2. **Feature Scaling**
   - Used StandardScaler to normalize numerical features
   - Scaled features: year, mileage, tax, mpg, engineSize

### 3. **Data Split**
   - **Training set**: 80% (14,372 samples)
   - **Testing set**: 20% (3,594 samples)
   - Random state: 42 for reproducibility

## Model Details

### Algorithm: Logistic Regression
- **Purpose**: Regression model to predict car prices
- **Parameters**:
  - Penalty: L2 regularization
  - C (Inverse regularization strength): 1.0
  - Solver: lbfgs (Limited-memory BFGS)
  - Max iterations: 100

### Model Performance
The model was trained on the preprocessed data and evaluated on the test set. Predictions were made successfully with the model stored for future use.

## Output Features
- **Total features after preprocessing**: 36 features
  - 5 original numerical features (scaled)
  - 23 one-hot encoded model categories
  - 3 one-hot encoded transmission categories
  - 5 one-hot encoded fuel type categories

## Model Artifacts
The following files are saved and can be loaded for making predictions:
- `ford_car_dataset.pkl`: Trained Logistic Regression model
- `scaler.pkl`: StandardScaler object for feature scaling
- `columns.pkl`: List of feature names for proper column ordering

## Usage

### Loading the Model
```python
import joblib as jb

# Load saved artifacts
mdl = jb.load("ford_car_dataset.pkl")
sclr = jb.load("scaler.pkl")
column = jb.load("columns.pkl")
```

### Making Predictions
1. Prepare input data with the same structure as training data
2. Apply one-hot encoding to categorical features
3. Scale numerical features using the saved scaler
4. Ensure column order matches the saved columns
5. Use the model to make predictions

## Example Prediction
A sample prediction was made on a test record resulting in a predicted price of **1299** (in the currency units used in the dataset).

## Key Steps in Notebook
1. Data loading and exploration
2. Data quality checks (missing values, duplicates)
3. Feature engineering (one-hot encoding)
4. Feature scaling (StandardScaler)
5. Train-test split (80-20)
6. Model training (Logistic Regression)
7. Model evaluation and reporting
8. Model serialization (saving .pkl files)
9. Model loading and testing on new data

## Requirements
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- joblib

## Note
The notebook uses Python 3.14.5 as specified in the kernel specification.

## Author
Created during Industrial Training Session 22

---
**Last Updated**: 2026-07-22
