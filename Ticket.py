import numpy as np
import pandas as pd
import streamlit as st 
import joblib

regressor=joblib.load('Model.pkl')


def welcome():
    return "Welcome All"


def predict_Ticket(Airline,	Source,	Destination, Total_Stops ,arrival_hour,	arrival_min	,Duration_hour,	Duration_min ,journey_Month ,journey_Date ,Dep_hour , Dep_min):
  prediction=regressor.predict(pd.DataFrame({'Airline':[Airline],'Source':[Source]	,'Destination':[Destination],	'Total_Stops':[Total_Stops],	'arrival_hour':[arrival_hour],'arrival_min':[arrival_min],'Duration_hour':[Duration_hour],	
  'Duration_min':[Duration_min],	'journey_Month':[journey_Month],'journey_Date':[journey_Date],'Dep_hour':[Dep_hour],'Dep_min':[Dep_min]}))
  print(prediction)
  return  prediction
def main():
    st.title("AirLines Ticket price prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit AirLines Ticket price prediction App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Airline = st.selectbox("Airline",['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia'])
    Source = st.selectbox("Source",['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])
    Destination = st.selectbox("Destination",['Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Hyderabad'])
    Total_Stops = st.slider("Total_Stops" , min_value= 0 , max_value=4 , value=0,step=1)
    arrival_hour = st.slider("arrival_hour" , min_value= 0 , max_value=23 , value=0,step=1)
    arrival_min = st.slider("arrival_min" , min_value= 0 , max_value=55 , value=0,step=5)
    Duration_hour = st.slider("Duration_hour" , min_value= 0 , max_value=50 , value=0,step=1)
    Duration_min = st.slider("Duration_min" , min_value= 0 , max_value=55 , value=0,step=5)
    journey_Month =st.selectbox("journey_Month" ,['3', '4', '5', '6'])
    journey_Date = st.slider("journey_Date" , min_value= 1 , max_value=30 , value=1,step=1)
    Dep_hour = st.slider("Dep_hour" , min_value= 0 , max_value=23 , value=0,step=1)
    Dep_min = st.slider("Dep_min" , min_value= 0 , max_value=55 , value=0,step=5)
    result=""
    if st.button("Predict"):
        result=predict_Ticket(Airline,	Source,	Destination, Total_Stops ,arrival_hour,	arrival_min	,Duration_hour,	Duration_min ,journey_Month ,journey_Date ,Dep_hour , Dep_min)
    st.success('The price is {} '.format(result))
    if st.button("About"):
        st.text("our app using streamlit")
        st.text("best of luck in your GP")
if __name__=='__main__':
    main()        
