from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import requests
chrome_service = ChromeService(
    '/Users/sirawitchtiyasuttipun/Downloads/chromedriver-mac-arm64_2/chromedriver')
choose = 0
df=pd.DataFrame()
f = open("rodkaidee.txt", "r")
driver = webdriver.Chrome(service=chrome_service)
today = date.today()
id=0
c=0
for line in f:
        id+=1
        webid=line
        #driver = webdriver.Chrome(service=chrome_service)
        #driver.get("https://rod.kaidee.com"+line)
        if(id%100==0):
            print(id)
        #html_data = driver.page_source
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        html_data = requests.get("https://rod.kaidee.com"+line,headers=header).text
        soup = BeautifulSoup(html_data, "html.parser")
        #print(line)
        if soup.find("div",class_="sc-y6put5-0")==None:
             title="-"
        else:title = soup.find("div",class_="sc-y6put5-0").get_text().strip()
        info = soup.find("div",class_="sc-1w68tq4-0 sc-1lmqj83-2 cAlovi hmXids")
        if(info == None):
             continue
        if info.find("div",class_="sc-12ljfib-0")==None:
             price="-"
        else:price = info.find("div",class_="sc-12ljfib-0").get_text().strip()[:-31]
        alllist = info.findAll('li')
        for li in alllist:
            text = li.get_text().strip()
            if "เลขไมล์" in text:
                km=text[7:-4]
            elif "ยี่ห้อ" in text:
                 brand=text[6:]
            elif "รุ่นย่อย" in text:
                 subversion=text[8:]
            elif "รุ่น" in text:
                 version=text[4:]
            elif "ประเภทย่อย" in text:
                 subtype=text[10:]
            elif "ประเภทรถ" in text:
                 cartype=text[8:]
            elif "ปีรถ" in text:
                 year=text[4:]
            elif "สี" in text:
                 color=text[2:]
            elif "แก๊ส" in text:
                gas=text[4:]
            elif "เกียร์" in text:
                 gear=text[6:]
            elif "เชื้อเพลิง" in text:
                 fuel=text[10:]
        seller = soup.find("div",class_="sc-1k125n6-2").get_text().strip()
        address = soup.findAll("span",class_="sc-3tpgds-0 kBbZux sc-mj06cq-1 biQatR")[1].get_text().strip()
        d=pd.DataFrame({'id':[id],'title':[title],'price':[price],'brand':[brand],'subversion':[subversion],'version':[subversion],'subtype':[subtype],'cartype':[cartype],'year':[year],'distance':[km],'fuel':[fuel],'gear':[gear],'color':[color],'gas':[gas],'seller':[seller],'address':[address],'web':['rodkaidee'],'webid':[webid],'date':[today]})
        df=pd.concat([df,d])
df.to_csv("DataFromrodkaidee.csv",index=False)
print("Done")
