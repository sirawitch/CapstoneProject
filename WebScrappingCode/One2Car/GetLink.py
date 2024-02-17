def getLink():

    from bs4 import BeautifulSoup
    import requests
    import os

    f = open(f"{os.environ['AIRFLOW_HOME']}/link.txt", "w")

    # for page in range(1, 97):
    for page in range(1, 2):
        headers = {
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
        }
        one2car_URL = "https://www.one2car.com/รถ-สำหรับ-ขาย/mazda?type=used&page_size=26&page_number="
        respond = requests.get(one2car_URL + f"{page}", headers=headers)
        html_data = respond.content

        soup = BeautifulSoup(html_data, "html.parser")
        links = soup.find_all("a")
        laststr = "test"
        for link in links:
            if link.get("href") == None:
                continue
            if "one2car.com/for-sale" in link.get("href"):
                if laststr == link.get("href"):
                    continue
                laststr = link.get("href")
                f.write(link.get("href") + "\n")

    f.close()
    print("Done")


from datetime import date
from airflow.providers.amazon.aws.transfers.local_to_s3 import (
    LocalFilesystemToS3Operator,
)
import os

create_link_object = LocalFilesystemToS3Operator(
    task_id="create_link_object",
    dest_bucket="aws-ia-mwaa-502983918849",
    dest_key=f"data/link-{date.today()}.txt",
    filename=f"{os.environ['AIRFLOW_HOME']}/link.txt",
    replace=True,
    aws_conn_id="s3_conn",
)
