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
f = open("carsome.txt", "r")
driver = webdriver.Chrome(service=chrome_service)
today = date.today()
id=0
for line in f:
        id+=1
        webid=line
        driver = webdriver.Chrome(service=chrome_service)
        driver.get("https://www.carsome.co.th"+line)
        html_data = driver.page_source
        soup = BeautifulSoup(html_data, "html.parser")
        priceDiv = soup.find("div",class_="car-price__decoration")
        if(priceDiv != None):
            price = priceDiv.get_text().strip()
        else:
             price="-"
        salePriceDiv = soup.find("div",class_="car-price")
        salePriceDiv = salePriceDiv.find("div",class_="price")
        salePrice = salePriceDiv.get_text().strip()
        nameDiv = soup.find("div",class_="vehicle__title-wrapper car-title-wrapper")
        name = nameDiv.get_text().strip()
        if(soup.find("div",class_="car-all__location-descs")==None):
             address="-"
        else:address = soup.find("div",class_="car-all__location-descs").get_text().strip()
        infoDiv =soup.find("div",class_="car-details-content").find_all("div",class_="detail-item")
        for div in infoDiv:
            text = div.get_text()
            if "เชื้อเพลิง" in text:
                 fuel = text.strip()[17:]
                 #print(text.strip()[17:])
            elif "สี" in text:
                 color = text.strip()[3:]
                 #print(text.strip()[3:])
            elif "ระยะทาง" in text:
                 km = text.strip()[14:-4]
                 #print(text.strip()[14:-4])
        injure = soup.find("div", class_="damage-images").find("div",class_="swiper-box").get_text().strip()
        d=pd.DataFrame({'id':[id],'name':[name],'price':[price],'salePrice':[salePrice],'distance':[km],'fuel':[fuel],'color':[color],'address':[address],'injure':[injure],'web':['carsome'],'webid':[webid[1:]],'date':[today]})
        df=pd.concat([df,d])
        driver.quit()
        continue
        if skip==1:
            print(line)
            driver.close()
            continue
        row =  pd.DataFrame({'Version':[head],'generalInfo':[generalInfo],'distance':[km],'update':[update],'cost':[cost],'other':[otherdata]})
        df=pd.concat([df,row])
        driver.close()
df.to_csv("DataFromCarsome.csv",index=False)
print("Done")