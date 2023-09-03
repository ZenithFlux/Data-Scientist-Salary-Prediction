import streamlit as st
import pandas as pd
import plotly.express as px

from ds_salary_predictor.train_pipeline.data_processing import clean_df
from train import DATASET_PATH


st.set_page_config(page_title="Exploratory Data Analysis")

@st.cache_data
def load_data():
    return clean_df(pd.read_csv(DATASET_PATH))

df = load_data()

st.title("Exploratory Data Analysis")
st.markdown("Answering questions about the data.")

# ---------------------------------------------------------------------------------------------------

st.header("Q1. Which skills are most popular in Data Science world?")

count = {x: df[y].sum() for x, y in {"Python": "python_yn", 
                                  "R": "R_yn", 
                                  "Spark": "spark", 
                                  "AWS": "aws", 
                                  "Excel": "excel"}.items()}

fig = px.bar(x=list(count.keys()), y=list(count.values()),
                       title="Skills Distribution",
                       labels={"x": "", "y": "count"})
st.plotly_chart(fig)

st.markdown("**Inference:** Python and Excel are the most popular skills in data science.")
st.divider()

# ---------------------------------------------------------------------------------------------------

st.header("Q2. What is the salary distribution among data scientists?")
fig = px.histogram(df, "avg_salary", title="Salary distribution",
                   labels={"avg_salary": "Avg. Salary (in thousand USD)"})
fig.update_traces(marker_color="green" ,marker_line_width=1, marker_line_color="lightgreen")
st.plotly_chart(fig)

st.markdown("**Inference:** Salary is normally distributed. Most data scientists earn about 60-120K yearly.")
st.divider()

# ---------------------------------------------------------------------------------------------------

st.header("Q3. How does the distribution of Company Ratings looks like?")
fig = px.histogram(df, "Rating", title="Company Ratings distribution",
                   labels={"Rating": "Company Ratings"})
fig.update_traces(marker_color="violet" ,marker_line_width=1, marker_line_color="white")
st.plotly_chart(fig)

st.markdown("**Inference:** Average company ratings are between 3.5 and 4.0. This is the expected distribution of ratings.")
st.divider()

# ---------------------------------------------------------------------------------------------------

st.header("Q4. Does living in same state affect salary?")
fig = px.box(x=df["avg_salary"],
             y=["Same state" if x==1 else "Not same state" for x in df.same_state],
             labels={"x": "Avg. Salary (in thousand USD)", "y": ""})
st.plotly_chart(fig)

st.markdown("**Inference:**") 
st.markdown("It does not affect salary much. " + 
            "Just people living in same state tend to have a wider salary distribution.")
st.divider()

# ---------------------------------------------------------------------------------------------------

st.header("Q5. Is hourly pay less or more than annual salary?")
fig = px.box(x=df["avg_salary"],
             y=["Hourly Pay" if x==1 else "Not Hourly" for x in df.hourly],
             labels={"x": "Avg. pay (in thousand USD) per year", "y": ""})
fig.update_traces(marker_color="orange")
st.plotly_chart(fig)

st.markdown("**Inference:** Hourly pay is significantly less compared to annual salary for data scientists.")
st.divider()

# ---------------------------------------------------------------------------------------------------

st.header("Q6. How do technical skills affect a data scientist's salary?")

skill = []
salary = []
for s in ["python_yn", "R_yn", "spark", "aws", "excel"]:
    for i, val in enumerate(df[s]):
        if val==0: continue
        s = s.capitalize()
        if s.endswith("_yn"): s = s[:-3]
        if s=="Aws": s = "AWS"
        skill.append(s)
        salary.append(df["avg_salary"][i])
        
fig = px.violin(y=salary, x=skill, box=True, labels={"x": "", "y": "Avg. Salary (in thousand USD)"})
fig.update_traces(marker_color="blue")
st.plotly_chart(fig)

st.markdown("**Inference:**")
st.markdown("1. Python, AWS and Spark knowing professionals have similar salaries.\n" +
            "2. R is not much valued in data science job market.")