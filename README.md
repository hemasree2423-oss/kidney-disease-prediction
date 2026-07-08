# Kidney Disease Prediction System

## Overview

The Kidney Disease Prediction System is a Machine Learning web application that predicts the likelihood of Chronic Kidney Disease (CKD) based on patient clinical parameters.

The project covers the complete machine learning workflow including data preprocessing, model training, web application development, and deployment.

## Features

* Predicts the likelihood of kidney disease using clinical data.
* User-friendly and interactive web interface.
* Displays prediction results instantly.
* Deployed online for public access.

## Technologies Used

* Python
* Streamlit
* NumPy
* Pandas
* Scikit-learn
* Pickle

## Input Parameters

The model uses the following patient details for prediction:

* Age
* Blood Pressure
* Specific Gravity
* Albumin
* Sugar
* Blood Glucose Random
* Blood Urea
* Serum Creatinine
* Sodium
* Potassium
* Hemoglobin
* Packed Cell Volume
* White Blood Cell Count
* Red Blood Cell Count
* Hypertension
* Diabetes Mellitus
* Anemia
* And other clinical indicators

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd kidney-disease-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Live Demo

Application Link:
Add your deployed application link here.

## Project Structure

```text
├── app.py
├── kidney_model.pkl
├── requirements.txt
|___ runtime.txt
|___ intern2.py
└── README.md
```

## Disclaimer

This application is intended for educational and research purposes only and should not be used as a substitute for professional medical advice or diagnosis.

## Author

Hemasree
