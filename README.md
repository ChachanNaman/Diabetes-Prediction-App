# 🩺 Diabetes Prediction Web App

A machine learning-powered **web application** built using **Streamlit** that predicts whether a person is diabetic based on input medical data.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)

---

## 🚀 Overview

This project leverages a trained machine learning model to make real-time predictions on whether a person has diabetes based on several medical features.

Users simply input values like glucose level, BMI, age, and more — and the app instantly returns a prediction.

---

## 📊 Features

- Clean and interactive web interface using **Streamlit**
- Accepts the following inputs:
  - Number of Pregnancies
  - Glucose Level
  - Blood Pressure
  - Skin Thickness
  - Insulin Level
  - BMI
  - Diabetes Pedigree Function
  - Age
- Predicts:
  - ✅ **The person is not diabetic**
  - ❌ **The person is diabetic**

---

## 🛠️ How to Run Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/diabetes-prediction-streamlit.git
cd diabetes-prediction-streamlit

### Step 2: Install dependencies
pip install -r requirements.txt

### Step 3: Launch the Streamlit app

streamlit run diabetes_app.py


Your app will be available at:
🔗 http://localhost:8501


## 🧠 Model Info

- Trained on the **PIMA Indians Diabetes dataset**
- Model: **Support Vector Classifier (SVC)** from `sklearn.svm`
- Saved using `pickle` as `trained_model.sav`


📦 Requirements
Install all required Python packages:
streamlit
numpy
scikit-learn

Generate with:
pip freeze > requirements.txt


**AUTHOR** - NAMAN CHACHAN

**EMAIL** - chachannaman@gmail.com