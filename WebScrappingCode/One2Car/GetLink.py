from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
chrome_service = ChromeService(
    '/Users/sirawitchtiyasuttipun/Downloads/chromedriver-mac-arm64_2/chromedriver')
choose = 0
driver = webdriver.Chrome(service=chrome_service)
page=1
f = open("one2car.txt", "w+")
for page in range(1,97):
    driver.get('https://www.one2car.com/รถ-สำหรับ-ขาย/mazda?type=used&page_size=26&page_number='+str(page))
    # element=driver.find_element(By.XPATH,"//div[@id='Car_List']")
    # data= element.get_attribute("innerHTML")
    html_data = driver.page_source
    soup = BeautifulSoup(html_data, "html.parser")
    links = soup.find_all("a")
    laststr="test"
    for link in links:
        if link.get("href") == None:
            continue
        if "one2car.com/for-sale" in link.get("href"):
            if(laststr == link.get("href")):
                continue
            laststr = link.get("href")
            print(link.get("href"))
            f.write(link.get("href")+"\n")
    
driver.quit()
print("Done")
# with open('WebScrap/data2023.html', "w", encoding="utf-8") as file:
#    file.write(data)
