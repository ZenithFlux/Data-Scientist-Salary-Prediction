import streamlit as st
import pandas as pd

from ds_salary_predictor.config import Config

@st.cache_data
def get_report():
    return pd.read_csv(Config.report_path)

st.title("Model Training Report")
st.markdown("All the models are trained on the same dataset")

report = get_report()
st.dataframe(report, hide_index=True)
st.markdown(f"### The Best Model for prediction is *{report['Model'].iloc[report['RMSE'].argmin()]}*.") 