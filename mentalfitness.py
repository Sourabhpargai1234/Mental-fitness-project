import pickle
import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu


loaded_model=pickle.load(open('C:/Users/Sourabh/OneDrive/Desktop/project/model_id.sav','rb'))

#sidebar
with st.sidebar:
    selected=option_menu('Health Prediction System',
                         ['Mental Health Prediction'],
                         default_index=0)
    
if (selected=='Mental Health Prediction'):
    st.title('Mental Health Prediction')
    age=st.text_input('Age of the person')
    sex=st.text_input('Enter gender')
    cp=st.text_input('Are you self emloyed')
    trestbps=st.text_input('Do your health condition interfere with your work?')
    chol=st.text_input('Do you work remotely or office?')
    fbs=st.text_input('Screen time per day?')
    restecg=st.text_input('Enter your Rest ECG')
    thalach=st.text_input('Enter the sleeing hours')
    exang=st.text_input('Do your emloyeer rovide mental heath benefits?')
    oldpeak=st.text_input('Do you feel stressed while working?')
    slope=st.text_input('Exercise time er day in minutes?')
    ca=st.text_input('your heart rate?')
    thal=st.text_input('Are you diabetic')





diab_diagnosis=''
if st.button('Test Result'):
    print("The person is mentally ill")
    prediction=loaded_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    if(prediction[0]==0):
       diab_diagnosis="The person is not mentally ill"
    else:
       diab_diagnosis="The person is mentally ill"


st.success(diab_diagnosis)