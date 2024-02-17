import datetime
import logging
import pendulum
from airflow.decorators import task
from airflow import DAG
from WebScrappingCode.GetLink import getLink, create_link_object
from WebScrappingCode.GetData import getData, create_data_object

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
        getLink()

    @task(
        task_id="get_data_task",
    )
    def get_data_one2car():
        getData()

    get_link_one2car() >> create_link_object >> get_data_one2car() >> create_data_object
