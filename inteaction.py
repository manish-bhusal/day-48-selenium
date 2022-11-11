from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service(
    "C:\Development\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
URL = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(URL)

article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(article_count.text)


driver.quit()
