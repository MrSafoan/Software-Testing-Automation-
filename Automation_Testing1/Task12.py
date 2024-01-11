from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.opencart.com/")

driver.find_element(By.XPATH,"//a[normalize-space()='Laptops & Notebooks']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Show All Laptops & Notebooks']").click()
driver.back()










