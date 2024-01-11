import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.opencart.com/index.php?route=product/category&language=en-gb&path=25_28")
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
driver.find_element(By.XPATH,"//img[@title='Samsung SyncMaster 941BW']").click()
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/form/div/button").click()
msg = driver.find_element(By.XPATH,"//*[@id='content']/div[1]/div[2]/h1").text
msg2 = driver.find_element(By.XPATH,"//ul[@class='list-unstyled']//li//h2").text
msg3 = driver.find_element(By.XPATH,"//li[normalize-space()='Ex Tax: $200.00']").text
print(msg)
print(msg2)
print(msg3)
driver.find_element(By.XPATH,"//a[@id='review-tab']").click()