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
    # element=driver.find_element(By.XPATH,"//div[@id='Car_List']")
    # data= element.get_attribute("innerHTML")
    #html_data = driver.page_source
    #soup = BeautifulSoup(html_data, "html.parser")
    #links = soup.find_all("a")
f = open("one2car.txt", "r")
    #for link in links:
    #    if link.get("href") == None:
    #        continue
    #    if "../icar" in link.get("href"):
    #        choose = 1-choose
    #        if choose == 0:
    #            continue
    #        print("https://www.taladrod.com/w40"+link.get("href")[2:])
    #        f.write("https://www.taladrod.com/w40"+link.get("href")[2:]+"\n")
    #driver.close()
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
        #divs = soup.find_all("div", class_="txt")
        #for div in divs:
        #    print(div)
        
        div = soup.find("div", class_ ="u-order-1@mobile u-margin-right-xs@mobile u-color-white u-text-3 u-text-4@mobile u-text-bold u-margin-bottom-none u-margin-top-xxs")
        # Extract and print the text from each div
        if(div==None):
              driver.quit()
              continue
        skip = 0
        afterbaht=0
        otherdata=""
        text_data = div.get_text()
        if("บาท" in text_data):
                #print(text_data[0:-4])
                cost = text_data[0:-4]
        name = soup.select('h1.listing__title')[0].text.strip()
        #print(name)
        Car = div
        div = soup.find_all("div", class_ ="c-card__body u-bg-haze-light u-flex u-flex--column")
        for i in div:
            text = i.get_text()
            if("สภาพ" in text):
                  status = text[9:-1]
                  #print(text[9:-1])
            elif("ปีที่ผลิต" in text):
                  a=1
                  #print(text[14:-1])
            elif("เลขไมล์" in text):
                 mile = text[18:-1]
                 #print(text[18:-1])
            elif("สี" in text):
                   color = text[7:-1]
                   #print(text[7:-1])
            elif("ขนาดเครื่องยนต์" in text):
                  a=1
                  #print(text[20:-1])
            elif("ระบบเกียร์" in text):
                  gear = text[15:-1]
                  #print(text[15:-1])
            #print("-----------------------")
        d=pd.DataFrame({'id':[id],'name':[name],'cost':[cost],'mile':[mile],'status':[status],'color':[color],'gear':[gear],'web':['one2car'],'webid':[webid],'date':[today]})
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
df.to_csv("DataFromOne2Car.csv",index=False)
print("Done")