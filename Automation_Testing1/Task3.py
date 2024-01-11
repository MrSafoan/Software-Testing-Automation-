import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver  = webdriver.Chrome(service=serv_obj)
mywait = WebDriverWait(driver,10,ignored_exceptions=[Exception])

driver.get("https://demo.opencart.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='search']/input").send_keys("Computer")
driver.find_element(By.XPATH,"//*[@id='header-cart']/div/button").click()
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_UP)
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
#time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='carousel-banner-0']/div[1]/button[2]").click()

SearchLink = mywait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='carousel-banner-1']/div[1]/button[3]")))

SearchLink.click()
driver.quit()


