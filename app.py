import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

model = joblib.load('flight_delay_model.pkl')

origins = joblib.load('origins.pkl')
destinations = joblib.load('destinations.pkl')

st.title("Prédiction de Retard de Vol")

origin = st.selectbox("Sélectionnez la ville de départ", origins)
dest = st.selectbox("Sélectionnez la ville d'arrivée", destinations)

date = st.date_input("Sélectionnez la date du vol", datetime.today())

month = date.month
dayofmonth = date.day

if st.button("Prédire le retard"):
    input_data = pd.DataFrame([[origin, dest, month, dayofmonth]], columns=['ORIGIN_CITY_NAME', 'DEST_CITY_NAME', 'MONTH', 'DAY_OF_MONTH'])
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.write("Le vol est susceptible d'avoir un retard.")
    else:
        st.write("Le vol est susceptible de ne pas avoir de retard.")
