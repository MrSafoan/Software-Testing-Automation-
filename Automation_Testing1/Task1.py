from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver  = webdriver.Chrome(service=serv_obj)

# open webpage

driver.get("https://demo.opencart.com/")
