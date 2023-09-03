import streamlit as st
import joblib as jl
import numpy as np

from ds_salary_predictor.config import Config

st.set_page_config(page_title="Data Scientist Salary Predictor")

@st.cache_resource
def load_model():
    return jl.load(Config.model_path)

st.title("Predict Salary of a Data Scientist")
st.markdown("Provide the following info about the person and their company")

rating = st.number_input("Company Rating:", 0., 5., 3.5, step=.1)

ans = st.radio("Does the company pay hourly to the data scientist?", ["Yes", "No"], 1)
hourly = 1 if ans=="Yes" else 0

ans = st.radio("Does the data scientist live in the same state as company?", ["Yes", "No"])
same_state = 1 if ans=="Yes" else 0

st.markdown("Which skills does the data scientist possess?")

data = [[rating, hourly, same_state, st.checkbox("Python", True), st.checkbox("R"),
        st.checkbox("Spark"), st.checkbox("AWS"), st.checkbox("Excel")]]

data = np.array(data, dtype=np.float32)

salary = load_model().predict(data)[0]
st.subheader(f"Predicted Salary: ${round(salary)}K")