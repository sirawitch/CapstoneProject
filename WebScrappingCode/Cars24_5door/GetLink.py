from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
chrome_service = ChromeService(
    '/Users/sirawitchtiyasuttipun/Downloads/chromedriver-mac-arm64_2/chromedriver')
choose = 0
driver = webdriver.Chrome(service=chrome_service)
f = open("cars24_5door_link.txt", "w+")
for year in range(2014,2022):
    driver.get('https://www.cars24.co.th/buy-used-cars-bangkok/?rf=year:'+str(year)+";"+str(year)+'&sf=make:Mazda&sf=doors:5&sort=relevance&sf=city:TH_BANGKOK')
    html_data = driver.page_source
    soup = BeautifulSoup(html_data, "html.parser")
    links = soup.find_all("a")
    for link in links:
        if link.get("href") == None:
            continue
        elif "buy-used-mazda" in link.get("href") and "THA" in  link.get("href"):
            f.write(link.get("href")+"\n")
driver.quit()
print("Done")
