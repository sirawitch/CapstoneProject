FROM apache/airflow:2.8.0-python3.11

ARG AIRFLOW_VERSION=2.8.0
ARG PYTHON_VERSION=3.11
USER airflow
COPY ./Airflow/requirements.txt /
RUN pip install --upgrade pip
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" \ 
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt" && \
    pip install --no-cache-dir -r /requirements.txt