import pandas as pd
import numpy as np
import datetime
import streamlit as st
import joblib

def main():
    html_temp = """
        <h1>Heart Disease Prediction</h1>
    """

    model = joblib.load('decision_tree.joblib')

    st.markdown(html_temp, unsafe_allow_html=True)

    st.markdown("This app will help you to predict heart disease...")
    
    p1 = st.number_input("Please enter your age", 20,80)

    s1 = st.selectbox("Select your gender",("Male","Female"))
    if s1=='Male':
        p2=0
    elif s1=='Female':
        p2=1

    p3 = st.number_input("Please enter your cp", 0,3)						
    p4 = st.number_input("Please enter your trestbps", 80,220)
    p5 = st.number_input("Please enter your chol", 40,600)
    p6 = st.number_input("Please enter your fbs", 0,1)
    p7 = st.number_input("Please enter your restecg", 0,2)
    p8 = st.number_input("Please enter your thalach", 60,220)
    p9 = st.number_input("Please enter your exang", 0,1)
    p10 = st.number_input("Please enter your oldpeak", 0.1,7.0,step=1.0)
    p11 = st.number_input("Please enter your slope", 0,2)
    p12 = st.number_input("Please enter your ca", 0,4)
    p13 = st.number_input("Please enter your thal", 0,3)
				
    data_new = pd.DataFrame({
    'age':52,
    'sex':1,
    'cp':0,
    'trestbps':125,
    'chol':212,
    'fbs':0,
    'restecg':1,
    'thalach':168,
    'exang':0,
    'oldpeak':1.0,
    'slope':2,
    'ca':2,
    'thal':3
},index=[0])


    if st.button("Predict"):
        pred = model.predict(data_new)
        if pred==0:
            st.success("No... You Don't Have Heart Disease".format(pred[0]))
        else:
            st.success("Yes... You Have Heart Disease".format(pred[0]))

if __name__ == '__main__':
    main()