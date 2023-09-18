FROM apache/airflow:latest-python3.11
COPY --chown=airflow:root WebScrappingCode /opt/airflow/WebScrappingCode
ARG AIRFLOW_VERSION=2.7.1
ARG PYTHON_VERSION=3.11
COPY ./Airflow/requirements.txt /
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" \ 
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-main/constraints-${PYTHON_VERSION}.txt" \
    -r /requirements.txt
USER airflow