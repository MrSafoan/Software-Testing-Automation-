from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.opencart.com/")
driver.find_element(By.XPATH,"//*[@id='top']/div[2]/div[2]/ul/li[2]/div/a").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
driver.find_element(By.XPATH,"//*[@id='input-firstname']").send_keys("SK")
driver.find_element(By.CSS_SELECTOR,"#input-lastname").send_keys("Safoan")
driver.find_element(By.CSS_SELECTOR,"#input-email").send_keys("safoan@gmail.com")
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
driver.find_element(By.CSS_SELECTOR,"#input-password").send_keys("1234")
driver.find_element(By.CSS_SELECTOR,"#input-newsletter-yes").click()
driver.find_element(By.CSS_SELECTOR,"#form-register > div > div > div > input").click()
time.sleep(5)
driver.quit()