import streamlit as st
from streamlit.components.v1 import html as st_html
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
from evidently import ColumnMapping
import pandas as pd

from ds_salary_predictor.train_pipeline.data_processing import clean_df


DATASET_PATH = "dataset/salary_data_cleaned.csv"

cm = ColumnMapping(target="avg_salary", numerical_features=["Rating"],
                   categorical_features=["hourly","same_state", "python_yn", "R_yn", "spark", "aws", "excel"])

drift_report = Report([DataDriftPreset()])
drift_report.run(reference_data=clean_df(pd.read_csv(DATASET_PATH)),
                 current_data=clean_df(pd.read_csv(DATASET_PATH)),
                 column_mapping=cm)

st.set_page_config(layout="wide")
st_html(drift_report.get_html(), width=1000, height=1200, scrolling=True)