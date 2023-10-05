from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
chrome_service = ChromeService(
    '/Users/sirawitchtiyasuttipun/Downloads/chromedriver-mac-arm64/chromedriver')
choose = 0
for year in range(1996, 2024):
    driver = webdriver.Chrome(service=chrome_service)
    driver.get('https://www.taladrod.com/w40/isch/schc.aspx?fno:all+mk:32+gr:b+y1:' +
               str(year)+'+y2:'+str(year)+'+gs:n')
    # element=driver.find_element(By.XPATH,"//div[@id='Car_List']")
    # data= element.get_attribute("innerHTML")
    html_data = driver.page_source
    soup = BeautifulSoup(html_data, "html.parser")
    links = soup.find_all("a")
    f = open("WebScrap/Link"+str(year)+".txt", "w")
    for link in links:
        if link.get("href") == None:
            continue
        if "../icar" in link.get("href"):
            choose = 1-choose
            if choose == 0:
                continue
            print("https://www.taladrod.com/w40"+link.get("href")[2:])
            f.write("https://www.taladrod.com/w40"+link.get("href")[2:]+"\n")
    driver.close()
print("Done")
# with open('WebScrap/data2023.html', "w", encoding="utf-8") as file:
#    file.write(data)
