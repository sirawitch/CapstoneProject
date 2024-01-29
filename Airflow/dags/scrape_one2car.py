import datetime
import logging
import pendulum
from airflow.decorators import task
from airflow import DAG

DAG_NAME = "scrap_one2car"
log = logging.getLogger(__name__)

with DAG(
    DAG_NAME,
    schedule="0 0 * * *",
    default_args={"depends_on_past": False},
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
):

    @task(
        task_id="get_link_task",
    )
    def get_link_one2car():
        """
        Scrape the one2car website to get link of cars to be sold
        """
        with open(
            "/opt/airflow/WebScrappingCode/One2Car/GetLink.py"
        ) as get_link_one2car_script:
            exec(get_link_one2car_script.read())

    @task(
        task_id="get_data_task",
    )
    def get_data_one2car():
        """
        Scrape the one2car website to get data of links
        """
        with open(
            "/opt/airflow/WebScrappingCode/One2Car/GetData.py"
        ) as get_data_one2car_script:
            exec(get_data_one2car_script.read())

    def 
    get_link_one2car() >> get_data_one2car()
