from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
chrome_service = ChromeService(
    '/Users/sirawitchtiyasuttipun/Downloads/chromedriver-mac-arm64/chromedriver')
choose = 0
df=pd.DataFrame()
for year in range(2020, 2024):
    # element=driver.find_element(By.XPATH,"//div[@id='Car_List']")
    # data= element.get_attribute("innerHTML")
    #html_data = driver.page_source
    #soup = BeautifulSoup(html_data, "html.parser")
    #links = soup.find_all("a")
    f = open("WebScrap/Link"+str(year)+".txt", "r")
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
    for line in f:
        driver = webdriver.Chrome(service=chrome_service)
        driver.get(line)
        html_data = driver.page_source
        soup = BeautifulSoup(html_data, "html.parser")
        #divs = soup.find_all("div", class_="txt")
        #for div in divs:
        #    print(div)
        divs = soup.find_all("div", class_="txt")
        # Extract and print the text from each div
        skip = 0
        afterbaht=0
        otherdata=""
        for div in divs:
            text_data = div.get_text()
            if "บาท" in text_data and afterbaht==0:
                split1 = text_data.split("ใช้มาแล้ว ")
                if(len(split1)==1):
                    skip=1
                    break
                generalInfo = split1[0]
                split2 = split1[1].split("กม.")
                if(len(split2)==1):
                    skip=1
                    break
                km = split2[0]
                split3 = split2[1].split("ราคา\xa0")
                if(len(split3)==1):
                    skip=1
                    break
                update = split3[0]
                if(len(split3[1])<8):
                    skip=1
                    break
                cost = split3[1][:-6]
                afterbaht=1
            elif afterbaht==0:
                head = text_data
            else:
                otherdata+=text_data
        if skip==1:
            print(line)
            driver.close()
            continue
        row =  pd.DataFrame({'Version':[head],'generalInfo':[generalInfo],'distance':[km],'update':[update],'cost':[cost],'other':[otherdata]})
        df=pd.concat([df,row])
        driver.close()
df.to_csv("WebScrap/DataWithOtherData3.csv",index=False)
print("Done")