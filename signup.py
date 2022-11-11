from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service(
    "C:\Development\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
URL = "http://secure-retreat-92358.herokuapp.com/"
driver.get(URL)
f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("Manish")
l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Bhusal")
email = driver.find_element(By.NAME, "email")
email.send_keys("manish@gmail.com")
email.send_keys(Keys.ENTER)
