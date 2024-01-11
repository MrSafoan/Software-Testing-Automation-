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
driver.find_element(By.XPATH,"//a[normalize-space()='Monitors (2)']").click()
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
driver.find_element(By.XPATH,"//img[@title='Samsung SyncMaster 941BW']").click()
driver.implicitly_wait(5)
#driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[1]/div[2]/div[1]/form/div/button").click()















