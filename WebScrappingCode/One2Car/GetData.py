from bs4 import BeautifulSoup
import pandas as pd
from datetime import date, timedelta
import requests
import os.path

today = date.today()

# define path
link_path = f"/opt/airflow/WebScrapData/One2Car/Link_{today.month}_{today.year}.txt"
existing_dimension_path = (
    f"/opt/airflow/WebScrapData/One2Car/dimension_{today.month}_{today.year}.csv"
)

# init var
every_car_basic_info = pd.DataFrame()
every_car_transaction_info = pd.DataFrame()
every_car_all_info = pd.DataFrame()
link_file = open(link_path, "r")
dimension_column_names = ["webid", "name", "mile", "color", "gear", "web"]
transaction_column_names = ["webid", "status", "cost", "date"]
existing_dimension_df = None

# check for existing car information file
if os.path.isfile(existing_dimension_path):
    existing_dimension_df = pd.read_csv(existing_dimension_path)
else:
    existing_dimension_df = pd.DataFrame(columns=dimension_column_names)

for line in link_file:
    webid = line[33:]

    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }
    respond = requests.get(line, headers=headers)
    html_data = respond.content

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
    # webid as identifier of a car

    dim_car_attribute = pd.DataFrame(
        {
            "webid": [webid],
            "name": [name],
            "mile": [mile],
            "color": [color],
            "gear": [gear],
            "web": ["one2car"],
        }
    )

    fact_car_transcation = pd.DataFrame(
        {
            "webid": [webid],
            "status": [status],
            "cost": [cost],
            "date": [today],
        }
    )

    every_car_all_info = pd.concat([every_car_all_info, car_all_info])

every_car_all_info.to_csv(
    f"/opt/airflow/WebScrapData/One2Car/{today.month}_{today.year}.csv",
    index=False,
    mode="a",
)


print("Done")
