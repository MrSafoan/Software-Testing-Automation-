from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.opencart.com/")

driver.find_element(By.XPATH,"//a[normalize-space()='Components']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Mice and Trackballs (0)']").click()

driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//a[@class='btn btn-primary']").click()
#driver.back()













