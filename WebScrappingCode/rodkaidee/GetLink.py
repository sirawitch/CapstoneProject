from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
chrome_service = ChromeService(
    '/Users/sirawitchtiyasuttipun/Downloads/chromedriver-mac-arm64_2/chromedriver')
driver = webdriver.Chrome(service=chrome_service)
f = open("rodkaidee.txt", "w+")
for page in range(1,44):
    driver.get("https://rod.kaidee.com/c11a12-auto-car-mazda/p-"+str(page))
    # element=driver.find_element(By.XPATH,"//div[@id='Car_List']")
    # data= element.get_attribute("innerHTML")
    html_data = driver.page_source
    soup = BeautifulSoup(html_data, "html.parser")
    links = soup.find_all("a")
    for link in links:
        if link.get("href") == None:
            continue
        elif "/product" in link.get("href"):
            f.write(link.get("href")+"\n")
driver.quit()
print("Done")
# with open('WebScrap/data2023.html', "w", encoding="utf-8") as file:
#    file.write(data)
