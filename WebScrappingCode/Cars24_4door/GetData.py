from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
chrome_service = ChromeService(
    '/Users/sirawitchtiyasuttipun/Downloads/chromedriver-mac-arm64_2/chromedriver')
choose = 0
df=pd.DataFrame()
f = open("cars24_4door_link.txt", "r")
driver = webdriver.Chrome(service=chrome_service)
today = date.today()
id=0
for line in f:
        id+=1
        webid=line
        driver = webdriver.Chrome(service=chrome_service)
        driver.get(line)
        html_data = driver.page_source
        soup = BeautifulSoup(html_data, "html.parser")
        name = soup.select('h1._3iDrO')[0].text.strip()
        addName = soup.select('p.qKPAR')[0].text.split('|')[0].strip()
        price =soup.select('strong.GBIX0')[0].text.split('บาท')
        notSalePrice = price[0].strip()
        salePrice = price[1].strip()
        info = soup.find("div",class_="_2X4e9").find_all("div",class_="_2X_Gu")
        for div in info:
            text = div.get_text()
            if "ออกรถ" in text:
                year=text[10:]
            elif "ทะเบียน" in text:
                tabian=text[8:]
            elif "สี" in text:
                color=text[2:]
            elif "เกียร์" in text:
                 gear=text[10:]
            elif "เครื่องยนต์" in text:
                fuel=text[11:]
            elif "ระยะทาง" in text:
                km=text[13:-4]
        injure = soup.find("div",class_="_1Wk7G").get_text().strip()
        d=pd.DataFrame({'id':[id],'year':[year],'tabian':[tabian],'name':[name],'addName':[addName],'salePrice':[salePrice],'notSalePrice':[notSalePrice],'distance':[km],'fuel':[fuel],'gear':[gear],'color':[color],'injure':[injure],'door':[4],'address':['Bangkok'],'web':['cars24'],'webid':[webid],'date':[today]})
        df=pd.concat([df,d])
        driver.quit()
df.to_csv("DataFromCars24.csv",index=False)
print("Done")