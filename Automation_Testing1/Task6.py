from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.opencart.com/")
driver.find_element(By.XPATH,"//*[@id='top']/div[2]/div[2]/ul/li[2]/div/a").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()

msg1 = driver.find_element(By.CSS_SELECTOR,"#column-right > div").text
print(msg1)
print("#######################################################")
msg2 = driver.find_element(By.CSS_SELECTOR,"body > footer > div").text
print(msg2)
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
driver.find_element(By.CSS_SELECTOR,"#column-right > div > a:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR,"#column-right > div > a:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR,"#column-right > div > a:nth-child(3)").click()
driver.find_element(By.CSS_SELECTOR,"#column-right > div > a:nth-child(4)").click()
driver.find_element(By.CSS_SELECTOR,"#column-right > div > a:nth-child(5)").click()
driver.find_element(By.CSS_SELECTOR,"#column-right > div > a:nth-child(6)").click()
driver.find_element(By.CSS_SELECTOR,"#column-right > div > a:nth-child(7)").click()
driver.find_element(By.CSS_SELECTOR,"#column-right > div > a:nth-child(8)").click()
driver.find_element(By.CSS_SELECTOR,"#column-right > div > a:nth-child(9)").click()
driver.find_element(By.CSS_SELECTOR,"#column-right > div > a:nth-child(10)").click()

#element = WebDriverWait(driver,10).until(EC.element_to_be_clickable(By.XPATH,"//*[@id='column-right']/div/a[11]"))
#element.click()
#driver.find_element(By.CSS_SELECTOR,"#column-right > div > a:nth-child(11)").click()
#driver.find_element(By.CSS_SELECTOR,"#column-right > div > a:nth-child(12)").click()
#driver.find_element(By.CSS_SELECTOR,"#column-right > div > a:nth-child(13)").click()
