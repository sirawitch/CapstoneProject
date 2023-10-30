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
f = open("chobrod.txt", "r")
driver = webdriver.Chrome(service=chrome_service)
today = date.today()
id=0
for line in f:
        id+=1
        webid=line
        driver = webdriver.Chrome(service=chrome_service)
        driver.get("https://chobrod.com"+line)
        html_data = driver.page_source
        soup = BeautifulSoup(html_data, "html.parser")
        costDiv = soup.find("div", class_ ="group-price")
        if(costDiv==None):
              driver.quit()
              continue
        text_data = costDiv.get_text()
        if("฿" in text_data):
                cost = text_data[51:]
        name = soup.select('h1.title')[0].text.strip()
        div = soup.find("div", class_ ="group-inline")
        if(div==None):
              driver.quit()
              continue
        div = div.find_all("div",class_="txt")
        a=0
        for i in div:
            text = i.get_text()
            if(a==0):
                gear=text
            elif(a==1):
                mile = text[:-3]
            a+=1
        div = soup.find("div",class_="box-author")
        seller = div.find("div",class_="title").get_text()
        div = soup.find("div",class_="box-detail-seller")
        address = div.find("ul").find("li").get_text().strip()
        d=pd.DataFrame({'id':[id],'name':[name],'cost':[cost],'mile':[mile],'gear':[gear],'seller':[seller],'address':[address],'web':['chobrod'],'webid':[webid[1:]],'date':[today]})
        df=pd.concat([df,d])
        driver.quit()
df.to_csv("DataFromChobrod.csv",index=False)
print("Done")