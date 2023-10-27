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
        div = soup.find("div", class_ ="group-price")
        if(div==None):
              driver.quit()
              continue
        text_data = div.get_text()
        if("฿" in text_data):
                #print(text_data[51:])
                cost = text_data[51:]
        
        name = soup.select('h1.title')[0].text.strip()
        #print(name)
        Car = div
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
        seller = div.find("div",class_="title")
        seller=seller.get_text()
        div = soup.find("div",class_="box-detail-seller")
        address = div.find("ul").find("li")
        address = address.get_text().strip()
        d=pd.DataFrame({'id':[id],'name':[name],'cost':[cost],'mile':[mile],'gear':[gear],'seller':[seller],'address':[address],'web':['chobrod'],'webid':[webid[1:]],'date':[today]})
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
df.to_csv("DataFromChobrod.csv",index=False)
print("Done")