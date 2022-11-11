from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = Service(
    "C:\Development\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
URL = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(URL)

article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# Click Button with click() method
article_count.click()

pages = driver.find_element(By.LINK_TEXT, "Pages")
pages.click()

# Type anything with .send_keys("WRITE YOUR TEXT HERE") method
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()
