from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

f = open("/opt/airflow/WebScrapData/One2Car/Link_new.txt", "w+")

for page in range(1, 97):
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
