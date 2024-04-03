<<<<<<< Updated upstream
def getData():
    from bs4 import BeautifulSoup
    import pandas as pd
    from datetime import date, timedelta
    import requests
    import os

    today = date.today()

    # define path
    link_path = f"{os.environ['AIRFLOW_HOME']}/link.txt"

    every_car_all_info = pd.DataFrame()
    link_file = open(link_path, "r")

    for line in link_file[1:3]:
        webid = line[33:]

        headers = {
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
        }
        respond = requests.get(line, headers=headers)
        html_data = respond.content
        print(html_data)
=======
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
chrome_service = ChromeService(
    '/Users/sirawitchtiyasuttipun/Downloads/chromedriver2/chromedriver')
df=pd.DataFrame()
f = open("one2car.txt", "r")
driver = webdriver.Chrome(service=chrome_service)
today = date.today()
id=0
for line in f:
        id+=1
        webid=line[33:]
        #print(line[33:])
        driver = webdriver.Chrome(service=chrome_service)
        driver.get(line)
        html_data = driver.page_source
>>>>>>> Stashed changes
        soup = BeautifulSoup(html_data, "html.parser")
        costDiv = soup.find(
            "div",
            class_="u-order-1@mobile u-margin-right-xs@mobile u-color-white u-text-3 u-text-4@mobile u-text-bold u-margin-bottom-none u-margin-top-xxs",
        )

        # Extract and print the text from each div
        if costDiv == None:
            continue
        skip = 0
        afterbaht = 0
        otherdata = ""
        text_data = costDiv.get_text()
        if "บาท" in text_data:
            cost = text_data[0:-4]
        name = soup.select("h1.listing__title")[0].text.strip()
        div = soup.find_all(
            "div", class_="c-card__body u-bg-haze-light u-flex u-flex--column"
        )
        for i in div:
            text = i.get_text()
            if "สภาพ" in text:
                status = text[9:-1]
            elif "เลขไมล์" in text:
                mile = text[18:-1]
            elif "สี" in text:
                color = text[7:-1]
            elif "ระบบเกียร์" in text:
                gear = text[15:-1]
        car_all_info = pd.DataFrame(
            {
                "name": [name],
                "cost": [cost],
                "mile": [mile],
                "status": [status],
                "color": [color],
                "gear": [gear],
                "web": ["one2car"],
                "webid": [webid],
                "date": [today],
            }
        )

        every_car_all_info = pd.concat([every_car_all_info, car_all_info])

    every_car_all_info.to_csv(
        f"{os.environ['AIRFLOW_HOME']}data.csv",
        index=False,
    )
    link_file.close()
    print("Done")


from datetime import date
from airflow.providers.amazon.aws.transfers.local_to_s3 import (
    LocalFilesystemToS3Operator,
)
import os

create_data_object = LocalFilesystemToS3Operator(
    task_id="create_data_object",
    dest_bucket="aws-ia-mwaa-502983918849",
    dest_key=f"data/data-{date.today()}.csv",
    filename=f"{os.environ['AIRFLOW_HOME']}/data.csv",
    replace=True,
    aws_conn_id="s3_conn",
)
