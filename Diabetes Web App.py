#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 18:05:33 2025

@author: namanchachan
"""

import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open('/Users/namanchachan/Desktop/Diabetes_Detection /trained_model.sav', 'rb'))


#creating function for prediction
def diabetes_prediction(input_data):
   

    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
    


def main():
    
    #giving title 
    st.title('Diabetes Prediction System Web App')
    
    #getting the input from the user 
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('BloodPressure Value')
    SkinThickness = st.text_input('SkinThickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction Value')
    Age = st.text_input('Age')
    
    #Code for Prediction
    diagnosis = ''
    
    #Creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)
    
    
#Writting command to run through terminal 
if __name__ == '__main__':
    main()