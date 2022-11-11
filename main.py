# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# chrome_driver_path = Service(
#     "C:\Development\chromedriver_win32\chromedriver.exe")

# driver = webdriver.Chrome(service=chrome_driver_path)
# URL = "https://www.amazon.com/Mad-Honey-Novel-Jodi-Picoult/dp/1984818384/ref=tmm_hrd_swatch_0?_encoding=UTF8&qid=1668137327&sr=8-2-fkmr3"
# driver.get(URL)
# price = driver.find_element(By.XPATH, '//*[@id="price"]')
# print(price.text)
# driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service(
    "C:\Development\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
URL = "https://www.python.org/"
driver.get(URL)

events = driver.find_element(
    By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul').text.splitlines()
events_dict = {i: {"time": events[i], "name": events[i+1]}
               for i in range(0, len(events), 2)}
print(events_dict)
driver.quit()
