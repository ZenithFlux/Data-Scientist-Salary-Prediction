FROM python:3.11.5-bookworm
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "streamlit", "run", "Predict_Salary.py" ]
CMD [ "--server.port", "80" ]
EXPOSE 80