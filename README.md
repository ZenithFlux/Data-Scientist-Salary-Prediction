# Data-Scientist-Salary-Prediction 💲💰💹

Predict the salaries of data science professionals using this ML webapp, built using Streamlit <img src="https://docs.streamlit.io/logo.svg" width="22">.  
Click the link below to go to the live site.

**Go to site: https://ds-salary-prediction.streamlit.app/**

Dataset used for training: [Salary Prediction (Kaggle)](https://www.kaggle.com/datasets/thedevastator/jobs-dataset-from-glassdoor)

This application was deployed on **AWS Elastic Container Service**.  
The AWS service is currently *disabled*.

<details>
<summary>View Screenshots</summary>
<img src="https://i.ibb.co/Z8WGzGx/ecs.png" title="Elastic Container Service">

<br />
<img src="https://i.ibb.co/QYDPv42/site.png" title="WebApp">
</details>

# How to run locally 📀💻

## Using Python

1. Clone this repository and move into the folder.  
```bash
git clone https://github.com/ZenithFlux/Data-Scientist-Salary-Prediction.git  
cd Data-Scientist-Salary-Prediction
```

2. Install all dependencies.  
`pip install -r requirements.txt`

3. Run streamlit server.  
`streamlit run Predict_Salary.py`  

The app will be served on *localhost* where it can be viewed using a browser.

## Using Docker <img src="https://creazilla-store.fra1.digitaloceanspaces.com/icons/3253696/docker-icon-icon-md.png" height="20">

If you have docker installed, just run the following command in terminal:  

```bash
docker run -it -p 5000:80 chaitanyalakhchaura12/ds-salary-predictor
```

The app will be served on ***localhost:5000***.  
Type *localhost:5000* in your browser to view the webapp.