# mkdir -p ./dags ./logs ./plugins ./config
docker build -t webscrap-airflow:0.01 -f ./Airflow/Dockerfile .
docker compose -f ./Airflow/docker-compose.yml up
