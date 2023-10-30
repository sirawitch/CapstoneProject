from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
chrome_service = ChromeService(
    '/Users/sirawitchtiyasuttipun/Downloads/chromedriver-mac-arm64_2/chromedriver')
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
        soup = BeautifulSoup(html_data, "html.parser")
        costDiv = soup.find("div", class_ ="u-order-1@mobile u-margin-right-xs@mobile u-color-white u-text-3 u-text-4@mobile u-text-bold u-margin-bottom-none u-margin-top-xxs")
        # Extract and print the text from each div
        if(costDiv==None):
              driver.quit()
              continue
        skip = 0
        afterbaht=0
        otherdata=""
        text_data = costDiv.get_text()
        if("บาท" in text_data):
                cost = text_data[0:-4]
        name = soup.select('h1.listing__title')[0].text.strip()
        div = soup.find_all("div", class_ ="c-card__body u-bg-haze-light u-flex u-flex--column")
        for i in div:
            text = i.get_text()
            if("สภาพ" in text):
                  status = text[9:-1]
            elif("เลขไมล์" in text):
                 mile = text[18:-1]
            elif("สี" in text):
                   color = text[7:-1]
            elif("ระบบเกียร์" in text):
                  gear = text[15:-1]
        d=pd.DataFrame({'id':[id],'name':[name],'cost':[cost],'mile':[mile],'status':[status],'color':[color],'gear':[gear],'web':['one2car'],'webid':[webid],'date':[today]})
        df=pd.concat([df,d])
        driver.quit()
df.to_csv("DataFromOne2Car.csv",index=False)
print("Done")