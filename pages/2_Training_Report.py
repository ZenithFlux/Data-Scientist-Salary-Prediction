import streamlit as st
import pandas as pd

from ds_salary_predictor.config import Config

@st.cache_data
def get_report():
    return pd.read_csv(Config.report_path)

st.title("Report of the best models trained on the same data")

st.dataframe(get_report(), hide_index=True)

st.markdown("### Best Model: ***Random Forest***")