import streamlit as st
import pandas as pd

from ds_salary_predictor.config import Config

st.set_page_config(page_title="Training Report")

@st.cache_data
def get_report():
    return pd.read_csv(Config.report_path)

st.title("Model Training Report")
st.markdown("All the models are trained on the same dataset")

report = get_report()
st.dataframe(report, hide_index=True)
st.markdown(f"### *{report['Model'].iloc[report['RMSE'].argmin()]}* is selected for prediction "+
            "since it has the least error (RMSE).") 